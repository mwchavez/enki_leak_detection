from aws_cdk import (
    Stack,
    Duration,
    aws_dynamodb as dynamodb,
    aws_iot as iot,
    CfnParameter,
    aws_iam as iam,
    aws_sns as sns,
    aws_sns_subscriptions as sub,
    aws_cloudwatch as cloudwatch,
    aws_cloudwatch_actions as cw_actions,
    aws_events as events,
    aws_backup as backup,
)
from constructs import Construct

class LeakDetectionPracticumStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, node_names: list[str], **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       
        for node_name in node_names:
            #Certificate Parameters
            cert_arn = CfnParameter(self, f"CertArn{node_name.capitalize()}",
                description = f"Certificate ARN for {node_name.capitalize()}",
                type = "String"
            )

            #Create an IoT Core device to represent the esp32 and its sensors
            iot_thing = iot.CfnThing(self, f"{node_name.capitalize()}Thing", thing_name = node_name)

            #Create a policy to attach to the nodes, giving them IAM permission to Connect to the IoT Core Server, and Publish/Subscribe to Topics.
            iot_device_policy = iot.CfnPolicy(self, f"{node_name.capitalize()}Policy",
                policy_name = f"leak_detect_{node_name}_policy",
                policy_document = {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": "iot:Connect",
                            "Resource": [f"arn:aws:iot:{Stack.of(self).region}:{Stack.of(self).account}:client/{node_name}"]
                        },
                        {
                            "Effect": "Allow",
                            "Action": "iot:Publish",
                            "Resource": [f"arn:aws:iot:{Stack.of(self).region}:{Stack.of(self).account}:topic/leaksensor/{node_name}/data"]
                        },
                        {
                            "Effect": "Allow",
                            "Action": "iot:Subscribe",
                            "Resource": [f"arn:aws:iot:{Stack.of(self).region}:{Stack.of(self).account}:topicfilter/leaksensor/{node_name}/data"]
                        },
                    ]
                }
            )

            #Tie the Certification to the Thing with a Principal attachment
            iot_thing_principal_attach = iot.CfnThingPrincipalAttachment(self, f"{node_name.capitalize()}ThingAttachment",
                thing_name = node_name,
                principal=cert_arn.value_as_string
            )
            
            iot_thing_principal_attach.add_dependency(iot_thing)


            iot_thing_policy_attach = iot.CfnPolicyPrincipalAttachment(self, f"{node_name.capitalize()}PolicyAttachment",
                policy_name = f"leak_detect_{node_name}_policy",
                principal=cert_arn.value_as_string
            )

            iot_thing_policy_attach.add_dependency(iot_device_policy)


       #Create a DynamoDB table to store the data 
        dynamodb_table = dynamodb.TableV2(self, "LeakDetectionTable",
            partition_key=dynamodb.Attribute(name = "device_id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name = "timestamp", type=dynamodb.AttributeType.NUMBER),
            billing=dynamodb.Billing.on_demand(),
            point_in_time_recovery=True
        )
        
       #Create a backup vault and daily backup plan for the DynamoDB table
        backup_vault = backup.BackupVault(self, "LeakDetectionBackupVault",
            backup_vault_name="LeakDetectionBackupVault"
        )

        backup_plan = backup.BackupPlan(self, "LeakDetectionBackupPlan",
            backup_vault=backup_vault,
            backup_plan_rules=[
                backup.BackupPlanRule(
                    rule_name="DailyBackup",
                    schedule_expression=events.Schedule.cron(hour="3", minute="0"),
                    delete_after=Duration.days(7)
                )
            ]
        )

        backup_plan.add_selection("LeakDetectionTableSelection",
            resources=[backup.BackupResource.from_dynamo_db_table(dynamodb_table)]
        )

       #Give IAM Role permission to write to DynamoDB
        write_to_dynamo_role = iam.Role(self, "IoTCoreDynamoWriteRole",
            assumed_by = iam.ServicePrincipal("iot.amazonaws.com")
        )

        write_to_dynamo_role.add_to_policy(iam.PolicyStatement(
            actions = ["dynamodb:PutItem"],
            resources = [dynamodb_table.table_arn]
        ))

        #Give IoT Rules Engine to put metric data in CloudWatch
        put_metrics_to_cw = iam.Role(self, "IoTCoreSendMetricsToCloudWatch",
            assumed_by = iam.ServicePrincipal("iot.amazonaws.com")
        )

        put_metrics_to_cw.add_to_policy(iam.PolicyStatement(
            actions = ["cloudwatch:PutMetricData"],
            resources = ["*"]
        ))

       #IoT Topic Rule
        iot_storage_topic_rule = iot.CfnTopicRule(self, "LeakDetectionTopicRule",
            topic_rule_payload = iot.CfnTopicRule.TopicRulePayloadProperty(
                sql="SELECT * FROM 'leaksensor/+/data'",
                actions=[
                    iot.CfnTopicRule.ActionProperty(
                        dynamo_d_bv2 = iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item = iot.CfnTopicRule.PutItemInputProperty(
                                table_name = dynamodb_table.table_name,
                            ),
                            role_arn = write_to_dynamo_role.role_arn,
                        )
                    ),

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "moisture",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "Percent",
                            metric_value = "${moisture}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ), 

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "temperature",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${temperature}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ),

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "vibration",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${vibration}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ),

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "acoustic",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${acoustic}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    )

                ]
            ))



       #Create an SNS topic to alert if the data falls out of a certain threshold
        email_01 = CfnParameter(self, "AlertEmail",
            description = "Email address for leak detection alerts",
            type = "String"
        )
        
        leak_alert_topic = sns.Topic(self, "LeakAlertTopic",
            display_name = "Leak Detection Alert"
        )

        leak_alert_topic.add_subscription(
            sub.EmailSubscription(email_01.value_as_string)
        )
      
        #Assign CloudWatch metrics to the custom metric namespace
        moisture_metric = cloudwatch.Metric(
            namespace = "Enki/LeakDetection",
            metric_name = "moisture"
        )
        
        temperature_metric = cloudwatch.Metric(
            namespace = "Enki/LeakDetection",
            metric_name = "temperature"
        )
        
        acoustic_metric = cloudwatch.Metric(
            namespace = "Enki/LeakDetection",
            metric_name = "acoustic"
        )

        vibration_metric = cloudwatch.Metric(
            namespace = "Enki/LeakDetection",
            metric_name = "vibration"
        )

       #Create Cloudwatch alarms to alert if data falls out of a certain threshold
        moisture_alarm = cloudwatch.Alarm(self, "Alarm for High Moisture",
            metric = moisture_metric,
            threshold = 80,
            evaluation_periods=3
        )
        
        temperature_alarm = cloudwatch.Alarm(self, "Alarm for Temperature Spike",
            metric = temperature_metric,
            threshold = 18, 
            evaluation_periods = 3
        )

        acoustic_alarm = cloudwatch.Alarm(self,"Alarm for Acoustic Anomaly",
            metric = acoustic_metric,
            threshold = 500,
            evaluation_periods = 3
        )

        vibration_alarm = cloudwatch.Alarm(self, "Alarm for Vibration Anomaly",
            metric = vibration_metric,
            threshold = 0.3,
            evaluation_periods = 3
        )

        #Connect the CloudWatch alarms to the SNS topic
        moisture_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))
        temperature_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))
        acoustic_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))
        vibration_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))

       #Create a Cloudwatch dashboard to visualize the data in the CloudWatch Metrics
        dashboard = cloudwatch.Dashboard(self, 'LeadDetectDash',
            dashboard_name = "Leak_Detection_Dashboard"
        )

        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title = "Moisture Monitoring",
                left = [moisture_metric]
            ),

            cloudwatch.GraphWidget(
                title = "Temperature Monitoring",
                left = [temperature_metric]
            ),

            cloudwatch.GraphWidget(
                title = "Acoustic Monitoring",
                left = [acoustic_metric]
            ),

            cloudwatch.GraphWidget(
                title = "Vibration",
                left = [vibration_metric]
            )
        )
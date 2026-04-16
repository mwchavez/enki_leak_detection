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

class LeakDetectionStack(Stack):

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
                            metric_name = "${device_id}_moisture",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "Percent",
                            metric_value = "${moisture}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ), 

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "${device_id}_temperature",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${temperature}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ),

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "${device_id}_vibration",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${vibration}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ),

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "${device_id}_acoustic",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${acoustic}",
                            role_arn = put_metrics_to_cw.role_arn
                        )
                    ),

                    iot.CfnTopicRule.ActionProperty(
                        cloudwatch_metric = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name = "${device_id}_confidence_score",
                            metric_namespace = "Enki/LeakDetection",
                            metric_unit = "None",
                            metric_value = "${confidence_score}",
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
        
        
        #Create a dictionary to create and store the CloudWatch metrics for each node
        metrics_by_node = {}
        for node_name in node_names:
            metrics_by_node[node_name] = {
                "moisture": cloudwatch.Metric(
                    namespace = "Enki/LeakDetection",
                    metric_name = f"{node_name}_moisture"
                ),
                
                "temperature": cloudwatch.Metric(
                    namespace = "Enki/LeakDetection",
                    metric_name = f"{node_name}_temperature"
                ),
                
                "acoustic": cloudwatch.Metric(
                    namespace = "Enki/LeakDetection",
                    metric_name = f"{node_name}_acoustic"
                ),

                "vibration": cloudwatch.Metric(
                    namespace = "Enki/LeakDetection",
                    metric_name = f"{node_name}_vibration"
                ),
                "confidence_score": cloudwatch.Metric(
                    namespace = "Enki/LeakDetection",
                    metric_name = f"{node_name}_confidence_score"
                )

            }

       #Create Cloudwatch alarms to alert if data falls out of a certain threshold for each node
        alarms_by_node = {}
        for node_name in node_names:
            moisture_alarm = cloudwatch.Alarm(self, f"Alarm for High Moisture {node_name}",
                metric = metrics_by_node[node_name]["moisture"],
                threshold = 80,
                evaluation_periods = 3
            )
            moisture_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))

            temperature_alarm = cloudwatch.Alarm(self, f"Alarm for Temperature Spike {node_name}",
                metric = metrics_by_node[node_name]["temperature"],
                threshold = 18,
                evaluation_periods = 3
            )
            temperature_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))

            acoustic_alarm = cloudwatch.Alarm(self, f"Alarm for Acoustic Anomaly {node_name}",
                metric = metrics_by_node[node_name]["acoustic"],
                threshold = 500,
                evaluation_periods = 3
            )
            acoustic_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))

            vibration_alarm = cloudwatch.Alarm(self, f"Alarm for Vibration Anomaly {node_name}",
                metric = metrics_by_node[node_name]["vibration"],
                threshold = 0.3,
                evaluation_periods = 3
            )
            vibration_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))

            confidence_score_alarm = cloudwatch.Alarm(self, f"Alarm for Confidence Score {node_name}",
                metric = metrics_by_node[node_name]["confidence_score"],
                threshold = 0.5,
                evaluation_periods = 3
            )
            confidence_score_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))
            
            alarms_by_node[node_name] = {
                "moisture": moisture_alarm,
                "temperature": temperature_alarm,
                "acoustic": acoustic_alarm,
                "vibration": vibration_alarm,
                "confidence_score": confidence_score_alarm,
            }
        
       #Create a Cloudwatch dashboard to visualize the data in the CloudWatch Metrics
        dashboard = cloudwatch.Dashboard(self, 'LeadDetectDash',
            dashboard_name = "Leak_Detection_Dashboard"
        )

        #Add widgets to the dashboard for each node
        for node_name in node_names:
            dashboard.add_widgets(
                cloudwatch.TextWidget(
                    markdown = f"# {node_name}"
                )
            )
            dashboard.add_widgets(
                cloudwatch.GraphWidget(
                    title = f"{node_name}_moisture",
                    left = [metrics_by_node[node_name]["moisture"]]
                ),
                cloudwatch.GraphWidget(
                    title = f"{node_name}_temperature",
                    left = [metrics_by_node[node_name]["temperature"]]
                ),
                cloudwatch.GraphWidget(
                    title = f"{node_name}_acoustic",
                    left = [metrics_by_node[node_name]["acoustic"]]
                ),
                cloudwatch.GraphWidget(
                    title = f"{node_name}_vibration",
                    left = [metrics_by_node[node_name]["vibration"]]
                ),
    
            )
        
        #Create a Composite Alarm for cross validation
        composite_alarms = []
        for node_name in node_names:
            alarm_rule = cloudwatch.AlarmRule.all_of(
                    cloudwatch.AlarmRule.any_of(
                        alarms_by_node[node_name]["moisture"],
                        alarms_by_node[node_name]["temperature"],
                        alarms_by_node[node_name]["acoustic"],
                        alarms_by_node[node_name]["vibration"],
                    ),
                    alarms_by_node[node_name]["confidence_score"]
                
            )
            composite_alarm = cloudwatch.CompositeAlarm(self, f"LeakDetectionCompositeAlarm{node_name}",
                composite_alarm_name = f"LeakDetectionCompositeAlarm_{node_name}",
                alarm_rule = alarm_rule
            )
            composite_alarm.add_alarm_action(cw_actions.SnsAction(leak_alert_topic))
            composite_alarms.append(composite_alarm)

        #Add a widget to the dashboard for the composite alarms
        dashboard.add_widgets(
            cloudwatch.AlarmStatusWidget(
                title = "System Status",
                alarms = composite_alarms
            )
        )



from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    aws_iot as iot, 
    CfnParameter,
    aws_iam as iam,
    aws_sns as sns,
    aws_sns_subscriptions as sub,
    aws_cloudwatch as cloudwatch,
    aws_cloudwatch_actions as cw_actions
)
from constructs import Construct

class LeakDetectionPracticumStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       
       #Certificate Parameters
        cert_arn_node01 = CfnParameter(self, "CertArnNode01",
            description="Certificate ARN for node-01",
            type="String"
        )
        cert_arn_node02 = CfnParameter(self, "CertArnNode02",
            description="Certificate ARN for node-02",
            type="String"
        )

       #Create a DynamoDB table to store the data 
        dynamodb_table = dynamodb.Table(self, "LeakDetectionTable",
            partition_key=dynamodb.Attribute(name="device_id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="timestamp", type=dynamodb.AttributeType.NUMBER),
            billing_mode=dynamodb.BillingMode.ON_DEMAND,
        )

       #Create a 2 IoT Core devices to represent the esp32 and its' sensors
        iot.CfnThing(self, "Node01Thing", thing_name="node01")
        iot.CfnThing(self, "Node02Thing", thing_name="node02")
        
       #Create a policy that allows the nodes to send the data to the DynamoDB table through an IAM role and policy
        iot.CfnPolicy(self, "NodePolicy",
            policy_name="leak_detection_nodes_policy",
            policy_document={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "iot:Connect",
                        "Resource": [f"arn:aws:iot:{Stack.of(self).region}:{Stack.of(self).account}:client/node*"]
                    },
                    {
                        "Effect": "Allow",
                        "Action": "iot:Publish",
                        "Resource": [f"arn:aws:iot:{Stack.of(self).region}:{Stack.of(self).account}:topic/leaksensor/node-*/data"]
                    },
                    {
                        "Effect": "Allow",
                        "Action": "iot:Subscribe",
                        "Resource": [f"arn:aws:iot:{Stack.of(self).region}:{Stack.of(self).account}:topicfilter/leaksensor/node-*/data"]
                    },
                ]
            }
        )
       
       #Certificate Attachments
        iot.CfnThingPrincipalAttachment(self, "Node01ThingAttachment",
            thing_name="node01",
            principal=cert_arn_node01.value_as_string
        )

        iot.CfnThingPrincipalAttachment(self, "Node02ThingAttachment",
            thing_name="node02",
            principal=cert_arn_node02.value_as_string
        )

        iot.CfnPolicyAttachment(self, "Node01PolicyAttachment",
            policy_name="leak_detection_nodes_policy",
            principal=cert_arn_node01.value_as_string
        )
        
        iot.CfnPolicyAttachment(self, "Node02PolicyAttachment",
            policy_name="leak_detection_nodes_policy",
            principal=cert_arn_node02.value_as_string
        )
              
       #Give IAM Rule permission to write to DynamoDB
        Table_Write_Role = iam.Role(self, "WritePermission",
            assumed_by=iam.ServicePrincipal("iot.amazonaws.com")
        )

        Table_Write_Role.add_to_policy(iam.PolicyStatement(
            actions=["dynamodb:PutItem"],
            resources=[dynamodb_table.table_arn]
        ))

       #IoT Topic Rule
        iot.CfnTopicRule(self, "LeakDetectionTopicRule",
            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                sql="SELECT * FROM 'leaksensor/+/data'",
                actions=[
                    iot.CfnTopicRule.ActionProperty(
                        dynamo_db_v2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name=dynamodb_table.table_name,
                            ),
                            role_arn=Table_Write_Role.role_arn
                        )
                    )
                ]
            ))

       #Create an SNS topic to alert if the data falls out of a certain threshold
        Email_01 = CfnParameter(self, "AlertEmail",
            description="Email address for leak detection alerts",
            type="String"
        )
        
        leak_alert_topic = sns.Topic(self, "LeakAlertTopic",
            display_name="Leak Detection Alert"
        )

        leak_alert_topic.add_subscription(
            sub.EmailSubscription(Email_01.value_as_string)
        )
      
       #Configure Cloudwatch to monitor the data in the DynamoDB table
        
       #Create a Cloudwatch alarm to alert if data falls out of a certain threshold

       #Create a Cloudwatch dashboard to visualize the data in the DynamoDB table
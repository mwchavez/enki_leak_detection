import aws_cdk as core
import aws_cdk.assertions as assertions

from leak_detection_practicum.leak_detection_practicum_stack import LeakDetectionPracticumStack

# example tests. To run these tests, uncomment this file along with the example
# resource in leak_detection_practicum/leak_detection_practicum_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LeakDetectionPracticumStack(app, "leak-detection-practicum")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

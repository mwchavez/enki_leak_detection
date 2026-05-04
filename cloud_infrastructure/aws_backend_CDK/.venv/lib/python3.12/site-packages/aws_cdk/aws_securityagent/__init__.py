r'''
# AWS::SecurityAgent Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_securityagent as securityagent
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SecurityAgent construct libraries](https://constructs.dev/search?q=securityagent)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SecurityAgent resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityAgent.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SecurityAgent](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityAgent.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_securityagent import (
    AgentSpaceReference as _AgentSpaceReference_d9ee65f4,
    ApplicationReference as _ApplicationReference_658b5da3,
    IAgentSpaceRef as _IAgentSpaceRef_4cc4399b,
    IApplicationRef as _IApplicationRef_47d5c35f,
    IPentestRef as _IPentestRef_c0adf303,
    ITargetDomainRef as _ITargetDomainRef_af00a826,
    PentestReference as _PentestReference_9b2eeaff,
    TargetDomainReference as _TargetDomainReference_ceabb397,
)


@jsii.implements(_IInspectable_c2943556, _IAgentSpaceRef_4cc4399b, _ITaggableV2_4e6798f8)
class CfnAgentSpace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityagent.CfnAgentSpace",
):
    '''Resource Type definition for AWS::SecurityAgent::AgentSpace.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html
    :cloudformationResource: AWS::SecurityAgent::AgentSpace
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityagent as securityagent
        
        cfn_agent_space = securityagent.CfnAgentSpace(self, "MyCfnAgentSpace",
            name="name",
        
            # the properties below are optional
            aws_resources=securityagent.CfnAgentSpace.AWSResourcesProperty(
                iam_roles=["iamRoles"],
                lambda_function_arns=["lambdaFunctionArns"],
                log_groups=["logGroups"],
                s3_buckets=["s3Buckets"],
                secret_arns=["secretArns"],
                vpcs=[securityagent.CfnAgentSpace.VpcConfigProperty(
                    security_group_arns=["securityGroupArns"],
                    subnet_arns=["subnetArns"],
                    vpc_arn="vpcArn"
                )]
            ),
            code_review_settings=securityagent.CfnAgentSpace.CodeReviewSettingsProperty(
                controls_scanning=False,
                general_purpose_scanning=False
            ),
            description="description",
            integrated_resources=[securityagent.CfnAgentSpace.IntegratedResourceProperty(
                integration="integration"
            )],
            kms_key_id="kmsKeyId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_domain_ids=["targetDomainIds"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        aws_resources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.AWSResourcesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        code_review_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.CodeReviewSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        integrated_resources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.IntegratedResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        target_domain_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::SecurityAgent::AgentSpace``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the agent space.
        :param aws_resources: AWS resource configuration.
        :param code_review_settings: Details of code review settings.
        :param description: Description of the agent space.
        :param integrated_resources: Integrated Resources configuration.
        :param kms_key_id: Identifier of the KMS key used to encrypt data. Can be a key ID, key ARN, alias name, or alias ARN. If not specified, an AWS managed key is used.
        :param tags: Tags for the agent space.
        :param target_domain_ids: List of target domain identifiers registered with the agent space.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef24fb7e0398f97f2bf34bb92f534c54e23ad1b57db92995399f3969c878222)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAgentSpaceProps(
            name=name,
            aws_resources=aws_resources,
            code_review_settings=code_review_settings,
            description=description,
            integrated_resources=integrated_resources,
            kms_key_id=kms_key_id,
            tags=tags,
            target_domain_ids=target_domain_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnAgentSpace")
    @builtins.classmethod
    def is_cfn_agent_space(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAgentSpace.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab99b207630f0fdce3650e450353eb2b8300110d6b87f21dea92ec73dcd5bd9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAgentSpace", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6908f826f50bf019406c2b4d7515bd3f8bb60cc61e6c3620b45f9c2502c594a5)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92cfc4584067e1e03d34496841f2f33ceaa43ec305156ce5c5500c1cc3729005)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "_AgentSpaceReference_d9ee65f4":
        '''A reference to a AgentSpace resource.'''
        return typing.cast("_AgentSpaceReference_d9ee65f4", jsii.get(self, "agentSpaceRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentSpaceId")
    def attr_agent_space_id(self) -> builtins.str:
        '''Unique identifier of the agent space.

        :cloudformationAttribute: AgentSpaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentSpaceId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Timestamp when the agent space was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''Timestamp when the agent space was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the agent space.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b16a68b67bb21513bdb7f3be0b225a0e1abb9fee8fa6c5ee87a26614c4447ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="awsResources")
    def aws_resources(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.AWSResourcesProperty"]]:
        '''AWS resource configuration.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.AWSResourcesProperty"]], jsii.get(self, "awsResources"))

    @aws_resources.setter
    def aws_resources(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.AWSResourcesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a750a967e1fac12db17d49079d9c04596b2af1ef6de44df7761e599169a3c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsResources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="codeReviewSettings")
    def code_review_settings(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.CodeReviewSettingsProperty"]]:
        '''Details of code review settings.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.CodeReviewSettingsProperty"]], jsii.get(self, "codeReviewSettings"))

    @code_review_settings.setter
    def code_review_settings(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.CodeReviewSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a1b2700da399046746b605e7912029af38d6e20164cc75a19db6ec285c91ca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeReviewSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the agent space.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883a998f4fead4777b8e089453a192c17422395f96917106145a0ad3c43bff09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="integratedResources")
    def integrated_resources(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IntegratedResourceProperty"]]]]:
        '''Integrated Resources configuration.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IntegratedResourceProperty"]]]], jsii.get(self, "integratedResources"))

    @integrated_resources.setter
    def integrated_resources(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IntegratedResourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a703a49b3f1a81fcad7cfc4a340dee66e153cc8a77237f59ed1fd706bc41afca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integratedResources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the KMS key used to encrypt data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8158b14701610c6f2fd630d80073e48e59db833f9491078d3ed86b230e8b7ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags for the agent space.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__452bbe46d262236c7182002fa61ed5aa51c2c3cca7df3a25caa1cc6af3deeb86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetDomainIds")
    def target_domain_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of target domain identifiers registered with the agent space.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetDomainIds"))

    @target_domain_ids.setter
    def target_domain_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e34b178a1218f29101cd534305dd0a625fa59e5c5a3e6c1661a1d658a1aa6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDomainIds", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnAgentSpace.AWSResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_roles": "iamRoles",
            "lambda_function_arns": "lambdaFunctionArns",
            "log_groups": "logGroups",
            "s3_buckets": "s3Buckets",
            "secret_arns": "secretArns",
            "vpcs": "vpcs",
        },
    )
    class AWSResourcesProperty:
        def __init__(
            self,
            *,
            iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
            lambda_function_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            log_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            s3_buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
            secret_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpcs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''AWS resource configuration.

            :param iam_roles: IAM role ARNs.
            :param lambda_function_arns: Lambda function ARNs used to retrieve tester credentials for pentests.
            :param log_groups: CloudWatch log group ARNs.
            :param s3_buckets: S3 bucket ARNs.
            :param secret_arns: SecretsManager secret ARNs used to store tester credentials for pentests.
            :param vpcs: VPC configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                a_wSResources_property = securityagent.CfnAgentSpace.AWSResourcesProperty(
                    iam_roles=["iamRoles"],
                    lambda_function_arns=["lambdaFunctionArns"],
                    log_groups=["logGroups"],
                    s3_buckets=["s3Buckets"],
                    secret_arns=["secretArns"],
                    vpcs=[securityagent.CfnAgentSpace.VpcConfigProperty(
                        security_group_arns=["securityGroupArns"],
                        subnet_arns=["subnetArns"],
                        vpc_arn="vpcArn"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce3a1f09aa1793040964f17ba37ea2d39035a52835521a06a2fd2429331eba65)
                check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
                check_type(argname="argument lambda_function_arns", value=lambda_function_arns, expected_type=type_hints["lambda_function_arns"])
                check_type(argname="argument log_groups", value=log_groups, expected_type=type_hints["log_groups"])
                check_type(argname="argument s3_buckets", value=s3_buckets, expected_type=type_hints["s3_buckets"])
                check_type(argname="argument secret_arns", value=secret_arns, expected_type=type_hints["secret_arns"])
                check_type(argname="argument vpcs", value=vpcs, expected_type=type_hints["vpcs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam_roles is not None:
                self._values["iam_roles"] = iam_roles
            if lambda_function_arns is not None:
                self._values["lambda_function_arns"] = lambda_function_arns
            if log_groups is not None:
                self._values["log_groups"] = log_groups
            if s3_buckets is not None:
                self._values["s3_buckets"] = s3_buckets
            if secret_arns is not None:
                self._values["secret_arns"] = secret_arns
            if vpcs is not None:
                self._values["vpcs"] = vpcs

        @builtins.property
        def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
            '''IAM role ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html#cfn-securityagent-agentspace-awsresources-iamroles
            '''
            result = self._values.get("iam_roles")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def lambda_function_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Lambda function ARNs used to retrieve tester credentials for pentests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html#cfn-securityagent-agentspace-awsresources-lambdafunctionarns
            '''
            result = self._values.get("lambda_function_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def log_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''CloudWatch log group ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html#cfn-securityagent-agentspace-awsresources-loggroups
            '''
            result = self._values.get("log_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def s3_buckets(self) -> typing.Optional[typing.List[builtins.str]]:
            '''S3 bucket ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html#cfn-securityagent-agentspace-awsresources-s3buckets
            '''
            result = self._values.get("s3_buckets")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def secret_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''SecretsManager secret ARNs used to store tester credentials for pentests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html#cfn-securityagent-agentspace-awsresources-secretarns
            '''
            result = self._values.get("secret_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpcs(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.VpcConfigProperty"]]]]:
            '''VPC configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-awsresources.html#cfn-securityagent-agentspace-awsresources-vpcs
            '''
            result = self._values.get("vpcs")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.VpcConfigProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnAgentSpace.CodeReviewSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "controls_scanning": "controlsScanning",
            "general_purpose_scanning": "generalPurposeScanning",
        },
    )
    class CodeReviewSettingsProperty:
        def __init__(
            self,
            *,
            controls_scanning: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
            general_purpose_scanning: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
        ) -> None:
            '''Details of code review settings.

            :param controls_scanning: Whether Controls are utilized for code review analysis.
            :param general_purpose_scanning: Whether general purpose analysis is performed for code review.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-codereviewsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                code_review_settings_property = securityagent.CfnAgentSpace.CodeReviewSettingsProperty(
                    controls_scanning=False,
                    general_purpose_scanning=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47533237cc30a0b4e6af78a36be81461d974345e71b59894210932a057ff4753)
                check_type(argname="argument controls_scanning", value=controls_scanning, expected_type=type_hints["controls_scanning"])
                check_type(argname="argument general_purpose_scanning", value=general_purpose_scanning, expected_type=type_hints["general_purpose_scanning"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "controls_scanning": controls_scanning,
                "general_purpose_scanning": general_purpose_scanning,
            }

        @builtins.property
        def controls_scanning(
            self,
        ) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''Whether Controls are utilized for code review analysis.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-codereviewsettings.html#cfn-securityagent-agentspace-codereviewsettings-controlsscanning
            '''
            result = self._values.get("controls_scanning")
            assert result is not None, "Required property 'controls_scanning' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        @builtins.property
        def general_purpose_scanning(
            self,
        ) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''Whether general purpose analysis is performed for code review.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-codereviewsettings.html#cfn-securityagent-agentspace-codereviewsettings-generalpurposescanning
            '''
            result = self._values.get("general_purpose_scanning")
            assert result is not None, "Required property 'general_purpose_scanning' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeReviewSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnAgentSpace.IntegratedResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"integration": "integration"},
    )
    class IntegratedResourceProperty:
        def __init__(self, *, integration: builtins.str) -> None:
            '''Integrated Resource details.

            :param integration: Unique identifier of the Provider Integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-integratedresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                integrated_resource_property = securityagent.CfnAgentSpace.IntegratedResourceProperty(
                    integration="integration"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fba15574f3d88d87ae613250d24376367fc26356706c91ce38869879d225d774)
                check_type(argname="argument integration", value=integration, expected_type=type_hints["integration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "integration": integration,
            }

        @builtins.property
        def integration(self) -> builtins.str:
            '''Unique identifier of the Provider Integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-integratedresource.html#cfn-securityagent-agentspace-integratedresource-integration
            '''
            result = self._values.get("integration")
            assert result is not None, "Required property 'integration' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegratedResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnAgentSpace.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_arns": "securityGroupArns",
            "subnet_arns": "subnetArns",
            "vpc_arn": "vpcArn",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Customer VPC configuration that the security testing environment accesses.

            :param security_group_arns: List of security group ARNs in the customer VPC.
            :param subnet_arns: List of subnet ARNs in the customer VPC.
            :param vpc_arn: ARN of the customer VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                vpc_config_property = securityagent.CfnAgentSpace.VpcConfigProperty(
                    security_group_arns=["securityGroupArns"],
                    subnet_arns=["subnetArns"],
                    vpc_arn="vpcArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e55cde8190d06b2c2ee5d0fc0c59ee2598deb376092113b341960302ca22f3fa)
                check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
                check_type(argname="argument subnet_arns", value=subnet_arns, expected_type=type_hints["subnet_arns"])
                check_type(argname="argument vpc_arn", value=vpc_arn, expected_type=type_hints["vpc_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_arns is not None:
                self._values["security_group_arns"] = security_group_arns
            if subnet_arns is not None:
                self._values["subnet_arns"] = subnet_arns
            if vpc_arn is not None:
                self._values["vpc_arn"] = vpc_arn

        @builtins.property
        def security_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of security group ARNs in the customer VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-vpcconfig.html#cfn-securityagent-agentspace-vpcconfig-securitygrouparns
            '''
            result = self._values.get("security_group_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of subnet ARNs in the customer VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-vpcconfig.html#cfn-securityagent-agentspace-vpcconfig-subnetarns
            '''
            result = self._values.get("subnet_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_arn(self) -> typing.Optional[builtins.str]:
            '''ARN of the customer VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-agentspace-vpcconfig.html#cfn-securityagent-agentspace-vpcconfig-vpcarn
            '''
            result = self._values.get("vpc_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityagent.CfnAgentSpaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "aws_resources": "awsResources",
        "code_review_settings": "codeReviewSettings",
        "description": "description",
        "integrated_resources": "integratedResources",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
        "target_domain_ids": "targetDomainIds",
    },
)
class CfnAgentSpaceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        aws_resources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.AWSResourcesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        code_review_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.CodeReviewSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        integrated_resources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.IntegratedResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        target_domain_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAgentSpace``.

        :param name: Name of the agent space.
        :param aws_resources: AWS resource configuration.
        :param code_review_settings: Details of code review settings.
        :param description: Description of the agent space.
        :param integrated_resources: Integrated Resources configuration.
        :param kms_key_id: Identifier of the KMS key used to encrypt data. Can be a key ID, key ARN, alias name, or alias ARN. If not specified, an AWS managed key is used.
        :param tags: Tags for the agent space.
        :param target_domain_ids: List of target domain identifiers registered with the agent space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityagent as securityagent
            
            cfn_agent_space_props = securityagent.CfnAgentSpaceProps(
                name="name",
            
                # the properties below are optional
                aws_resources=securityagent.CfnAgentSpace.AWSResourcesProperty(
                    iam_roles=["iamRoles"],
                    lambda_function_arns=["lambdaFunctionArns"],
                    log_groups=["logGroups"],
                    s3_buckets=["s3Buckets"],
                    secret_arns=["secretArns"],
                    vpcs=[securityagent.CfnAgentSpace.VpcConfigProperty(
                        security_group_arns=["securityGroupArns"],
                        subnet_arns=["subnetArns"],
                        vpc_arn="vpcArn"
                    )]
                ),
                code_review_settings=securityagent.CfnAgentSpace.CodeReviewSettingsProperty(
                    controls_scanning=False,
                    general_purpose_scanning=False
                ),
                description="description",
                integrated_resources=[securityagent.CfnAgentSpace.IntegratedResourceProperty(
                    integration="integration"
                )],
                kms_key_id="kmsKeyId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_domain_ids=["targetDomainIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63fcebc9f38c568223136c35c5b8bf056aaf1d2658a8795d9f9fac31e9b9d41)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_resources", value=aws_resources, expected_type=type_hints["aws_resources"])
            check_type(argname="argument code_review_settings", value=code_review_settings, expected_type=type_hints["code_review_settings"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument integrated_resources", value=integrated_resources, expected_type=type_hints["integrated_resources"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_domain_ids", value=target_domain_ids, expected_type=type_hints["target_domain_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if aws_resources is not None:
            self._values["aws_resources"] = aws_resources
        if code_review_settings is not None:
            self._values["code_review_settings"] = code_review_settings
        if description is not None:
            self._values["description"] = description
        if integrated_resources is not None:
            self._values["integrated_resources"] = integrated_resources
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags
        if target_domain_ids is not None:
            self._values["target_domain_ids"] = target_domain_ids

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the agent space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_resources(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.AWSResourcesProperty"]]:
        '''AWS resource configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-awsresources
        '''
        result = self._values.get("aws_resources")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.AWSResourcesProperty"]], result)

    @builtins.property
    def code_review_settings(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.CodeReviewSettingsProperty"]]:
        '''Details of code review settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-codereviewsettings
        '''
        result = self._values.get("code_review_settings")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.CodeReviewSettingsProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the agent space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integrated_resources(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IntegratedResourceProperty"]]]]:
        '''Integrated Resources configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-integratedresources
        '''
        result = self._values.get("integrated_resources")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IntegratedResourceProperty"]]]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the KMS key used to encrypt data.

        Can be a key ID, key ARN, alias name, or alias ARN. If not specified, an AWS managed key is used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags for the agent space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def target_domain_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of target domain identifiers registered with the agent space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-agentspace.html#cfn-securityagent-agentspace-targetdomainids
        '''
        result = self._values.get("target_domain_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAgentSpaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IApplicationRef_47d5c35f, _ITaggableV2_4e6798f8)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityagent.CfnApplication",
):
    '''Resource Type definition for AWS::SecurityAgent::Application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-application.html
    :cloudformationResource: AWS::SecurityAgent::Application
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityagent as securityagent
        
        cfn_application = securityagent.CfnApplication(self, "MyCfnApplication",
            default_kms_key_id="defaultKmsKeyId",
            id_cConfiguration=securityagent.CfnApplication.IdCConfigurationProperty(
                id_cApplication_arn="idCApplicationArn",
                id_cInstance_arn="idCInstanceArn"
            ),
            role_arn="roleArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        default_kms_key_id: typing.Optional[builtins.str] = None,
        id_c_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.IdCConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SecurityAgent::Application``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_kms_key_id: Identifier of a KMS key. Can be a key ID, key ARN, alias name, or alias ARN.
        :param id_c_configuration: 
        :param role_arn: 
        :param tags: Tags for the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__578e51536b17e4aa32471e1d1fd3cd36d0e5c7e116bd3ca5ec01a9f0375c8eaf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            default_kms_key_id=default_kms_key_id,
            id_c_configuration=id_c_configuration,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForApplication")
    @builtins.classmethod
    def arn_for_application(cls, resource: "_IApplicationRef_47d5c35f") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c433d5a147ba3da470a74a02ec6dd989c1b96e915ea645eaef3e76561553d75)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForApplication", [resource]))

    @jsii.member(jsii_name="fromApplicationId")
    @builtins.classmethod
    def from_application_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        application_id: builtins.str,
    ) -> "_IApplicationRef_47d5c35f":
        '''Creates a new IApplicationRef from a applicationId.

        :param scope: -
        :param id: -
        :param application_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f2c6116a3f36a4ce344c2f9db127c9051bfb6434e801671ada9ac6759c6b2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        return typing.cast("_IApplicationRef_47d5c35f", jsii.sinvoke(cls, "fromApplicationId", [scope, id, application_id]))

    @jsii.member(jsii_name="isCfnApplication")
    @builtins.classmethod
    def is_cfn_application(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnApplication.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a09967466853d14feb121c24215733fe03c1d1391f8665057e98ba520571424)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnApplication", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04cffc3747cf67ceaff2b6e916311d776ba0b34d476bedfb51c1525d5eb61aad)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c36892ec084e2095c0e7432c2d16c26897ae9f27f7fd82501dc58469a11a032)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "_ApplicationReference_658b5da3":
        '''A reference to a Application resource.'''
        return typing.cast("_ApplicationReference_658b5da3", jsii.get(self, "applicationRef"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationName")
    def attr_application_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ApplicationName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationName"))

    @builtins.property
    @jsii.member(jsii_name="attrDomain")
    def attr_domain(self) -> builtins.str:
        '''
        :cloudformationAttribute: Domain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomain"))

    @builtins.property
    @jsii.member(jsii_name="attrIdCConfigurationIdCApplicationArn")
    def attr_id_c_configuration_id_c_application_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdCConfiguration.IdCApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdCConfigurationIdCApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="defaultKmsKeyId")
    def default_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of a KMS key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultKmsKeyId"))

    @default_kms_key_id.setter
    def default_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1b23f95eb73ca8d49ebfe6e25d6191771b19653585d80e49067d6c9d2eaebf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultKmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="idCConfiguration")
    def id_c_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IdCConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IdCConfigurationProperty"]], jsii.get(self, "idCConfiguration"))

    @id_c_configuration.setter
    def id_c_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IdCConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ecbd010873e2be9992a4b7544fb8d13bbefabe8ec47426007067d9833779d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idCConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc2feb71ef581c3b5a294d96c8d2c5b3409f62c2bbf7ed680d87fc10fbb73dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags for the application.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e425ca9094c48d21d490f93d36a1ee1223c9a17938db33636007495504db25f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnApplication.IdCConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id_c_application_arn": "idCApplicationArn",
            "id_c_instance_arn": "idCInstanceArn",
        },
    )
    class IdCConfigurationProperty:
        def __init__(
            self,
            *,
            id_c_application_arn: typing.Optional[builtins.str] = None,
            id_c_instance_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param id_c_application_arn: 
            :param id_c_instance_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-application-idcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                id_cConfiguration_property = securityagent.CfnApplication.IdCConfigurationProperty(
                    id_cApplication_arn="idCApplicationArn",
                    id_cInstance_arn="idCInstanceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e26c4b578f401e1801e9bee4038a5ded65c9be7b3ddd0a76f89eb025cc9eefc)
                check_type(argname="argument id_c_application_arn", value=id_c_application_arn, expected_type=type_hints["id_c_application_arn"])
                check_type(argname="argument id_c_instance_arn", value=id_c_instance_arn, expected_type=type_hints["id_c_instance_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id_c_application_arn is not None:
                self._values["id_c_application_arn"] = id_c_application_arn
            if id_c_instance_arn is not None:
                self._values["id_c_instance_arn"] = id_c_instance_arn

        @builtins.property
        def id_c_application_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-application-idcconfiguration.html#cfn-securityagent-application-idcconfiguration-idcapplicationarn
            '''
            result = self._values.get("id_c_application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id_c_instance_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-application-idcconfiguration.html#cfn-securityagent-application-idcconfiguration-idcinstancearn
            '''
            result = self._values.get("id_c_instance_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdCConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityagent.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_kms_key_id": "defaultKmsKeyId",
        "id_c_configuration": "idCConfiguration",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        default_kms_key_id: typing.Optional[builtins.str] = None,
        id_c_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.IdCConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param default_kms_key_id: Identifier of a KMS key. Can be a key ID, key ARN, alias name, or alias ARN.
        :param id_c_configuration: 
        :param role_arn: 
        :param tags: Tags for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-application.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityagent as securityagent
            
            cfn_application_props = securityagent.CfnApplicationProps(
                default_kms_key_id="defaultKmsKeyId",
                id_cConfiguration=securityagent.CfnApplication.IdCConfigurationProperty(
                    id_cApplication_arn="idCApplicationArn",
                    id_cInstance_arn="idCInstanceArn"
                ),
                role_arn="roleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b36d9297d6d873ed09ead98b35106a55f3a507c8ce2351f00ffb25948761dfd)
            check_type(argname="argument default_kms_key_id", value=default_kms_key_id, expected_type=type_hints["default_kms_key_id"])
            check_type(argname="argument id_c_configuration", value=id_c_configuration, expected_type=type_hints["id_c_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_kms_key_id is not None:
            self._values["default_kms_key_id"] = default_kms_key_id
        if id_c_configuration is not None:
            self._values["id_c_configuration"] = id_c_configuration
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifier of a KMS key.

        Can be a key ID, key ARN, alias name, or alias ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-application.html#cfn-securityagent-application-defaultkmskeyid
        '''
        result = self._values.get("default_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id_c_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IdCConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-application.html#cfn-securityagent-application-idcconfiguration
        '''
        result = self._values.get("id_c_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IdCConfigurationProperty"]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-application.html#cfn-securityagent-application-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags for the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-application.html#cfn-securityagent-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IPentestRef_c0adf303)
class CfnPentest(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest",
):
    '''Resource Type definition for AWS::SecurityAgent::Pentest.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html
    :cloudformationResource: AWS::SecurityAgent::Pentest
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityagent as securityagent
        
        cfn_pentest = securityagent.CfnPentest(self, "MyCfnPentest",
            agent_space_id="agentSpaceId",
            assets=securityagent.CfnPentest.AssetsProperty(
                actors=[securityagent.CfnPentest.ActorProperty(
                    authentication=securityagent.CfnPentest.AuthenticationProperty(
                        provider_type="providerType",
                        value="value"
                    ),
                    description="description",
                    identifier="identifier",
                    uris=["uris"]
                )],
                documents=[securityagent.CfnPentest.DocumentInfoProperty(
                    artifact_id="artifactId",
                    s3_location="s3Location"
                )],
                endpoints=[securityagent.CfnPentest.EndpointProperty(
                    uri="uri"
                )],
                integrated_repositories=[securityagent.CfnPentest.IntegratedRepositoryProperty(
                    integration_id="integrationId",
                    provider_resource_id="providerResourceId"
                )],
                source_code=[securityagent.CfnPentest.SourceCodeRepositoryProperty(
                    s3_location="s3Location"
                )]
            ),
            service_role="serviceRole",
        
            # the properties below are optional
            code_remediation_strategy="codeRemediationStrategy",
            exclude_risk_types=["excludeRiskTypes"],
            log_config=securityagent.CfnPentest.CloudWatchLogProperty(
                log_group="logGroup",
                log_stream="logStream"
            ),
            network_traffic_config=securityagent.CfnPentest.NetworkTrafficConfigProperty(
                custom_headers=[securityagent.CfnPentest.CustomHeaderProperty(
                    name="name",
                    value="value"
                )],
                rules=[securityagent.CfnPentest.NetworkTrafficRuleProperty(
                    effect="effect",
                    network_traffic_rule_type="networkTrafficRuleType",
                    pattern="pattern"
                )]
            ),
            title="title",
            vpc_config=securityagent.CfnPentest.VpcConfigProperty(
                security_group_arns=["securityGroupArns"],
                subnet_arns=["subnetArns"],
                vpc_arn="vpcArn"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        agent_space_id: builtins.str,
        assets: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.AssetsProperty", typing.Dict[builtins.str, typing.Any]]],
        service_role: builtins.str,
        code_remediation_strategy: typing.Optional[builtins.str] = None,
        exclude_risk_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.CloudWatchLogProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        network_traffic_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.NetworkTrafficConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        title: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SecurityAgent::Pentest``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_space_id: 
        :param assets: 
        :param service_role: 
        :param code_remediation_strategy: 
        :param exclude_risk_types: 
        :param log_config: 
        :param network_traffic_config: 
        :param title: 
        :param vpc_config: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d83c0f79102402315ab2667cd779997a2fd84704dc25119af31f0018a831848)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPentestProps(
            agent_space_id=agent_space_id,
            assets=assets,
            service_role=service_role,
            code_remediation_strategy=code_remediation_strategy,
            exclude_risk_types=exclude_risk_types,
            log_config=log_config,
            network_traffic_config=network_traffic_config,
            title=title,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnPentest")
    @builtins.classmethod
    def is_cfn_pentest(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPentest.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c91cc55571ff5885f1a1d0b1933fbe225557b1f86c95d8ba38bc33fe4c61e84a)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPentest", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caa7bfb9f39891718a13a4e778189ad97817330895f8e15bef30dfe07550ac51)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0a2f1484080dcc24c0effa2a509767dbea4fad3028a7ab44a871ebb67120b1e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPentestId")
    def attr_pentest_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PentestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPentestId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="pentestRef")
    def pentest_ref(self) -> "_PentestReference_9b2eeaff":
        '''A reference to a Pentest resource.'''
        return typing.cast("_PentestReference_9b2eeaff", jsii.get(self, "pentestRef"))

    @builtins.property
    @jsii.member(jsii_name="agentSpaceId")
    def agent_space_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentSpaceId"))

    @agent_space_id.setter
    def agent_space_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a6d1b2d87fc882cf2734deb7858624f1dcc00e7c63002525d1a9fa7cd3d6e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentSpaceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assets")
    def assets(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPentest.AssetsProperty"]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPentest.AssetsProperty"], jsii.get(self, "assets"))

    @assets.setter
    def assets(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnPentest.AssetsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12345bae4c066f259b044fe64398908ebbbf527bb6d6854d69571a436a5aa6c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae21e38e0529ed7148f6ea4283dba1ed6d7f4d6eab2c535834d2aebb4788a140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="codeRemediationStrategy")
    def code_remediation_strategy(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeRemediationStrategy"))

    @code_remediation_strategy.setter
    def code_remediation_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f11a8b62790439898a591432715582d38bc20ececc324a951cdb947a80581ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeRemediationStrategy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="excludeRiskTypes")
    def exclude_risk_types(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeRiskTypes"))

    @exclude_risk_types.setter
    def exclude_risk_types(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0e3c6ff9fc0223ce453b38a2e22fc60a5081555fd3eb0f71c75468863a92b75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeRiskTypes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.CloudWatchLogProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.CloudWatchLogProperty"]], jsii.get(self, "logConfig"))

    @log_config.setter
    def log_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.CloudWatchLogProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3c320e1d6daf33457b394bd52277ab4d04be687b9915b95f0d348f241f7b38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkTrafficConfig")
    def network_traffic_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficConfigProperty"]], jsii.get(self, "networkTrafficConfig"))

    @network_traffic_config.setter
    def network_traffic_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d4fb3fd1f4f28dd91245a6e6a1cbd6d3f9175fdb58d771301ab68da826171b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkTrafficConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "title"))

    @title.setter
    def title(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dbf45fab9e1a4ebffd4a194d8dabfcc48049da8b74581218b16440ec3b6841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.VpcConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c52839de7f5fb0b1842f597d1d019725896583f4fbfaa741b87eaa453825436)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.ActorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication": "authentication",
            "description": "description",
            "identifier": "identifier",
            "uris": "uris",
        },
    )
    class ActorProperty:
        def __init__(
            self,
            *,
            authentication: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.AuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            description: typing.Optional[builtins.str] = None,
            identifier: typing.Optional[builtins.str] = None,
            uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param authentication: 
            :param description: 
            :param identifier: 
            :param uris: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-actor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                actor_property = securityagent.CfnPentest.ActorProperty(
                    authentication=securityagent.CfnPentest.AuthenticationProperty(
                        provider_type="providerType",
                        value="value"
                    ),
                    description="description",
                    identifier="identifier",
                    uris=["uris"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__789552d2a299b54f21a25572baa25b7b652499c9578bcdf16e84796ef97b2678)
                check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
                check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authentication is not None:
                self._values["authentication"] = authentication
            if description is not None:
                self._values["description"] = description
            if identifier is not None:
                self._values["identifier"] = identifier
            if uris is not None:
                self._values["uris"] = uris

        @builtins.property
        def authentication(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.AuthenticationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-actor.html#cfn-securityagent-pentest-actor-authentication
            '''
            result = self._values.get("authentication")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.AuthenticationProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-actor.html#cfn-securityagent-pentest-actor-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def identifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-actor.html#cfn-securityagent-pentest-actor-identifier
            '''
            result = self._values.get("identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uris(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-actor.html#cfn-securityagent-pentest-actor-uris
            '''
            result = self._values.get("uris")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.AssetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actors": "actors",
            "documents": "documents",
            "endpoints": "endpoints",
            "integrated_repositories": "integratedRepositories",
            "source_code": "sourceCode",
        },
    )
    class AssetsProperty:
        def __init__(
            self,
            *,
            actors: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.ActorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            documents: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.DocumentInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            endpoints: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            integrated_repositories: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.IntegratedRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_code: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.SourceCodeRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param actors: 
            :param documents: 
            :param endpoints: 
            :param integrated_repositories: 
            :param source_code: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-assets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                assets_property = securityagent.CfnPentest.AssetsProperty(
                    actors=[securityagent.CfnPentest.ActorProperty(
                        authentication=securityagent.CfnPentest.AuthenticationProperty(
                            provider_type="providerType",
                            value="value"
                        ),
                        description="description",
                        identifier="identifier",
                        uris=["uris"]
                    )],
                    documents=[securityagent.CfnPentest.DocumentInfoProperty(
                        artifact_id="artifactId",
                        s3_location="s3Location"
                    )],
                    endpoints=[securityagent.CfnPentest.EndpointProperty(
                        uri="uri"
                    )],
                    integrated_repositories=[securityagent.CfnPentest.IntegratedRepositoryProperty(
                        integration_id="integrationId",
                        provider_resource_id="providerResourceId"
                    )],
                    source_code=[securityagent.CfnPentest.SourceCodeRepositoryProperty(
                        s3_location="s3Location"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__90ac541f4598ca1ed36733bf9d5a278158f6b2a40ecc4723d2aa1ebff5ec5fa5)
                check_type(argname="argument actors", value=actors, expected_type=type_hints["actors"])
                check_type(argname="argument documents", value=documents, expected_type=type_hints["documents"])
                check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
                check_type(argname="argument integrated_repositories", value=integrated_repositories, expected_type=type_hints["integrated_repositories"])
                check_type(argname="argument source_code", value=source_code, expected_type=type_hints["source_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if actors is not None:
                self._values["actors"] = actors
            if documents is not None:
                self._values["documents"] = documents
            if endpoints is not None:
                self._values["endpoints"] = endpoints
            if integrated_repositories is not None:
                self._values["integrated_repositories"] = integrated_repositories
            if source_code is not None:
                self._values["source_code"] = source_code

        @builtins.property
        def actors(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.ActorProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-assets.html#cfn-securityagent-pentest-assets-actors
            '''
            result = self._values.get("actors")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.ActorProperty"]]]], result)

        @builtins.property
        def documents(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.DocumentInfoProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-assets.html#cfn-securityagent-pentest-assets-documents
            '''
            result = self._values.get("documents")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.DocumentInfoProperty"]]]], result)

        @builtins.property
        def endpoints(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.EndpointProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-assets.html#cfn-securityagent-pentest-assets-endpoints
            '''
            result = self._values.get("endpoints")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.EndpointProperty"]]]], result)

        @builtins.property
        def integrated_repositories(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.IntegratedRepositoryProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-assets.html#cfn-securityagent-pentest-assets-integratedrepositories
            '''
            result = self._values.get("integrated_repositories")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.IntegratedRepositoryProperty"]]]], result)

        @builtins.property
        def source_code(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.SourceCodeRepositoryProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-assets.html#cfn-securityagent-pentest-assets-sourcecode
            '''
            result = self._values.get("source_code")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.SourceCodeRepositoryProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.AuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"provider_type": "providerType", "value": "value"},
    )
    class AuthenticationProperty:
        def __init__(
            self,
            *,
            provider_type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param provider_type: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-authentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                authentication_property = securityagent.CfnPentest.AuthenticationProperty(
                    provider_type="providerType",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3532134765f42b5beced42cd2054d3ee1cba754ed2a8662007413abe8b3a7ed7)
                check_type(argname="argument provider_type", value=provider_type, expected_type=type_hints["provider_type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if provider_type is not None:
                self._values["provider_type"] = provider_type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def provider_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-authentication.html#cfn-securityagent-pentest-authentication-providertype
            '''
            result = self._values.get("provider_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-authentication.html#cfn-securityagent-pentest-authentication-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.CloudWatchLogProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup", "log_stream": "logStream"},
    )
    class CloudWatchLogProperty:
        def __init__(
            self,
            *,
            log_group: typing.Optional[builtins.str] = None,
            log_stream: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group: 
            :param log_stream: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-cloudwatchlog.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                cloud_watch_log_property = securityagent.CfnPentest.CloudWatchLogProperty(
                    log_group="logGroup",
                    log_stream="logStream"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0010faccc2dea59f0a9b2019a1a5ccfb658f48bd657c0f07a7ecda42c683cbd)
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
                check_type(argname="argument log_stream", value=log_stream, expected_type=type_hints["log_stream"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group is not None:
                self._values["log_group"] = log_group
            if log_stream is not None:
                self._values["log_stream"] = log_stream

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-cloudwatchlog.html#cfn-securityagent-pentest-cloudwatchlog-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_stream(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-cloudwatchlog.html#cfn-securityagent-pentest-cloudwatchlog-logstream
            '''
            result = self._values.get("log_stream")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.CustomHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class CustomHeaderProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-customheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                custom_header_property = securityagent.CfnPentest.CustomHeaderProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ff7bb011d1dc68f7f5b77ec0006ed8c2c4d7fc669ef653d7e4901b2d069e6a6)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-customheader.html#cfn-securityagent-pentest-customheader-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-customheader.html#cfn-securityagent-pentest-customheader-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.DocumentInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"artifact_id": "artifactId", "s3_location": "s3Location"},
    )
    class DocumentInfoProperty:
        def __init__(
            self,
            *,
            artifact_id: typing.Optional[builtins.str] = None,
            s3_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param artifact_id: 
            :param s3_location: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-documentinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                document_info_property = securityagent.CfnPentest.DocumentInfoProperty(
                    artifact_id="artifactId",
                    s3_location="s3Location"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4656bb528684e0993c3460489d2969558cf2587fa69964451204d94d714a217f)
                check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if artifact_id is not None:
                self._values["artifact_id"] = artifact_id
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def artifact_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-documentinfo.html#cfn-securityagent-pentest-documentinfo-artifactid
            '''
            result = self._values.get("artifact_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_location(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-documentinfo.html#cfn-securityagent-pentest-documentinfo-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={"uri": "uri"},
    )
    class EndpointProperty:
        def __init__(self, *, uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param uri: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                endpoint_property = securityagent.CfnPentest.EndpointProperty(
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__562d8396754a9f08650638a9ecc518a12e0b18c5256fc88afb318a18e3ffb029)
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if uri is not None:
                self._values["uri"] = uri

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-endpoint.html#cfn-securityagent-pentest-endpoint-uri
            '''
            result = self._values.get("uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.IntegratedRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "integration_id": "integrationId",
            "provider_resource_id": "providerResourceId",
        },
    )
    class IntegratedRepositoryProperty:
        def __init__(
            self,
            *,
            integration_id: builtins.str,
            provider_resource_id: builtins.str,
        ) -> None:
            '''
            :param integration_id: 
            :param provider_resource_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-integratedrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                integrated_repository_property = securityagent.CfnPentest.IntegratedRepositoryProperty(
                    integration_id="integrationId",
                    provider_resource_id="providerResourceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68c1c48352289031e291e4b2d1c94656660c67be9e64899490c98b8ea5799b99)
                check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
                check_type(argname="argument provider_resource_id", value=provider_resource_id, expected_type=type_hints["provider_resource_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "integration_id": integration_id,
                "provider_resource_id": provider_resource_id,
            }

        @builtins.property
        def integration_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-integratedrepository.html#cfn-securityagent-pentest-integratedrepository-integrationid
            '''
            result = self._values.get("integration_id")
            assert result is not None, "Required property 'integration_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def provider_resource_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-integratedrepository.html#cfn-securityagent-pentest-integratedrepository-providerresourceid
            '''
            result = self._values.get("provider_resource_id")
            assert result is not None, "Required property 'provider_resource_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegratedRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.NetworkTrafficConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_headers": "customHeaders", "rules": "rules"},
    )
    class NetworkTrafficConfigProperty:
        def __init__(
            self,
            *,
            custom_headers: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.CustomHeaderProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            rules: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.NetworkTrafficRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param custom_headers: 
            :param rules: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                network_traffic_config_property = securityagent.CfnPentest.NetworkTrafficConfigProperty(
                    custom_headers=[securityagent.CfnPentest.CustomHeaderProperty(
                        name="name",
                        value="value"
                    )],
                    rules=[securityagent.CfnPentest.NetworkTrafficRuleProperty(
                        effect="effect",
                        network_traffic_rule_type="networkTrafficRuleType",
                        pattern="pattern"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a46b4c00871d10d581e0a437b2abc4ca1f9ec70f49f35b5756a2f6c310f63645)
                check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_headers is not None:
                self._values["custom_headers"] = custom_headers
            if rules is not None:
                self._values["rules"] = rules

        @builtins.property
        def custom_headers(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.CustomHeaderProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficconfig.html#cfn-securityagent-pentest-networktrafficconfig-customheaders
            '''
            result = self._values.get("custom_headers")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.CustomHeaderProperty"]]]], result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficRuleProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficconfig.html#cfn-securityagent-pentest-networktrafficconfig-rules
            '''
            result = self._values.get("rules")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficRuleProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkTrafficConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.NetworkTrafficRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "effect": "effect",
            "network_traffic_rule_type": "networkTrafficRuleType",
            "pattern": "pattern",
        },
    )
    class NetworkTrafficRuleProperty:
        def __init__(
            self,
            *,
            effect: typing.Optional[builtins.str] = None,
            network_traffic_rule_type: typing.Optional[builtins.str] = None,
            pattern: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param effect: 
            :param network_traffic_rule_type: 
            :param pattern: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                network_traffic_rule_property = securityagent.CfnPentest.NetworkTrafficRuleProperty(
                    effect="effect",
                    network_traffic_rule_type="networkTrafficRuleType",
                    pattern="pattern"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__346479bc3d7bb9e27fe6c61adba2e4e5fca86ff3607b3c398cef04141179a54d)
                check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
                check_type(argname="argument network_traffic_rule_type", value=network_traffic_rule_type, expected_type=type_hints["network_traffic_rule_type"])
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if effect is not None:
                self._values["effect"] = effect
            if network_traffic_rule_type is not None:
                self._values["network_traffic_rule_type"] = network_traffic_rule_type
            if pattern is not None:
                self._values["pattern"] = pattern

        @builtins.property
        def effect(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficrule.html#cfn-securityagent-pentest-networktrafficrule-effect
            '''
            result = self._values.get("effect")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_traffic_rule_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficrule.html#cfn-securityagent-pentest-networktrafficrule-networktrafficruletype
            '''
            result = self._values.get("network_traffic_rule_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pattern(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-networktrafficrule.html#cfn-securityagent-pentest-networktrafficrule-pattern
            '''
            result = self._values.get("pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkTrafficRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.SourceCodeRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_location": "s3Location"},
    )
    class SourceCodeRepositoryProperty:
        def __init__(
            self,
            *,
            s3_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param s3_location: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-sourcecoderepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                source_code_repository_property = securityagent.CfnPentest.SourceCodeRepositoryProperty(
                    s3_location="s3Location"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac9ae05bfdd52d767951d638cfa69e9ccda258b973752d2d20a628d9a31eaa37)
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def s3_location(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-sourcecoderepository.html#cfn-securityagent-pentest-sourcecoderepository-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceCodeRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnPentest.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_arns": "securityGroupArns",
            "subnet_arns": "subnetArns",
            "vpc_arn": "vpcArn",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param security_group_arns: 
            :param subnet_arns: 
            :param vpc_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                vpc_config_property = securityagent.CfnPentest.VpcConfigProperty(
                    security_group_arns=["securityGroupArns"],
                    subnet_arns=["subnetArns"],
                    vpc_arn="vpcArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d61eb619b94085829ddd0e1e01d9220a86b2f2a7d6cf90af8a7ef5406580f8da)
                check_type(argname="argument security_group_arns", value=security_group_arns, expected_type=type_hints["security_group_arns"])
                check_type(argname="argument subnet_arns", value=subnet_arns, expected_type=type_hints["subnet_arns"])
                check_type(argname="argument vpc_arn", value=vpc_arn, expected_type=type_hints["vpc_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_arns is not None:
                self._values["security_group_arns"] = security_group_arns
            if subnet_arns is not None:
                self._values["subnet_arns"] = subnet_arns
            if vpc_arn is not None:
                self._values["vpc_arn"] = vpc_arn

        @builtins.property
        def security_group_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-vpcconfig.html#cfn-securityagent-pentest-vpcconfig-securitygrouparns
            '''
            result = self._values.get("security_group_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-vpcconfig.html#cfn-securityagent-pentest-vpcconfig-subnetarns
            '''
            result = self._values.get("subnet_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-pentest-vpcconfig.html#cfn-securityagent-pentest-vpcconfig-vpcarn
            '''
            result = self._values.get("vpc_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityagent.CfnPentestProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_space_id": "agentSpaceId",
        "assets": "assets",
        "service_role": "serviceRole",
        "code_remediation_strategy": "codeRemediationStrategy",
        "exclude_risk_types": "excludeRiskTypes",
        "log_config": "logConfig",
        "network_traffic_config": "networkTrafficConfig",
        "title": "title",
        "vpc_config": "vpcConfig",
    },
)
class CfnPentestProps:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        assets: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.AssetsProperty", typing.Dict[builtins.str, typing.Any]]],
        service_role: builtins.str,
        code_remediation_strategy: typing.Optional[builtins.str] = None,
        exclude_risk_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.CloudWatchLogProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        network_traffic_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.NetworkTrafficConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        title: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPentest.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPentest``.

        :param agent_space_id: 
        :param assets: 
        :param service_role: 
        :param code_remediation_strategy: 
        :param exclude_risk_types: 
        :param log_config: 
        :param network_traffic_config: 
        :param title: 
        :param vpc_config: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityagent as securityagent
            
            cfn_pentest_props = securityagent.CfnPentestProps(
                agent_space_id="agentSpaceId",
                assets=securityagent.CfnPentest.AssetsProperty(
                    actors=[securityagent.CfnPentest.ActorProperty(
                        authentication=securityagent.CfnPentest.AuthenticationProperty(
                            provider_type="providerType",
                            value="value"
                        ),
                        description="description",
                        identifier="identifier",
                        uris=["uris"]
                    )],
                    documents=[securityagent.CfnPentest.DocumentInfoProperty(
                        artifact_id="artifactId",
                        s3_location="s3Location"
                    )],
                    endpoints=[securityagent.CfnPentest.EndpointProperty(
                        uri="uri"
                    )],
                    integrated_repositories=[securityagent.CfnPentest.IntegratedRepositoryProperty(
                        integration_id="integrationId",
                        provider_resource_id="providerResourceId"
                    )],
                    source_code=[securityagent.CfnPentest.SourceCodeRepositoryProperty(
                        s3_location="s3Location"
                    )]
                ),
                service_role="serviceRole",
            
                # the properties below are optional
                code_remediation_strategy="codeRemediationStrategy",
                exclude_risk_types=["excludeRiskTypes"],
                log_config=securityagent.CfnPentest.CloudWatchLogProperty(
                    log_group="logGroup",
                    log_stream="logStream"
                ),
                network_traffic_config=securityagent.CfnPentest.NetworkTrafficConfigProperty(
                    custom_headers=[securityagent.CfnPentest.CustomHeaderProperty(
                        name="name",
                        value="value"
                    )],
                    rules=[securityagent.CfnPentest.NetworkTrafficRuleProperty(
                        effect="effect",
                        network_traffic_rule_type="networkTrafficRuleType",
                        pattern="pattern"
                    )]
                ),
                title="title",
                vpc_config=securityagent.CfnPentest.VpcConfigProperty(
                    security_group_arns=["securityGroupArns"],
                    subnet_arns=["subnetArns"],
                    vpc_arn="vpcArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c559e5db197574d4ae1f025e3b803c57f3be51b8ece875af311e31ee53439996)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument assets", value=assets, expected_type=type_hints["assets"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument code_remediation_strategy", value=code_remediation_strategy, expected_type=type_hints["code_remediation_strategy"])
            check_type(argname="argument exclude_risk_types", value=exclude_risk_types, expected_type=type_hints["exclude_risk_types"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument network_traffic_config", value=network_traffic_config, expected_type=type_hints["network_traffic_config"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "assets": assets,
            "service_role": service_role,
        }
        if code_remediation_strategy is not None:
            self._values["code_remediation_strategy"] = code_remediation_strategy
        if exclude_risk_types is not None:
            self._values["exclude_risk_types"] = exclude_risk_types
        if log_config is not None:
            self._values["log_config"] = log_config
        if network_traffic_config is not None:
            self._values["network_traffic_config"] = network_traffic_config
        if title is not None:
            self._values["title"] = title
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-agentspaceid
        '''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assets(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPentest.AssetsProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-assets
        '''
        result = self._values.get("assets")
        assert result is not None, "Required property 'assets' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPentest.AssetsProperty"], result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-servicerole
        '''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_remediation_strategy(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-coderemediationstrategy
        '''
        result = self._values.get("code_remediation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_risk_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-excluderisktypes
        '''
        result = self._values.get("exclude_risk_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.CloudWatchLogProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-logconfig
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.CloudWatchLogProperty"]], result)

    @builtins.property
    def network_traffic_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficConfigProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-networktrafficconfig
        '''
        result = self._values.get("network_traffic_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.NetworkTrafficConfigProperty"]], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.VpcConfigProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-pentest.html#cfn-securityagent-pentest-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPentest.VpcConfigProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPentestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITargetDomainRef_af00a826, _ITaggableV2_4e6798f8)
class CfnTargetDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityagent.CfnTargetDomain",
):
    '''Resource Type definition for AWS::SecurityAgent::TargetDomain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-targetdomain.html
    :cloudformationResource: AWS::SecurityAgent::TargetDomain
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityagent as securityagent
        
        cfn_target_domain = securityagent.CfnTargetDomain(self, "MyCfnTargetDomain",
            target_domain_name="targetDomainName",
            verification_method="verificationMethod",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        target_domain_name: builtins.str,
        verification_method: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SecurityAgent::TargetDomain``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param target_domain_name: Domain name of the target domain.
        :param verification_method: Verification method for the target domain.
        :param tags: Tags for the target domain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__878ffc1db10f802dace8d2e2b8da197fc72a464ee7e1bf4b758459d40f69bdbd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTargetDomainProps(
            target_domain_name=target_domain_name,
            verification_method=verification_method,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTargetDomain")
    @builtins.classmethod
    def arn_for_target_domain(
        cls,
        resource: "_ITargetDomainRef_af00a826",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81e1761bf769450d26e9a44c689b180a0313093c94213dc2efb8725854e1c567)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTargetDomain", [resource]))

    @jsii.member(jsii_name="fromTargetDomainId")
    @builtins.classmethod
    def from_target_domain_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        target_domain_id: builtins.str,
    ) -> "_ITargetDomainRef_af00a826":
        '''Creates a new ITargetDomainRef from a targetDomainId.

        :param scope: -
        :param id: -
        :param target_domain_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feaccacc26d6486ee808ff6976e54b897467200721d393339a2626c7140a988e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target_domain_id", value=target_domain_id, expected_type=type_hints["target_domain_id"])
        return typing.cast("_ITargetDomainRef_af00a826", jsii.sinvoke(cls, "fromTargetDomainId", [scope, id, target_domain_id]))

    @jsii.member(jsii_name="isCfnTargetDomain")
    @builtins.classmethod
    def is_cfn_target_domain(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTargetDomain.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6d3eef3f7c3cd789ab79da3088eb61d31f8a51b2596f878c00b9950199901e0)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTargetDomain", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38176af85c78aacf28bcca6103451599f6c0a18d0e1194a676b1dee7e22dc33c)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d07980d2478f727d19e075dbe061b47a6e20a6fb50a86fdbb29ab13a8cf4464)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Timestamp when the target domain was registered.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetDomainId")
    def attr_target_domain_id(self) -> builtins.str:
        '''Unique identifier of the target domain.

        :cloudformationAttribute: TargetDomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrVerificationDetails")
    def attr_verification_details(self) -> "_IResolvable_da3f097b":
        '''Verification details to verify registered target domain.

        :cloudformationAttribute: VerificationDetails
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrVerificationDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrVerificationStatus")
    def attr_verification_status(self) -> builtins.str:
        '''Current verification status of the registered target domain.

        :cloudformationAttribute: VerificationStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVerificationStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVerifiedAt")
    def attr_verified_at(self) -> builtins.str:
        '''Timestamp when the target domain was last successfully verified.

        :cloudformationAttribute: VerifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVerifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="targetDomainRef")
    def target_domain_ref(self) -> "_TargetDomainReference_ceabb397":
        '''A reference to a TargetDomain resource.'''
        return typing.cast("_TargetDomainReference_ceabb397", jsii.get(self, "targetDomainRef"))

    @builtins.property
    @jsii.member(jsii_name="targetDomainName")
    def target_domain_name(self) -> builtins.str:
        '''Domain name of the target domain.'''
        return typing.cast(builtins.str, jsii.get(self, "targetDomainName"))

    @target_domain_name.setter
    def target_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d6c4b286fe30ffd05bdc92aba839ee70a4ca4bb588a990624b2c475fd0538d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDomainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="verificationMethod")
    def verification_method(self) -> builtins.str:
        '''Verification method for the target domain.'''
        return typing.cast(builtins.str, jsii.get(self, "verificationMethod"))

    @verification_method.setter
    def verification_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd6564e9fb3e24116f69a58cefae08e448259ede7a9abafed661403d6b1178b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verificationMethod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags for the target domain.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6f042892550a98541edaa6e1796a1758b068d75e0519ff58ac34acd15b57da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnTargetDomain.DnsVerificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_record_name": "dnsRecordName",
            "dns_record_type": "dnsRecordType",
            "token": "token",
        },
    )
    class DnsVerificationProperty:
        def __init__(
            self,
            *,
            dns_record_name: typing.Optional[builtins.str] = None,
            dns_record_type: typing.Optional[builtins.str] = None,
            token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents DNS TXT verification details.

            :param dns_record_name: Record name to be added in DNS for target domain.
            :param dns_record_type: Type of record to be added in DNS for target domain.
            :param token: Token used to verify domain ownership.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-dnsverification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                dns_verification_property = securityagent.CfnTargetDomain.DnsVerificationProperty(
                    dns_record_name="dnsRecordName",
                    dns_record_type="dnsRecordType",
                    token="token"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bdd34122559827ef7f15faedc167343795db3461e498b9b4f70e66099c84d6d)
                check_type(argname="argument dns_record_name", value=dns_record_name, expected_type=type_hints["dns_record_name"])
                check_type(argname="argument dns_record_type", value=dns_record_type, expected_type=type_hints["dns_record_type"])
                check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dns_record_name is not None:
                self._values["dns_record_name"] = dns_record_name
            if dns_record_type is not None:
                self._values["dns_record_type"] = dns_record_type
            if token is not None:
                self._values["token"] = token

        @builtins.property
        def dns_record_name(self) -> typing.Optional[builtins.str]:
            '''Record name to be added in DNS for target domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-dnsverification.html#cfn-securityagent-targetdomain-dnsverification-dnsrecordname
            '''
            result = self._values.get("dns_record_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dns_record_type(self) -> typing.Optional[builtins.str]:
            '''Type of record to be added in DNS for target domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-dnsverification.html#cfn-securityagent-targetdomain-dnsverification-dnsrecordtype
            '''
            result = self._values.get("dns_record_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token(self) -> typing.Optional[builtins.str]:
            '''Token used to verify domain ownership.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-dnsverification.html#cfn-securityagent-targetdomain-dnsverification-token
            '''
            result = self._values.get("token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DnsVerificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnTargetDomain.HttpVerificationProperty",
        jsii_struct_bases=[],
        name_mapping={"route_path": "routePath", "token": "token"},
    )
    class HttpVerificationProperty:
        def __init__(
            self,
            *,
            route_path: typing.Optional[builtins.str] = None,
            token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents HTTP route verification details.

            :param route_path: Route path where verification token should be placed.
            :param token: Token used to verify domain ownership.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-httpverification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                http_verification_property = securityagent.CfnTargetDomain.HttpVerificationProperty(
                    route_path="routePath",
                    token="token"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f08bc9c789c7c94972c4a50bbef536b0c48fee8512bb999ce10923b9ddff45fa)
                check_type(argname="argument route_path", value=route_path, expected_type=type_hints["route_path"])
                check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if route_path is not None:
                self._values["route_path"] = route_path
            if token is not None:
                self._values["token"] = token

        @builtins.property
        def route_path(self) -> typing.Optional[builtins.str]:
            '''Route path where verification token should be placed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-httpverification.html#cfn-securityagent-targetdomain-httpverification-routepath
            '''
            result = self._values.get("route_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token(self) -> typing.Optional[builtins.str]:
            '''Token used to verify domain ownership.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-httpverification.html#cfn-securityagent-targetdomain-httpverification-token
            '''
            result = self._values.get("token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpVerificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityagent.CfnTargetDomain.VerificationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_txt": "dnsTxt",
            "http_route": "httpRoute",
            "method": "method",
        },
    )
    class VerificationDetailsProperty:
        def __init__(
            self,
            *,
            dns_txt: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTargetDomain.DnsVerificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            http_route: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTargetDomain.HttpVerificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            method: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Verification details to verify registered target domain.

            :param dns_txt: Represents DNS TXT verification details.
            :param http_route: Represents HTTP route verification details.
            :param method: Type of domain ownership verification method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-verificationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityagent as securityagent
                
                verification_details_property = securityagent.CfnTargetDomain.VerificationDetailsProperty(
                    dns_txt=securityagent.CfnTargetDomain.DnsVerificationProperty(
                        dns_record_name="dnsRecordName",
                        dns_record_type="dnsRecordType",
                        token="token"
                    ),
                    http_route=securityagent.CfnTargetDomain.HttpVerificationProperty(
                        route_path="routePath",
                        token="token"
                    ),
                    method="method"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11e4fb69c6cced95c934c5eaec53323f5777c7c29dc89c1ef48e276a60de1388)
                check_type(argname="argument dns_txt", value=dns_txt, expected_type=type_hints["dns_txt"])
                check_type(argname="argument http_route", value=http_route, expected_type=type_hints["http_route"])
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dns_txt is not None:
                self._values["dns_txt"] = dns_txt
            if http_route is not None:
                self._values["http_route"] = http_route
            if method is not None:
                self._values["method"] = method

        @builtins.property
        def dns_txt(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTargetDomain.DnsVerificationProperty"]]:
            '''Represents DNS TXT verification details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-verificationdetails.html#cfn-securityagent-targetdomain-verificationdetails-dnstxt
            '''
            result = self._values.get("dns_txt")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTargetDomain.DnsVerificationProperty"]], result)

        @builtins.property
        def http_route(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTargetDomain.HttpVerificationProperty"]]:
            '''Represents HTTP route verification details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-verificationdetails.html#cfn-securityagent-targetdomain-verificationdetails-httproute
            '''
            result = self._values.get("http_route")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTargetDomain.HttpVerificationProperty"]], result)

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''Type of domain ownership verification method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityagent-targetdomain-verificationdetails.html#cfn-securityagent-targetdomain-verificationdetails-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VerificationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityagent.CfnTargetDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "target_domain_name": "targetDomainName",
        "verification_method": "verificationMethod",
        "tags": "tags",
    },
)
class CfnTargetDomainProps:
    def __init__(
        self,
        *,
        target_domain_name: builtins.str,
        verification_method: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTargetDomain``.

        :param target_domain_name: Domain name of the target domain.
        :param verification_method: Verification method for the target domain.
        :param tags: Tags for the target domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-targetdomain.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityagent as securityagent
            
            cfn_target_domain_props = securityagent.CfnTargetDomainProps(
                target_domain_name="targetDomainName",
                verification_method="verificationMethod",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f1b75c7c137d29b68d0ad3172a61002b50fd0f7ac20c14fe2f8c007fb86c1fb)
            check_type(argname="argument target_domain_name", value=target_domain_name, expected_type=type_hints["target_domain_name"])
            check_type(argname="argument verification_method", value=verification_method, expected_type=type_hints["verification_method"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_domain_name": target_domain_name,
            "verification_method": verification_method,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def target_domain_name(self) -> builtins.str:
        '''Domain name of the target domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-targetdomain.html#cfn-securityagent-targetdomain-targetdomainname
        '''
        result = self._values.get("target_domain_name")
        assert result is not None, "Required property 'target_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def verification_method(self) -> builtins.str:
        '''Verification method for the target domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-targetdomain.html#cfn-securityagent-targetdomain-verificationmethod
        '''
        result = self._values.get("verification_method")
        assert result is not None, "Required property 'verification_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags for the target domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityagent-targetdomain.html#cfn-securityagent-targetdomain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTargetDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAgentSpace",
    "CfnAgentSpaceProps",
    "CfnApplication",
    "CfnApplicationProps",
    "CfnPentest",
    "CfnPentestProps",
    "CfnTargetDomain",
    "CfnTargetDomainProps",
]

publication.publish()

def _typecheckingstub__3ef24fb7e0398f97f2bf34bb92f534c54e23ad1b57db92995399f3969c878222(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    aws_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.AWSResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    code_review_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.CodeReviewSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    integrated_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.IntegratedResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_domain_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab99b207630f0fdce3650e450353eb2b8300110d6b87f21dea92ec73dcd5bd9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6908f826f50bf019406c2b4d7515bd3f8bb60cc61e6c3620b45f9c2502c594a5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92cfc4584067e1e03d34496841f2f33ceaa43ec305156ce5c5500c1cc3729005(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b16a68b67bb21513bdb7f3be0b225a0e1abb9fee8fa6c5ee87a26614c4447ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a750a967e1fac12db17d49079d9c04596b2af1ef6de44df7761e599169a3c4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAgentSpace.AWSResourcesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1b2700da399046746b605e7912029af38d6e20164cc75a19db6ec285c91ca2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAgentSpace.CodeReviewSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883a998f4fead4777b8e089453a192c17422395f96917106145a0ad3c43bff09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a703a49b3f1a81fcad7cfc4a340dee66e153cc8a77237f59ed1fd706bc41afca(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAgentSpace.IntegratedResourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8158b14701610c6f2fd630d80073e48e59db833f9491078d3ed86b230e8b7ee4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452bbe46d262236c7182002fa61ed5aa51c2c3cca7df3a25caa1cc6af3deeb86(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e34b178a1218f29101cd534305dd0a625fa59e5c5a3e6c1661a1d658a1aa6c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3a1f09aa1793040964f17ba37ea2d39035a52835521a06a2fd2429331eba65(
    *,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    lambda_function_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpcs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47533237cc30a0b4e6af78a36be81461d974345e71b59894210932a057ff4753(
    *,
    controls_scanning: typing.Union[builtins.bool, _IResolvable_da3f097b],
    general_purpose_scanning: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fba15574f3d88d87ae613250d24376367fc26356706c91ce38869879d225d774(
    *,
    integration: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55cde8190d06b2c2ee5d0fc0c59ee2598deb376092113b341960302ca22f3fa(
    *,
    security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63fcebc9f38c568223136c35c5b8bf056aaf1d2658a8795d9f9fac31e9b9d41(
    *,
    name: builtins.str,
    aws_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.AWSResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    code_review_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.CodeReviewSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    integrated_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.IntegratedResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_domain_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__578e51536b17e4aa32471e1d1fd3cd36d0e5c7e116bd3ca5ec01a9f0375c8eaf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_kms_key_id: typing.Optional[builtins.str] = None,
    id_c_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.IdCConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c433d5a147ba3da470a74a02ec6dd989c1b96e915ea645eaef3e76561553d75(
    resource: _IApplicationRef_47d5c35f,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f2c6116a3f36a4ce344c2f9db127c9051bfb6434e801671ada9ac6759c6b2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a09967466853d14feb121c24215733fe03c1d1391f8665057e98ba520571424(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04cffc3747cf67ceaff2b6e916311d776ba0b34d476bedfb51c1525d5eb61aad(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c36892ec084e2095c0e7432c2d16c26897ae9f27f7fd82501dc58469a11a032(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1b23f95eb73ca8d49ebfe6e25d6191771b19653585d80e49067d6c9d2eaebf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ecbd010873e2be9992a4b7544fb8d13bbefabe8ec47426007067d9833779d6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.IdCConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc2feb71ef581c3b5a294d96c8d2c5b3409f62c2bbf7ed680d87fc10fbb73dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e425ca9094c48d21d490f93d36a1ee1223c9a17938db33636007495504db25f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e26c4b578f401e1801e9bee4038a5ded65c9be7b3ddd0a76f89eb025cc9eefc(
    *,
    id_c_application_arn: typing.Optional[builtins.str] = None,
    id_c_instance_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b36d9297d6d873ed09ead98b35106a55f3a507c8ce2351f00ffb25948761dfd(
    *,
    default_kms_key_id: typing.Optional[builtins.str] = None,
    id_c_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.IdCConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d83c0f79102402315ab2667cd779997a2fd84704dc25119af31f0018a831848(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_space_id: builtins.str,
    assets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.AssetsProperty, typing.Dict[builtins.str, typing.Any]]],
    service_role: builtins.str,
    code_remediation_strategy: typing.Optional[builtins.str] = None,
    exclude_risk_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.CloudWatchLogProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_traffic_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.NetworkTrafficConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    title: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91cc55571ff5885f1a1d0b1933fbe225557b1f86c95d8ba38bc33fe4c61e84a(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa7bfb9f39891718a13a4e778189ad97817330895f8e15bef30dfe07550ac51(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a2f1484080dcc24c0effa2a509767dbea4fad3028a7ab44a871ebb67120b1e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a6d1b2d87fc882cf2734deb7858624f1dcc00e7c63002525d1a9fa7cd3d6e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12345bae4c066f259b044fe64398908ebbbf527bb6d6854d69571a436a5aa6c0(
    value: typing.Union[_IResolvable_da3f097b, CfnPentest.AssetsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae21e38e0529ed7148f6ea4283dba1ed6d7f4d6eab2c535834d2aebb4788a140(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f11a8b62790439898a591432715582d38bc20ececc324a951cdb947a80581ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e3c6ff9fc0223ce453b38a2e22fc60a5081555fd3eb0f71c75468863a92b75(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3c320e1d6daf33457b394bd52277ab4d04be687b9915b95f0d348f241f7b38(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPentest.CloudWatchLogProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d4fb3fd1f4f28dd91245a6e6a1cbd6d3f9175fdb58d771301ab68da826171b6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPentest.NetworkTrafficConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dbf45fab9e1a4ebffd4a194d8dabfcc48049da8b74581218b16440ec3b6841(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c52839de7f5fb0b1842f597d1d019725896583f4fbfaa741b87eaa453825436(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPentest.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789552d2a299b54f21a25572baa25b7b652499c9578bcdf16e84796ef97b2678(
    *,
    authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.AuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    identifier: typing.Optional[builtins.str] = None,
    uris: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90ac541f4598ca1ed36733bf9d5a278158f6b2a40ecc4723d2aa1ebff5ec5fa5(
    *,
    actors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.ActorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.DocumentInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    integrated_repositories: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.IntegratedRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.SourceCodeRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3532134765f42b5beced42cd2054d3ee1cba754ed2a8662007413abe8b3a7ed7(
    *,
    provider_type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0010faccc2dea59f0a9b2019a1a5ccfb658f48bd657c0f07a7ecda42c683cbd(
    *,
    log_group: typing.Optional[builtins.str] = None,
    log_stream: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff7bb011d1dc68f7f5b77ec0006ed8c2c4d7fc669ef653d7e4901b2d069e6a6(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4656bb528684e0993c3460489d2969558cf2587fa69964451204d94d714a217f(
    *,
    artifact_id: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__562d8396754a9f08650638a9ecc518a12e0b18c5256fc88afb318a18e3ffb029(
    *,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c1c48352289031e291e4b2d1c94656660c67be9e64899490c98b8ea5799b99(
    *,
    integration_id: builtins.str,
    provider_resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46b4c00871d10d581e0a437b2abc4ca1f9ec70f49f35b5756a2f6c310f63645(
    *,
    custom_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.CustomHeaderProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.NetworkTrafficRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346479bc3d7bb9e27fe6c61adba2e4e5fca86ff3607b3c398cef04141179a54d(
    *,
    effect: typing.Optional[builtins.str] = None,
    network_traffic_rule_type: typing.Optional[builtins.str] = None,
    pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac9ae05bfdd52d767951d638cfa69e9ccda258b973752d2d20a628d9a31eaa37(
    *,
    s3_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61eb619b94085829ddd0e1e01d9220a86b2f2a7d6cf90af8a7ef5406580f8da(
    *,
    security_group_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c559e5db197574d4ae1f025e3b803c57f3be51b8ece875af311e31ee53439996(
    *,
    agent_space_id: builtins.str,
    assets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.AssetsProperty, typing.Dict[builtins.str, typing.Any]]],
    service_role: builtins.str,
    code_remediation_strategy: typing.Optional[builtins.str] = None,
    exclude_risk_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.CloudWatchLogProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_traffic_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.NetworkTrafficConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    title: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPentest.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__878ffc1db10f802dace8d2e2b8da197fc72a464ee7e1bf4b758459d40f69bdbd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target_domain_name: builtins.str,
    verification_method: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81e1761bf769450d26e9a44c689b180a0313093c94213dc2efb8725854e1c567(
    resource: _ITargetDomainRef_af00a826,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feaccacc26d6486ee808ff6976e54b897467200721d393339a2626c7140a988e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    target_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6d3eef3f7c3cd789ab79da3088eb61d31f8a51b2596f878c00b9950199901e0(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38176af85c78aacf28bcca6103451599f6c0a18d0e1194a676b1dee7e22dc33c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d07980d2478f727d19e075dbe061b47a6e20a6fb50a86fdbb29ab13a8cf4464(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d6c4b286fe30ffd05bdc92aba839ee70a4ca4bb588a990624b2c475fd0538d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd6564e9fb3e24116f69a58cefae08e448259ede7a9abafed661403d6b1178b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6f042892550a98541edaa6e1796a1758b068d75e0519ff58ac34acd15b57da(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bdd34122559827ef7f15faedc167343795db3461e498b9b4f70e66099c84d6d(
    *,
    dns_record_name: typing.Optional[builtins.str] = None,
    dns_record_type: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08bc9c789c7c94972c4a50bbef536b0c48fee8512bb999ce10923b9ddff45fa(
    *,
    route_path: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e4fb69c6cced95c934c5eaec53323f5777c7c29dc89c1ef48e276a60de1388(
    *,
    dns_txt: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetDomain.DnsVerificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTargetDomain.HttpVerificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f1b75c7c137d29b68d0ad3172a61002b50fd0f7ac20c14fe2f8c007fb86c1fb(
    *,
    target_domain_name: builtins.str,
    verification_method: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

r'''
# AWS::NovaAct Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_novaact as novaact
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NovaAct construct libraries](https://constructs.dev/search?q=novaact)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NovaAct resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NovaAct.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NovaAct](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NovaAct.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_novaact import (
    IWorkflowDefinitionRef as _IWorkflowDefinitionRef_70087ab1,
    WorkflowDefinitionReference as _WorkflowDefinitionReference_59ffa042,
)


@jsii.implements(_IInspectable_c2943556, _IWorkflowDefinitionRef_70087ab1)
class CfnWorkflowDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_novaact.CfnWorkflowDefinition",
):
    '''Definition of AWS::NovaAct::WorkflowDefinition Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-novaact-workflowdefinition.html
    :cloudformationResource: AWS::NovaAct::WorkflowDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_novaact as novaact
        
        cfn_workflow_definition = novaact.CfnWorkflowDefinition(self, "MyCfnWorkflowDefinition",
            name="name",
        
            # the properties below are optional
            description="description",
            export_config=novaact.CfnWorkflowDefinition.WorkflowExportConfigProperty(
                s3_bucket_name="s3BucketName",
        
                # the properties below are optional
                s3_key_prefix="s3KeyPrefix"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        export_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowDefinition.WorkflowExportConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::NovaAct::WorkflowDefinition``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the workflow definition. Must be unique within your account and region.
        :param description: An optional description of the workflow definition's purpose and functionality.
        :param export_config: Configuration settings for exporting workflow execution data and logs to Amazon S3.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093f8a864ee72702b771cc9cdf3adce7cf2a97464e0c030381a32c68b796bf67)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowDefinitionProps(
            name=name, description=description, export_config=export_config
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkflowDefinition")
    @builtins.classmethod
    def arn_for_workflow_definition(
        cls,
        resource: "_IWorkflowDefinitionRef_70087ab1",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d00ba4e93f474c3a5a106ad995b260e1ddfb0b0b28c8b7a591fdaff9129f41)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkflowDefinition", [resource]))

    @jsii.member(jsii_name="isCfnWorkflowDefinition")
    @builtins.classmethod
    def is_cfn_workflow_definition(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkflowDefinition.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf692b32b5dfafd3e257db2aeca9c96a31d97b58293ad256c94a1c5bf51db5d3)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkflowDefinition", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6283bd89642b973de05b991d6961ca2b21e02a90044d3cddb3bed3c252bc7466)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d003c303ead7b5ed96c9ecacef8b790dea75bd08b4c5cc15cb0511c35e636df)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the workflow definition.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the workflow definition was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the workflow definition.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="workflowDefinitionRef")
    def workflow_definition_ref(self) -> "_WorkflowDefinitionReference_59ffa042":
        '''A reference to a WorkflowDefinition resource.'''
        return typing.cast("_WorkflowDefinitionReference_59ffa042", jsii.get(self, "workflowDefinitionRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the workflow definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4287a78237ea24e16d0143f2346cfe58823d507634f64b7fb2858d7e6209ba99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the workflow definition's purpose and functionality.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce8b50d69ea19fefafdeda8362c5f53861d48507669ec42b02010972e227a837)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="exportConfig")
    def export_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowDefinition.WorkflowExportConfigProperty"]]:
        '''Configuration settings for exporting workflow execution data and logs to Amazon S3.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowDefinition.WorkflowExportConfigProperty"]], jsii.get(self, "exportConfig"))

    @export_config.setter
    def export_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowDefinition.WorkflowExportConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912842274cbae4c384017f1852cac251c1842dc0160302abe13698ac68196d08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_novaact.CfnWorkflowDefinition.WorkflowExportConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "s3_key_prefix": "s3KeyPrefix",
        },
    )
    class WorkflowExportConfigProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: builtins.str,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for exporting workflow execution data and logs to Amazon S3.

            :param s3_bucket_name: The name of the Amazon S3 bucket for exporting workflow data.
            :param s3_key_prefix: An optional prefix for Amazon S3 object keys to organize exported data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-novaact-workflowdefinition-workflowexportconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_novaact as novaact
                
                workflow_export_config_property = novaact.CfnWorkflowDefinition.WorkflowExportConfigProperty(
                    s3_bucket_name="s3BucketName",
                
                    # the properties below are optional
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__702bd201e9d609f53af06bb05ea9fd90391fb603dc3cdb113bf534b9d81456c6)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket_name": s3_bucket_name,
            }
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def s3_bucket_name(self) -> builtins.str:
            '''The name of the Amazon S3 bucket for exporting workflow data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-novaact-workflowdefinition-workflowexportconfig.html#cfn-novaact-workflowdefinition-workflowexportconfig-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            assert result is not None, "Required property 's3_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''An optional prefix for Amazon S3 object keys to organize exported data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-novaact-workflowdefinition-workflowexportconfig.html#cfn-novaact-workflowdefinition-workflowexportconfig-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowExportConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_novaact.CfnWorkflowDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "export_config": "exportConfig",
    },
)
class CfnWorkflowDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        export_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowDefinition.WorkflowExportConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflowDefinition``.

        :param name: The name of the workflow definition. Must be unique within your account and region.
        :param description: An optional description of the workflow definition's purpose and functionality.
        :param export_config: Configuration settings for exporting workflow execution data and logs to Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-novaact-workflowdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_novaact as novaact
            
            cfn_workflow_definition_props = novaact.CfnWorkflowDefinitionProps(
                name="name",
            
                # the properties below are optional
                description="description",
                export_config=novaact.CfnWorkflowDefinition.WorkflowExportConfigProperty(
                    s3_bucket_name="s3BucketName",
            
                    # the properties below are optional
                    s3_key_prefix="s3KeyPrefix"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f03183f2df66815d167de60ee918a19d6d38d60dabdc1818bd9472ea62806bfb)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument export_config", value=export_config, expected_type=type_hints["export_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if export_config is not None:
            self._values["export_config"] = export_config

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the workflow definition.

        Must be unique within your account and region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-novaact-workflowdefinition.html#cfn-novaact-workflowdefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the workflow definition's purpose and functionality.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-novaact-workflowdefinition.html#cfn-novaact-workflowdefinition-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def export_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowDefinition.WorkflowExportConfigProperty"]]:
        '''Configuration settings for exporting workflow execution data and logs to Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-novaact-workflowdefinition.html#cfn-novaact-workflowdefinition-exportconfig
        '''
        result = self._values.get("export_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowDefinition.WorkflowExportConfigProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnWorkflowDefinition",
    "CfnWorkflowDefinitionProps",
]

publication.publish()

def _typecheckingstub__093f8a864ee72702b771cc9cdf3adce7cf2a97464e0c030381a32c68b796bf67(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    export_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowDefinition.WorkflowExportConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d00ba4e93f474c3a5a106ad995b260e1ddfb0b0b28c8b7a591fdaff9129f41(
    resource: _IWorkflowDefinitionRef_70087ab1,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf692b32b5dfafd3e257db2aeca9c96a31d97b58293ad256c94a1c5bf51db5d3(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6283bd89642b973de05b991d6961ca2b21e02a90044d3cddb3bed3c252bc7466(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d003c303ead7b5ed96c9ecacef8b790dea75bd08b4c5cc15cb0511c35e636df(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4287a78237ea24e16d0143f2346cfe58823d507634f64b7fb2858d7e6209ba99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce8b50d69ea19fefafdeda8362c5f53861d48507669ec42b02010972e227a837(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912842274cbae4c384017f1852cac251c1842dc0160302abe13698ac68196d08(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflowDefinition.WorkflowExportConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702bd201e9d609f53af06bb05ea9fd90391fb603dc3cdb113bf534b9d81456c6(
    *,
    s3_bucket_name: builtins.str,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f03183f2df66815d167de60ee918a19d6d38d60dabdc1818bd9472ea62806bfb(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    export_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowDefinition.WorkflowExportConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

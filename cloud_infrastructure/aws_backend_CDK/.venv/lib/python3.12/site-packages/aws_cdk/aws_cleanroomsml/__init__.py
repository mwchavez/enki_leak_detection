r'''
# AWS::CleanRoomsML Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cleanroomsml as cleanroomsml
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CleanRoomsML construct libraries](https://constructs.dev/search?q=cleanroomsml)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CleanRoomsML resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CleanRoomsML](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRoomsML.html).

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
from ..interfaces.aws_cleanroomsml import (
    ConfiguredModelAlgorithmAssociationReference as _ConfiguredModelAlgorithmAssociationReference_5b374d85,
    ConfiguredModelAlgorithmReference as _ConfiguredModelAlgorithmReference_bcc5a30f,
    IConfiguredModelAlgorithmAssociationRef as _IConfiguredModelAlgorithmAssociationRef_5d6df5cb,
    IConfiguredModelAlgorithmRef as _IConfiguredModelAlgorithmRef_c000ba6b,
    ITrainingDatasetRef as _ITrainingDatasetRef_e0f12c42,
    TrainingDatasetReference as _TrainingDatasetReference_d53f15ee,
)


@jsii.implements(_IInspectable_c2943556, _IConfiguredModelAlgorithmRef_c000ba6b, _ITaggableV2_4e6798f8)
class CfnConfiguredModelAlgorithm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithm",
):
    '''Definition of AWS::CleanRoomsML::ConfiguredModelAlgorithm Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html
    :cloudformationResource: AWS::CleanRoomsML::ConfiguredModelAlgorithm
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanroomsml as cleanroomsml
        
        cfn_configured_model_algorithm = cleanroomsml.CfnConfiguredModelAlgorithm(self, "MyCfnConfiguredModelAlgorithm",
            name="name",
            role_arn="roleArn",
        
            # the properties below are optional
            description="description",
            inference_container_config=cleanroomsml.CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty(
                image_uri="imageUri"
            ),
            kms_key_arn="kmsKeyArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            training_container_config=cleanroomsml.CfnConfiguredModelAlgorithm.ContainerConfigProperty(
                image_uri="imageUri",
        
                # the properties below are optional
                arguments=["arguments"],
                entrypoint=["entrypoint"],
                metric_definitions=[cleanroomsml.CfnConfiguredModelAlgorithm.MetricDefinitionProperty(
                    name="name",
                    regex="regex"
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        inference_container_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        training_container_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithm.ContainerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CleanRoomsML::ConfiguredModelAlgorithm``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: 
        :param role_arn: 
        :param description: 
        :param inference_container_config: 
        :param kms_key_arn: 
        :param tags: An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm.
        :param training_container_config: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9add5e5fc7b05d2aa8b862a0b3f77721f43df75943badf1e52b1b8c11b661f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfiguredModelAlgorithmProps(
            name=name,
            role_arn=role_arn,
            description=description,
            inference_container_config=inference_container_config,
            kms_key_arn=kms_key_arn,
            tags=tags,
            training_container_config=training_container_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForConfiguredModelAlgorithm")
    @builtins.classmethod
    def arn_for_configured_model_algorithm(
        cls,
        resource: "_IConfiguredModelAlgorithmRef_c000ba6b",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe92be2373e1b28b447ac31793dbefd680b4163dd1c777ba2c309b2cd490a2d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForConfiguredModelAlgorithm", [resource]))

    @jsii.member(jsii_name="isCfnConfiguredModelAlgorithm")
    @builtins.classmethod
    def is_cfn_configured_model_algorithm(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnConfiguredModelAlgorithm.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58172d7c5bba2efab8369c3c9b9d2892e8e3ef50d1ce32e7b1c640d267b33a07)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnConfiguredModelAlgorithm", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__101100b1e573c15641233745c75f387f2f906f34b6df888bcd29bf79633a8239)
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
            type_hints = typing.get_type_hints(_typecheckingstub__403ba867d7d1404bdf36baa4c2b3dcd5d1264c6914f5aac5fbc3ab0fe0f98c1c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguredModelAlgorithmArn")
    def attr_configured_model_algorithm_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConfiguredModelAlgorithmArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfiguredModelAlgorithmArn"))

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
    @jsii.member(jsii_name="configuredModelAlgorithmRef")
    def configured_model_algorithm_ref(
        self,
    ) -> "_ConfiguredModelAlgorithmReference_bcc5a30f":
        '''A reference to a ConfiguredModelAlgorithm resource.'''
        return typing.cast("_ConfiguredModelAlgorithmReference_bcc5a30f", jsii.get(self, "configuredModelAlgorithmRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84fb62060d27ca3dad20b96f63aa1a385fd6527599eee76d7638f98e79daf6f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092e7369580c2f623975b01d4cab03e9c7197cd72d0d3895deae863689c4f248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cf7cbf05f79b61ec2c8bbdc62eeebca87800fe721f2dec8affb4867d42e4ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inferenceContainerConfig")
    def inference_container_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty"]], jsii.get(self, "inferenceContainerConfig"))

    @inference_container_config.setter
    def inference_container_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921d9695e86808b47495e9acd680f91eaa50034525dcec342e1d8fc730a30430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inferenceContainerConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b07aee4401db10797bdc20d2ff55e198cb0f54972f1dfa9058913c2b5bf44a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d3e6447ee2429ba914a52ccf1133c099d3f81703c4ce77859f7dd4f50b978a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trainingContainerConfig")
    def training_container_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.ContainerConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.ContainerConfigProperty"]], jsii.get(self, "trainingContainerConfig"))

    @training_container_config.setter
    def training_container_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.ContainerConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6881177ba8c4e4d4c7fabe1b3635afa39a446f6d7e1563f4fb879f52f5fb663d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trainingContainerConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithm.ContainerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "arguments": "arguments",
            "entrypoint": "entrypoint",
            "metric_definitions": "metricDefinitions",
        },
    )
    class ContainerConfigProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            metric_definitions: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithm.MetricDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param image_uri: 
            :param arguments: 
            :param entrypoint: 
            :param metric_definitions: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                container_config_property = cleanroomsml.CfnConfiguredModelAlgorithm.ContainerConfigProperty(
                    image_uri="imageUri",
                
                    # the properties below are optional
                    arguments=["arguments"],
                    entrypoint=["entrypoint"],
                    metric_definitions=[cleanroomsml.CfnConfiguredModelAlgorithm.MetricDefinitionProperty(
                        name="name",
                        regex="regex"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__12dd4ea50ae8c8c1f4153da75226b7aab6c9684ff49f6539afa13aadab810017)
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
                check_type(argname="argument arguments", value=arguments, expected_type=type_hints["arguments"])
                check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
                check_type(argname="argument metric_definitions", value=metric_definitions, expected_type=type_hints["metric_definitions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image_uri": image_uri,
            }
            if arguments is not None:
                self._values["arguments"] = arguments
            if entrypoint is not None:
                self._values["entrypoint"] = entrypoint
            if metric_definitions is not None:
                self._values["metric_definitions"] = metric_definitions

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.html#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.html#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-arguments
            '''
            result = self._values.get("arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.html#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-entrypoint
            '''
            result = self._values.get("entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def metric_definitions(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.MetricDefinitionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.html#cfn-cleanroomsml-configuredmodelalgorithm-containerconfig-metricdefinitions
            '''
            result = self._values.get("metric_definitions")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.MetricDefinitionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"image_uri": "imageUri"},
    )
    class InferenceContainerConfigProperty:
        def __init__(self, *, image_uri: builtins.str) -> None:
            '''
            :param image_uri: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                inference_container_config_property = cleanroomsml.CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty(
                    image_uri="imageUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d561138399fe485c7f8c1dab5da8276fb4f9104888afc0211c73814871f4db6)
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image_uri": image_uri,
            }

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig.html#cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InferenceContainerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithm.MetricDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "regex": "regex"},
    )
    class MetricDefinitionProperty:
        def __init__(self, *, name: builtins.str, regex: builtins.str) -> None:
            '''
            :param name: 
            :param regex: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                metric_definition_property = cleanroomsml.CfnConfiguredModelAlgorithm.MetricDefinitionProperty(
                    name="name",
                    regex="regex"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cbdc32e8e4e20cd09c57719079ab7392669c441363bb3abbe8820e7d46dd543)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "regex": regex,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition.html#cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def regex(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithm-metricdefinition.html#cfn-cleanroomsml-configuredmodelalgorithm-metricdefinition-regex
            '''
            result = self._values.get("regex")
            assert result is not None, "Required property 'regex' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IConfiguredModelAlgorithmAssociationRef_5d6df5cb, _ITaggableV2_4e6798f8)
class CfnConfiguredModelAlgorithmAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation",
):
    '''Definition of AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html
    :cloudformationResource: AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanroomsml as cleanroomsml
        
        cfn_configured_model_algorithm_association = cleanroomsml.CfnConfiguredModelAlgorithmAssociation(self, "MyCfnConfiguredModelAlgorithmAssociation",
            configured_model_algorithm_arn="configuredModelAlgorithmArn",
            membership_identifier="membershipIdentifier",
            name="name",
        
            # the properties below are optional
            description="description",
            privacy_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty(
                policies=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty(
                    trained_model_exports=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty(
                        files_to_export=["filesToExport"],
                        max_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty(
                            unit="unit",
                            value=123
                        )
                    ),
                    trained_model_inference_jobs=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty(
                        container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                            allowed_account_ids=["allowedAccountIds"],
        
                            # the properties below are optional
                            filter_pattern="filterPattern",
                            log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                entities_to_redact=["entitiesToRedact"],
        
                                # the properties below are optional
                                custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                    custom_data_identifiers=["customDataIdentifiers"]
                                )
                            ),
                            log_type="logType"
                        )],
                        max_output_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty(
                            unit="unit",
                            value=123
                        )
                    ),
                    trained_models=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty(
                        container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                            allowed_account_ids=["allowedAccountIds"],
        
                            # the properties below are optional
                            filter_pattern="filterPattern",
                            log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                entities_to_redact=["entitiesToRedact"],
        
                                # the properties below are optional
                                custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                    custom_data_identifiers=["customDataIdentifiers"]
                                )
                            ),
                            log_type="logType"
                        )],
                        container_metrics=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty(
                            noise_level="noiseLevel"
                        ),
                        max_artifact_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty(
                            unit="unit",
                            value=123
                        )
                    )
                )
            ),
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
        configured_model_algorithm_arn: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        privacy_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configured_model_algorithm_arn: 
        :param membership_identifier: 
        :param name: 
        :param description: 
        :param privacy_configuration: 
        :param tags: An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm association.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a034d9eda51309ce6906a92c52fe385af754cad01c4669704e95371412aa4c82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfiguredModelAlgorithmAssociationProps(
            configured_model_algorithm_arn=configured_model_algorithm_arn,
            membership_identifier=membership_identifier,
            name=name,
            description=description,
            privacy_configuration=privacy_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForConfiguredModelAlgorithmAssociation")
    @builtins.classmethod
    def arn_for_configured_model_algorithm_association(
        cls,
        resource: "_IConfiguredModelAlgorithmAssociationRef_5d6df5cb",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cddf6593a701a4d13683248bc56f69d821c1bf4fc0ccef76963a4b87cad49638)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForConfiguredModelAlgorithmAssociation", [resource]))

    @jsii.member(jsii_name="isCfnConfiguredModelAlgorithmAssociation")
    @builtins.classmethod
    def is_cfn_configured_model_algorithm_association(
        cls,
        x: typing.Any,
    ) -> builtins.bool:
        '''Checks whether the given object is a CfnConfiguredModelAlgorithmAssociation.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ef00d95c26cc59c2ba724cb02070915f111031775e7ae56cdc41a3f820eeb2)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnConfiguredModelAlgorithmAssociation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef2ecca8abcf092dfbf6e68a0f7acda79451843ec6255c9dbd8875c29d812ddd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc73243f20b7225a7b48092a7597b990d086b659b922246a618290bac56db7ed)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguredModelAlgorithmAssociationArn")
    def attr_configured_model_algorithm_association_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConfiguredModelAlgorithmAssociationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfiguredModelAlgorithmAssociationArn"))

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
    @jsii.member(jsii_name="configuredModelAlgorithmAssociationRef")
    def configured_model_algorithm_association_ref(
        self,
    ) -> "_ConfiguredModelAlgorithmAssociationReference_5b374d85":
        '''A reference to a ConfiguredModelAlgorithmAssociation resource.'''
        return typing.cast("_ConfiguredModelAlgorithmAssociationReference_5b374d85", jsii.get(self, "configuredModelAlgorithmAssociationRef"))

    @builtins.property
    @jsii.member(jsii_name="configuredModelAlgorithmArn")
    def configured_model_algorithm_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configuredModelAlgorithmArn"))

    @configured_model_algorithm_arn.setter
    def configured_model_algorithm_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acee9b91f31a6a5fb74a362703ae71ac574e762f84a7552fd4ffbf05f3f713b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuredModelAlgorithmArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69080d38e1f1bb9347d20cdb2de93f048e22f21654d45670e586dec664950498)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9798dbeaa85a39f5a37c80e1c3a3a0f30330711eb84e7a055c610f819c384e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2353683a85d08f04391a843c9b451c7da3479829cf55530f44efe6bd03c0a458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privacyConfiguration")
    def privacy_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty"]], jsii.get(self, "privacyConfiguration"))

    @privacy_configuration.setter
    def privacy_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df97e8aaaffba77a0d74c07b40612ccaa090c972cf24969395623262e80537b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privacyConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm association.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca97080fb41ace7427954bf826084b395f9f2457ef95662151d1aab7231a5b0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_data_identifiers": "customDataIdentifiers"},
    )
    class CustomEntityConfigProperty:
        def __init__(
            self,
            *,
            custom_data_identifiers: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param custom_data_identifiers: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                custom_entity_config_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                    custom_data_identifiers=["customDataIdentifiers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1710dcf96d19e57f9f6b1f22b1acb55122da536d5ca24e473b242ce21a52399b)
                check_type(argname="argument custom_data_identifiers", value=custom_data_identifiers, expected_type=type_hints["custom_data_identifiers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_data_identifiers": custom_data_identifiers,
            }

        @builtins.property
        def custom_data_identifiers(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-customentityconfig-customdataidentifiers
            '''
            result = self._values.get("custom_data_identifiers")
            assert result is not None, "Required property 'custom_data_identifiers' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomEntityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entities_to_redact": "entitiesToRedact",
            "custom_entity_config": "customEntityConfig",
        },
    )
    class LogRedactionConfigurationProperty:
        def __init__(
            self,
            *,
            entities_to_redact: typing.Sequence[builtins.str],
            custom_entity_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param entities_to_redact: 
            :param custom_entity_config: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                log_redaction_configuration_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                    entities_to_redact=["entitiesToRedact"],
                
                    # the properties below are optional
                    custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                        custom_data_identifiers=["customDataIdentifiers"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c103dcc9627e880f31873ee728f160d0ccf0209bd4c2ead6ae3da609454a5c1d)
                check_type(argname="argument entities_to_redact", value=entities_to_redact, expected_type=type_hints["entities_to_redact"])
                check_type(argname="argument custom_entity_config", value=custom_entity_config, expected_type=type_hints["custom_entity_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entities_to_redact": entities_to_redact,
            }
            if custom_entity_config is not None:
                self._values["custom_entity_config"] = custom_entity_config

        @builtins.property
        def entities_to_redact(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-entitiestoredact
            '''
            result = self._values.get("entities_to_redact")
            assert result is not None, "Required property 'entities_to_redact' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def custom_entity_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-logredactionconfiguration-customentityconfig
            '''
            result = self._values.get("custom_entity_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogRedactionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_account_ids": "allowedAccountIds",
            "filter_pattern": "filterPattern",
            "log_redaction_configuration": "logRedactionConfiguration",
            "log_type": "logType",
        },
    )
    class LogsConfigurationPolicyProperty:
        def __init__(
            self,
            *,
            allowed_account_ids: typing.Sequence[builtins.str],
            filter_pattern: typing.Optional[builtins.str] = None,
            log_redaction_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            log_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param allowed_account_ids: 
            :param filter_pattern: 
            :param log_redaction_configuration: 
            :param log_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                logs_configuration_policy_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                    allowed_account_ids=["allowedAccountIds"],
                
                    # the properties below are optional
                    filter_pattern="filterPattern",
                    log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                        entities_to_redact=["entitiesToRedact"],
                
                        # the properties below are optional
                        custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                            custom_data_identifiers=["customDataIdentifiers"]
                        )
                    ),
                    log_type="logType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c620013d45f62be0ac95f38666412f20f488540d33211aac358683a234dac6d3)
                check_type(argname="argument allowed_account_ids", value=allowed_account_ids, expected_type=type_hints["allowed_account_ids"])
                check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
                check_type(argname="argument log_redaction_configuration", value=log_redaction_configuration, expected_type=type_hints["log_redaction_configuration"])
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allowed_account_ids": allowed_account_ids,
            }
            if filter_pattern is not None:
                self._values["filter_pattern"] = filter_pattern
            if log_redaction_configuration is not None:
                self._values["log_redaction_configuration"] = log_redaction_configuration
            if log_type is not None:
                self._values["log_type"] = log_type

        @builtins.property
        def allowed_account_ids(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-allowedaccountids
            '''
            result = self._values.get("allowed_account_ids")
            assert result is not None, "Required property 'allowed_account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def filter_pattern(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-filterpattern
            '''
            result = self._values.get("filter_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_redaction_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logredactionconfiguration
            '''
            result = self._values.get("log_redaction_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty"]], result)

        @builtins.property
        def log_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-logsconfigurationpolicy-logtype
            '''
            result = self._values.get("log_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogsConfigurationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"noise_level": "noiseLevel"},
    )
    class MetricsConfigurationPolicyProperty:
        def __init__(self, *, noise_level: builtins.str) -> None:
            '''
            :param noise_level: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                metrics_configuration_policy_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty(
                    noise_level="noiseLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82f1b429531f0f1bf7945804821fec24222684078b3f82681f068a8a1511b66e)
                check_type(argname="argument noise_level", value=noise_level, expected_type=type_hints["noise_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "noise_level": noise_level,
            }

        @builtins.property
        def noise_level(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-metricsconfigurationpolicy-noiselevel
            '''
            result = self._values.get("noise_level")
            assert result is not None, "Required property 'noise_level' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricsConfigurationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trained_model_exports": "trainedModelExports",
            "trained_model_inference_jobs": "trainedModelInferenceJobs",
            "trained_models": "trainedModels",
        },
    )
    class PrivacyConfigurationPoliciesProperty:
        def __init__(
            self,
            *,
            trained_model_exports: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trained_model_inference_jobs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trained_models: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param trained_model_exports: 
            :param trained_model_inference_jobs: 
            :param trained_models: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                privacy_configuration_policies_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty(
                    trained_model_exports=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty(
                        files_to_export=["filesToExport"],
                        max_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty(
                            unit="unit",
                            value=123
                        )
                    ),
                    trained_model_inference_jobs=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty(
                        container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                            allowed_account_ids=["allowedAccountIds"],
                
                            # the properties below are optional
                            filter_pattern="filterPattern",
                            log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                entities_to_redact=["entitiesToRedact"],
                
                                # the properties below are optional
                                custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                    custom_data_identifiers=["customDataIdentifiers"]
                                )
                            ),
                            log_type="logType"
                        )],
                        max_output_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty(
                            unit="unit",
                            value=123
                        )
                    ),
                    trained_models=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty(
                        container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                            allowed_account_ids=["allowedAccountIds"],
                
                            # the properties below are optional
                            filter_pattern="filterPattern",
                            log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                entities_to_redact=["entitiesToRedact"],
                
                                # the properties below are optional
                                custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                    custom_data_identifiers=["customDataIdentifiers"]
                                )
                            ),
                            log_type="logType"
                        )],
                        container_metrics=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty(
                            noise_level="noiseLevel"
                        ),
                        max_artifact_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty(
                            unit="unit",
                            value=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cbd400f79261542d8fc4c160e0b7b1547cd6502f165a63f2aeae18b427f6709c)
                check_type(argname="argument trained_model_exports", value=trained_model_exports, expected_type=type_hints["trained_model_exports"])
                check_type(argname="argument trained_model_inference_jobs", value=trained_model_inference_jobs, expected_type=type_hints["trained_model_inference_jobs"])
                check_type(argname="argument trained_models", value=trained_models, expected_type=type_hints["trained_models"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if trained_model_exports is not None:
                self._values["trained_model_exports"] = trained_model_exports
            if trained_model_inference_jobs is not None:
                self._values["trained_model_inference_jobs"] = trained_model_inference_jobs
            if trained_models is not None:
                self._values["trained_models"] = trained_models

        @builtins.property
        def trained_model_exports(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelexports
            '''
            result = self._values.get("trained_model_exports")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty"]], result)

        @builtins.property
        def trained_model_inference_jobs(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodelinferencejobs
            '''
            result = self._values.get("trained_model_inference_jobs")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty"]], result)

        @builtins.property
        def trained_models(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfigurationpolicies-trainedmodels
            '''
            result = self._values.get("trained_models")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivacyConfigurationPoliciesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"policies": "policies"},
    )
    class PrivacyConfigurationProperty:
        def __init__(
            self,
            *,
            policies: typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param policies: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                privacy_configuration_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty(
                    policies=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty(
                        trained_model_exports=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty(
                            files_to_export=["filesToExport"],
                            max_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty(
                                unit="unit",
                                value=123
                            )
                        ),
                        trained_model_inference_jobs=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty(
                            container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                                allowed_account_ids=["allowedAccountIds"],
                
                                # the properties below are optional
                                filter_pattern="filterPattern",
                                log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                    entities_to_redact=["entitiesToRedact"],
                
                                    # the properties below are optional
                                    custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                        custom_data_identifiers=["customDataIdentifiers"]
                                    )
                                ),
                                log_type="logType"
                            )],
                            max_output_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty(
                                unit="unit",
                                value=123
                            )
                        ),
                        trained_models=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty(
                            container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                                allowed_account_ids=["allowedAccountIds"],
                
                                # the properties below are optional
                                filter_pattern="filterPattern",
                                log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                    entities_to_redact=["entitiesToRedact"],
                
                                    # the properties below are optional
                                    custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                        custom_data_identifiers=["customDataIdentifiers"]
                                    )
                                ),
                                log_type="logType"
                            )],
                            container_metrics=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty(
                                noise_level="noiseLevel"
                            ),
                            max_artifact_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty(
                                unit="unit",
                                value=123
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__169305b87437862d512e7568d12980c2168dc726cdf9632cce6c7fef7504934e)
                check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policies": policies,
            }

        @builtins.property
        def policies(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration-policies
            '''
            result = self._values.get("policies")
            assert result is not None, "Required property 'policies' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivacyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class TrainedModelArtifactMaxSizeProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''
            :param unit: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                trained_model_artifact_max_size_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__89024a2eadf8200bb8404a928567b47964457921868372c1e633310e728ed020)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrainedModelArtifactMaxSizeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"files_to_export": "filesToExport", "max_size": "maxSize"},
    )
    class TrainedModelExportsConfigurationPolicyProperty:
        def __init__(
            self,
            *,
            files_to_export: typing.Sequence[builtins.str],
            max_size: typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param files_to_export: 
            :param max_size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                trained_model_exports_configuration_policy_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty(
                    files_to_export=["filesToExport"],
                    max_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty(
                        unit="unit",
                        value=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4913e9be6a32e069755b3ca4083236fc25f338d4a5e2beea638de9ec9b8aa747)
                check_type(argname="argument files_to_export", value=files_to_export, expected_type=type_hints["files_to_export"])
                check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "files_to_export": files_to_export,
                "max_size": max_size,
            }

        @builtins.property
        def files_to_export(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-filestoexport
            '''
            result = self._values.get("files_to_export")
            assert result is not None, "Required property 'files_to_export' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def max_size(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsconfigurationpolicy-maxsize
            '''
            result = self._values.get("max_size")
            assert result is not None, "Required property 'max_size' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrainedModelExportsConfigurationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class TrainedModelExportsMaxSizeProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''
            :param unit: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                trained_model_exports_max_size_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fca5f74802d989477fae0c194b8e00db0cc46628fd33f6510e7c587aca08bc18)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrainedModelExportsMaxSizeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_logs": "containerLogs",
            "max_output_size": "maxOutputSize",
        },
    )
    class TrainedModelInferenceJobsConfigurationPolicyProperty:
        def __init__(
            self,
            *,
            container_logs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            max_output_size: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param container_logs: 
            :param max_output_size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                trained_model_inference_jobs_configuration_policy_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty(
                    container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                        allowed_account_ids=["allowedAccountIds"],
                
                        # the properties below are optional
                        filter_pattern="filterPattern",
                        log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                            entities_to_redact=["entitiesToRedact"],
                
                            # the properties below are optional
                            custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                custom_data_identifiers=["customDataIdentifiers"]
                            )
                        ),
                        log_type="logType"
                    )],
                    max_output_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty(
                        unit="unit",
                        value=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de366777da0a88ecb80544d0e9eba5f5e0e2ac02672ed77ec02ec56b53edd1e4)
                check_type(argname="argument container_logs", value=container_logs, expected_type=type_hints["container_logs"])
                check_type(argname="argument max_output_size", value=max_output_size, expected_type=type_hints["max_output_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_logs is not None:
                self._values["container_logs"] = container_logs
            if max_output_size is not None:
                self._values["max_output_size"] = max_output_size

        @builtins.property
        def container_logs(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-containerlogs
            '''
            result = self._values.get("container_logs")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty"]]]], result)

        @builtins.property
        def max_output_size(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencejobsconfigurationpolicy-maxoutputsize
            '''
            result = self._values.get("max_output_size")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrainedModelInferenceJobsConfigurationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class TrainedModelInferenceMaxOutputSizeProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''
            :param unit: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                trained_model_inference_max_output_size_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7061520f7e14394fa17e9f7e854292f1ccd5d6879e78660211f4451b7a2d1788)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelinferencemaxoutputsize-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrainedModelInferenceMaxOutputSizeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_logs": "containerLogs",
            "container_metrics": "containerMetrics",
            "max_artifact_size": "maxArtifactSize",
        },
    )
    class TrainedModelsConfigurationPolicyProperty:
        def __init__(
            self,
            *,
            container_logs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            container_metrics: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_artifact_size: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param container_logs: 
            :param container_metrics: 
            :param max_artifact_size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                trained_models_configuration_policy_property = cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty(
                    container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                        allowed_account_ids=["allowedAccountIds"],
                
                        # the properties below are optional
                        filter_pattern="filterPattern",
                        log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                            entities_to_redact=["entitiesToRedact"],
                
                            # the properties below are optional
                            custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                custom_data_identifiers=["customDataIdentifiers"]
                            )
                        ),
                        log_type="logType"
                    )],
                    container_metrics=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty(
                        noise_level="noiseLevel"
                    ),
                    max_artifact_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty(
                        unit="unit",
                        value=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dbad9b346056b9eeff87d26d1b24512d18861219bfdb711bfb734705c7501883)
                check_type(argname="argument container_logs", value=container_logs, expected_type=type_hints["container_logs"])
                check_type(argname="argument container_metrics", value=container_metrics, expected_type=type_hints["container_metrics"])
                check_type(argname="argument max_artifact_size", value=max_artifact_size, expected_type=type_hints["max_artifact_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_logs is not None:
                self._values["container_logs"] = container_logs
            if container_metrics is not None:
                self._values["container_metrics"] = container_metrics
            if max_artifact_size is not None:
                self._values["max_artifact_size"] = max_artifact_size

        @builtins.property
        def container_logs(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containerlogs
            '''
            result = self._values.get("container_logs")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty"]]]], result)

        @builtins.property
        def container_metrics(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-containermetrics
            '''
            result = self._values.get("container_metrics")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty"]], result)

        @builtins.property
        def max_artifact_size(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelsconfigurationpolicy-maxartifactsize
            '''
            result = self._values.get("max_artifact_size")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrainedModelsConfigurationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configured_model_algorithm_arn": "configuredModelAlgorithmArn",
        "membership_identifier": "membershipIdentifier",
        "name": "name",
        "description": "description",
        "privacy_configuration": "privacyConfiguration",
        "tags": "tags",
    },
)
class CfnConfiguredModelAlgorithmAssociationProps:
    def __init__(
        self,
        *,
        configured_model_algorithm_arn: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        privacy_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguredModelAlgorithmAssociation``.

        :param configured_model_algorithm_arn: 
        :param membership_identifier: 
        :param name: 
        :param description: 
        :param privacy_configuration: 
        :param tags: An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanroomsml as cleanroomsml
            
            cfn_configured_model_algorithm_association_props = cleanroomsml.CfnConfiguredModelAlgorithmAssociationProps(
                configured_model_algorithm_arn="configuredModelAlgorithmArn",
                membership_identifier="membershipIdentifier",
                name="name",
            
                # the properties below are optional
                description="description",
                privacy_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty(
                    policies=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty(
                        trained_model_exports=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty(
                            files_to_export=["filesToExport"],
                            max_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty(
                                unit="unit",
                                value=123
                            )
                        ),
                        trained_model_inference_jobs=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty(
                            container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                                allowed_account_ids=["allowedAccountIds"],
            
                                # the properties below are optional
                                filter_pattern="filterPattern",
                                log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                    entities_to_redact=["entitiesToRedact"],
            
                                    # the properties below are optional
                                    custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                        custom_data_identifiers=["customDataIdentifiers"]
                                    )
                                ),
                                log_type="logType"
                            )],
                            max_output_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty(
                                unit="unit",
                                value=123
                            )
                        ),
                        trained_models=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty(
                            container_logs=[cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty(
                                allowed_account_ids=["allowedAccountIds"],
            
                                # the properties below are optional
                                filter_pattern="filterPattern",
                                log_redaction_configuration=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty(
                                    entities_to_redact=["entitiesToRedact"],
            
                                    # the properties below are optional
                                    custom_entity_config=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty(
                                        custom_data_identifiers=["customDataIdentifiers"]
                                    )
                                ),
                                log_type="logType"
                            )],
                            container_metrics=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty(
                                noise_level="noiseLevel"
                            ),
                            max_artifact_size=cleanroomsml.CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty(
                                unit="unit",
                                value=123
                            )
                        )
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b4b3cd92b818e3351d55fc0aef8aa822e344f046e6128a3609fd0cb332a274)
            check_type(argname="argument configured_model_algorithm_arn", value=configured_model_algorithm_arn, expected_type=type_hints["configured_model_algorithm_arn"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument privacy_configuration", value=privacy_configuration, expected_type=type_hints["privacy_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn,
            "membership_identifier": membership_identifier,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if privacy_configuration is not None:
            self._values["privacy_configuration"] = privacy_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configured_model_algorithm_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-configuredmodelalgorithmarn
        '''
        result = self._values.get("configured_model_algorithm_arn")
        assert result is not None, "Required property 'configured_model_algorithm_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def privacy_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration
        '''
        result = self._values.get("privacy_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html#cfn-cleanroomsml-configuredmodelalgorithmassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfiguredModelAlgorithmAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnConfiguredModelAlgorithmProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_arn": "roleArn",
        "description": "description",
        "inference_container_config": "inferenceContainerConfig",
        "kms_key_arn": "kmsKeyArn",
        "tags": "tags",
        "training_container_config": "trainingContainerConfig",
    },
)
class CfnConfiguredModelAlgorithmProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        inference_container_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        training_container_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfiguredModelAlgorithm.ContainerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguredModelAlgorithm``.

        :param name: 
        :param role_arn: 
        :param description: 
        :param inference_container_config: 
        :param kms_key_arn: 
        :param tags: An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm.
        :param training_container_config: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanroomsml as cleanroomsml
            
            cfn_configured_model_algorithm_props = cleanroomsml.CfnConfiguredModelAlgorithmProps(
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                description="description",
                inference_container_config=cleanroomsml.CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty(
                    image_uri="imageUri"
                ),
                kms_key_arn="kmsKeyArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                training_container_config=cleanroomsml.CfnConfiguredModelAlgorithm.ContainerConfigProperty(
                    image_uri="imageUri",
            
                    # the properties below are optional
                    arguments=["arguments"],
                    entrypoint=["entrypoint"],
                    metric_definitions=[cleanroomsml.CfnConfiguredModelAlgorithm.MetricDefinitionProperty(
                        name="name",
                        regex="regex"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8630df9152fcd414f9145fb10a14422c79abb7df8b8b60682f7b9630d74ce2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument inference_container_config", value=inference_container_config, expected_type=type_hints["inference_container_config"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument training_container_config", value=training_container_config, expected_type=type_hints["training_container_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if inference_container_config is not None:
            self._values["inference_container_config"] = inference_container_config
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if tags is not None:
            self._values["tags"] = tags
        if training_container_config is not None:
            self._values["training_container_config"] = training_container_config

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inference_container_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig
        '''
        result = self._values.get("inference_container_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty"]], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An arbitrary set of tags (key-value pairs) for this cleanrooms-ml configured model algorithm.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def training_container_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.ContainerConfigProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-configuredmodelalgorithm.html#cfn-cleanroomsml-configuredmodelalgorithm-trainingcontainerconfig
        '''
        result = self._values.get("training_container_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfiguredModelAlgorithm.ContainerConfigProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfiguredModelAlgorithmProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITrainingDatasetRef_e0f12c42, _ITaggableV2_4e6798f8)
class CfnTrainingDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset",
):
    '''Defines the information necessary to create a training dataset.

    In Clean Rooms ML, the ``TrainingDataset`` is metadata that points to a Glue table, which is read only during ``AudienceModel`` creation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html
    :cloudformationResource: AWS::CleanRoomsML::TrainingDataset
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanroomsml as cleanroomsml
        
        cfn_training_dataset = cleanroomsml.CfnTrainingDataset(self, "MyCfnTrainingDataset",
            name="name",
            role_arn="roleArn",
            training_data=[cleanroomsml.CfnTrainingDataset.DatasetProperty(
                input_config=cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                    data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                        glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                            database_name="databaseName",
                            table_name="tableName",
        
                            # the properties below are optional
                            catalog_id="catalogId"
                        )
                    ),
                    schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                        column_name="columnName",
                        column_types=["columnTypes"]
                    )]
                ),
                type="type"
            )],
        
            # the properties below are optional
            description="description",
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
        name: builtins.str,
        role_arn: builtins.str,
        training_data: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTrainingDataset.DatasetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CleanRoomsML::TrainingDataset``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the training dataset.
        :param role_arn: The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset. Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an ``AccessDeniedException`` error.
        :param training_data: An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.
        :param description: The description of the training dataset.
        :param tags: The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. The following basic restrictions apply to tags: - Maximum number of tags per resource - 50. - For each resource, each tag key must be unique, and each tag key can have only one value. - Maximum key length - 128 Unicode characters in UTF-8. - Maximum value length - 256 Unicode characters in UTF-8. - If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : /
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__038c489df01bd94323363a194424fbe900aac226689cefa852a1f05e78d3bf55)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrainingDatasetProps(
            name=name,
            role_arn=role_arn,
            training_data=training_data,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTrainingDataset")
    @builtins.classmethod
    def arn_for_training_dataset(
        cls,
        resource: "_ITrainingDatasetRef_e0f12c42",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9550e7cc74f3a3279d5dadd02f957b89e1799245db85d81f550168acf07d3e4e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTrainingDataset", [resource]))

    @jsii.member(jsii_name="isCfnTrainingDataset")
    @builtins.classmethod
    def is_cfn_training_dataset(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTrainingDataset.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78cf47e6a5adfa0a4a705f563e7416bb97dce81c2248e22f49d4a1a299157dfd)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTrainingDataset", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9028b0a86b67eeece54985e3b32f00cd36517f094fd9d81836504af70a287532)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a85a48fae07d74ac7e0c59e9b85c0b8f0441d9c407bfe3085fc7206894045b9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the training dataset.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTrainingDatasetArn")
    def attr_training_dataset_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the training dataset.

        :cloudformationAttribute: TrainingDatasetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrainingDatasetArn"))

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
    @jsii.member(jsii_name="trainingDatasetRef")
    def training_dataset_ref(self) -> "_TrainingDatasetReference_d53f15ee":
        '''A reference to a TrainingDataset resource.'''
        return typing.cast("_TrainingDatasetReference_d53f15ee", jsii.get(self, "trainingDatasetRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the training dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494f55ff0a6978c4165f5d363cd591484cf83133d7818ceede53e907d0c936c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dd3ad8ea8435bdf184f933dfcef7f130800d9b2a40eae3e2318bb9c9a09e4e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trainingData")
    def training_data(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetProperty"]]]:
        '''An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetProperty"]]], jsii.get(self, "trainingData"))

    @training_data.setter
    def training_data(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1942d638c495e8ce078a6ab83bfe20a886d72c3fb786c501cd684c593146ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trainingData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the training dataset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1072b383b65b621f0fc0b4b9426fe6c12552a36489cacafc4d1d23d46a07fc1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The optional metadata that you apply to the resource to help you categorize and organize them.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b6f50dc896f0f57ebfe75a224d400087cca80791cfac1f7d4afe9d1151d747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "column_types": "columnTypes"},
    )
    class ColumnSchemaProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            column_types: typing.Sequence[builtins.str],
        ) -> None:
            '''Metadata for a column.

            :param column_name: The name of a column.
            :param column_types: The data type of column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-columnschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                column_schema_property = cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                    column_name="columnName",
                    column_types=["columnTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15de5d6643671de2a88fad9d9afaad1a33eaa500023772c59a4b9d5f2c0e5ca5)
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
                check_type(argname="argument column_types", value=column_types, expected_type=type_hints["column_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_name": column_name,
                "column_types": column_types,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''The name of a column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-columnschema.html#cfn-cleanroomsml-trainingdataset-columnschema-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_types(self) -> typing.List[builtins.str]:
            '''The data type of column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-columnschema.html#cfn-cleanroomsml-trainingdataset-columnschema-columntypes
            '''
            result = self._values.get("column_types")
            assert result is not None, "Required property 'column_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.DataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"glue_data_source": "glueDataSource"},
    )
    class DataSourceProperty:
        def __init__(
            self,
            *,
            glue_data_source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTrainingDataset.GlueDataSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines information about the Glue data source that contains the training data.

            :param glue_data_source: A GlueDataSource object that defines the catalog ID, database name, and table name for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                data_source_property = cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                    glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                        database_name="databaseName",
                        table_name="tableName",
                
                        # the properties below are optional
                        catalog_id="catalogId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d605167b33212652a5badb6d4db40ca8e474bafedbd9c8b5354317bb8e696966)
                check_type(argname="argument glue_data_source", value=glue_data_source, expected_type=type_hints["glue_data_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "glue_data_source": glue_data_source,
            }

        @builtins.property
        def glue_data_source(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.GlueDataSourceProperty"]:
            '''A GlueDataSource object that defines the catalog ID, database name, and table name for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasource.html#cfn-cleanroomsml-trainingdataset-datasource-gluedatasource
            '''
            result = self._values.get("glue_data_source")
            assert result is not None, "Required property 'glue_data_source' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.GlueDataSourceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"data_source": "dataSource", "schema": "schema"},
    )
    class DatasetInputConfigProperty:
        def __init__(
            self,
            *,
            data_source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTrainingDataset.DataSourceProperty", typing.Dict[builtins.str, typing.Any]]],
            schema: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTrainingDataset.ColumnSchemaProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Defines the Glue data source and schema mapping information.

            :param data_source: A DataSource object that specifies the Glue data source for the training data.
            :param schema: The schema information for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                dataset_input_config_property = cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                    data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                        glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                            database_name="databaseName",
                            table_name="tableName",
                
                            # the properties below are optional
                            catalog_id="catalogId"
                        )
                    ),
                    schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                        column_name="columnName",
                        column_types=["columnTypes"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab93d97f5b26accc73a8c37bd47a1cbf272dd2d33e0ff1a267931c622072b676)
                check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source": data_source,
                "schema": schema,
            }

        @builtins.property
        def data_source(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DataSourceProperty"]:
            '''A DataSource object that specifies the Glue data source for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html#cfn-cleanroomsml-trainingdataset-datasetinputconfig-datasource
            '''
            result = self._values.get("data_source")
            assert result is not None, "Required property 'data_source' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DataSourceProperty"], result)

        @builtins.property
        def schema(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.ColumnSchemaProperty"]]]:
            '''The schema information for the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-datasetinputconfig.html#cfn-cleanroomsml-trainingdataset-datasetinputconfig-schema
            '''
            result = self._values.get("schema")
            assert result is not None, "Required property 'schema' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.ColumnSchemaProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetInputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.DatasetProperty",
        jsii_struct_bases=[],
        name_mapping={"input_config": "inputConfig", "type": "type"},
    )
    class DatasetProperty:
        def __init__(
            self,
            *,
            input_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTrainingDataset.DatasetInputConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''Defines where the training dataset is located, what type of data it contains, and how to access the data.

            :param input_config: A DatasetInputConfig object that defines the data source and schema mapping.
            :param type: What type of information is found in the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-dataset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                dataset_property = cleanroomsml.CfnTrainingDataset.DatasetProperty(
                    input_config=cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                        data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                            glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                                database_name="databaseName",
                                table_name="tableName",
                
                                # the properties below are optional
                                catalog_id="catalogId"
                            )
                        ),
                        schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                            column_name="columnName",
                            column_types=["columnTypes"]
                        )]
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__38a3a37ec245bf1288fe1fb7ea7c3d9b1d3b4642f41f30639da52a4dca9bd86c)
                check_type(argname="argument input_config", value=input_config, expected_type=type_hints["input_config"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_config": input_config,
                "type": type,
            }

        @builtins.property
        def input_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetInputConfigProperty"]:
            '''A DatasetInputConfig object that defines the data source and schema mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-dataset.html#cfn-cleanroomsml-trainingdataset-dataset-inputconfig
            '''
            result = self._values.get("input_config")
            assert result is not None, "Required property 'input_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetInputConfigProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''What type of information is found in the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-dataset.html#cfn-cleanroomsml-trainingdataset-dataset-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "table_name": "tableName",
            "catalog_id": "catalogId",
        },
    )
    class GlueDataSourceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
            catalog_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the Glue data source that contains the training data.

            :param database_name: The Glue database that contains the training data.
            :param table_name: The Glue table that contains the training data.
            :param catalog_id: The Glue catalog that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanroomsml as cleanroomsml
                
                glue_data_source_property = cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                    database_name="databaseName",
                    table_name="tableName",
                
                    # the properties below are optional
                    catalog_id="catalogId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__960bc53c7c406ea248f393051fd58abbf5074d22e0eb6439f849d7558cb02ffd)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The Glue database that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html#cfn-cleanroomsml-trainingdataset-gluedatasource-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The Glue table that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html#cfn-cleanroomsml-trainingdataset-gluedatasource-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The Glue catalog that contains the training data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanroomsml-trainingdataset-gluedatasource.html#cfn-cleanroomsml-trainingdataset-gluedatasource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanroomsml.CfnTrainingDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_arn": "roleArn",
        "training_data": "trainingData",
        "description": "description",
        "tags": "tags",
    },
)
class CfnTrainingDatasetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        training_data: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTrainingDataset.DatasetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrainingDataset``.

        :param name: The name of the training dataset.
        :param role_arn: The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset. Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an ``AccessDeniedException`` error.
        :param training_data: An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.
        :param description: The description of the training dataset.
        :param tags: The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. The following basic restrictions apply to tags: - Maximum number of tags per resource - 50. - For each resource, each tag key must be unique, and each tag key can have only one value. - Maximum key length - 128 Unicode characters in UTF-8. - Maximum value length - 256 Unicode characters in UTF-8. - If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanroomsml as cleanroomsml
            
            cfn_training_dataset_props = cleanroomsml.CfnTrainingDatasetProps(
                name="name",
                role_arn="roleArn",
                training_data=[cleanroomsml.CfnTrainingDataset.DatasetProperty(
                    input_config=cleanroomsml.CfnTrainingDataset.DatasetInputConfigProperty(
                        data_source=cleanroomsml.CfnTrainingDataset.DataSourceProperty(
                            glue_data_source=cleanroomsml.CfnTrainingDataset.GlueDataSourceProperty(
                                database_name="databaseName",
                                table_name="tableName",
            
                                # the properties below are optional
                                catalog_id="catalogId"
                            )
                        ),
                        schema=[cleanroomsml.CfnTrainingDataset.ColumnSchemaProperty(
                            column_name="columnName",
                            column_types=["columnTypes"]
                        )]
                    ),
                    type="type"
                )],
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a83ce04ef3c373a0c189c16bb2a7e23aea1fda52268a69a4e97e560d76564547)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument training_data", value=training_data, expected_type=type_hints["training_data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "role_arn": role_arn,
            "training_data": training_data,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the training dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the ``dataSource`` field of each dataset.

        Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an ``AccessDeniedException`` error.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def training_data(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetProperty"]]]:
        '''An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema.

        You must provide a role that has read access to these tables.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-trainingdata
        '''
        result = self._values.get("training_data")
        assert result is not None, "Required property 'training_data' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTrainingDataset.DatasetProperty"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the training dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The optional metadata that you apply to the resource to help you categorize and organize them.

        Each tag consists of a key and an optional value, both of which you define.

        The following basic restrictions apply to tags:

        - Maximum number of tags per resource - 50.
        - For each resource, each tag key must be unique, and each tag key can have only one value.
        - Maximum key length - 128 Unicode characters in UTF-8.
        - Maximum value length - 256 Unicode characters in UTF-8.
        - If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : /

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanroomsml-trainingdataset.html#cfn-cleanroomsml-trainingdataset-tags
        ::

        .

        - Tag keys and values are case sensitive.
        - Do not use ``aws:`` , ``AWS:`` , or any upper or lowercase combination of such as a prefix for keys as it is reserved. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has ``aws`` as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of ``aws`` do not count against your tags per resource limit.
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrainingDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfiguredModelAlgorithm",
    "CfnConfiguredModelAlgorithmAssociation",
    "CfnConfiguredModelAlgorithmAssociationProps",
    "CfnConfiguredModelAlgorithmProps",
    "CfnTrainingDataset",
    "CfnTrainingDatasetProps",
]

publication.publish()

def _typecheckingstub__6d9add5e5fc7b05d2aa8b862a0b3f77721f43df75943badf1e52b1b8c11b661f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    inference_container_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    training_container_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithm.ContainerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe92be2373e1b28b447ac31793dbefd680b4163dd1c777ba2c309b2cd490a2d(
    resource: _IConfiguredModelAlgorithmRef_c000ba6b,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58172d7c5bba2efab8369c3c9b9d2892e8e3ef50d1ce32e7b1c640d267b33a07(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__101100b1e573c15641233745c75f387f2f906f34b6df888bcd29bf79633a8239(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__403ba867d7d1404bdf36baa4c2b3dcd5d1264c6914f5aac5fbc3ab0fe0f98c1c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84fb62060d27ca3dad20b96f63aa1a385fd6527599eee76d7638f98e79daf6f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092e7369580c2f623975b01d4cab03e9c7197cd72d0d3895deae863689c4f248(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cf7cbf05f79b61ec2c8bbdc62eeebca87800fe721f2dec8affb4867d42e4ac5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921d9695e86808b47495e9acd680f91eaa50034525dcec342e1d8fc730a30430(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b07aee4401db10797bdc20d2ff55e198cb0f54972f1dfa9058913c2b5bf44a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d3e6447ee2429ba914a52ccf1133c099d3f81703c4ce77859f7dd4f50b978a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6881177ba8c4e4d4c7fabe1b3635afa39a446f6d7e1563f4fb879f52f5fb663d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfiguredModelAlgorithm.ContainerConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12dd4ea50ae8c8c1f4153da75226b7aab6c9684ff49f6539afa13aadab810017(
    *,
    image_uri: builtins.str,
    arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
    entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
    metric_definitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithm.MetricDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d561138399fe485c7f8c1dab5da8276fb4f9104888afc0211c73814871f4db6(
    *,
    image_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbdc32e8e4e20cd09c57719079ab7392669c441363bb3abbe8820e7d46dd543(
    *,
    name: builtins.str,
    regex: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a034d9eda51309ce6906a92c52fe385af754cad01c4669704e95371412aa4c82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configured_model_algorithm_arn: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    privacy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cddf6593a701a4d13683248bc56f69d821c1bf4fc0ccef76963a4b87cad49638(
    resource: _IConfiguredModelAlgorithmAssociationRef_5d6df5cb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ef00d95c26cc59c2ba724cb02070915f111031775e7ae56cdc41a3f820eeb2(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef2ecca8abcf092dfbf6e68a0f7acda79451843ec6255c9dbd8875c29d812ddd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc73243f20b7225a7b48092a7597b990d086b659b922246a618290bac56db7ed(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acee9b91f31a6a5fb74a362703ae71ac574e762f84a7552fd4ffbf05f3f713b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69080d38e1f1bb9347d20cdb2de93f048e22f21654d45670e586dec664950498(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9798dbeaa85a39f5a37c80e1c3a3a0f30330711eb84e7a055c610f819c384e3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2353683a85d08f04391a843c9b451c7da3479829cf55530f44efe6bd03c0a458(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df97e8aaaffba77a0d74c07b40612ccaa090c972cf24969395623262e80537b7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca97080fb41ace7427954bf826084b395f9f2457ef95662151d1aab7231a5b0c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1710dcf96d19e57f9f6b1f22b1acb55122da536d5ca24e473b242ce21a52399b(
    *,
    custom_data_identifiers: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c103dcc9627e880f31873ee728f160d0ccf0209bd4c2ead6ae3da609454a5c1d(
    *,
    entities_to_redact: typing.Sequence[builtins.str],
    custom_entity_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.CustomEntityConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c620013d45f62be0ac95f38666412f20f488540d33211aac358683a234dac6d3(
    *,
    allowed_account_ids: typing.Sequence[builtins.str],
    filter_pattern: typing.Optional[builtins.str] = None,
    log_redaction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.LogRedactionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f1b429531f0f1bf7945804821fec24222684078b3f82681f068a8a1511b66e(
    *,
    noise_level: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd400f79261542d8fc4c160e0b7b1547cd6502f165a63f2aeae18b427f6709c(
    *,
    trained_model_exports: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsConfigurationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trained_model_inference_jobs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceJobsConfigurationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trained_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.TrainedModelsConfigurationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169305b87437862d512e7568d12980c2168dc726cdf9632cce6c7fef7504934e(
    *,
    policies: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationPoliciesProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89024a2eadf8200bb8404a928567b47964457921868372c1e633310e728ed020(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4913e9be6a32e069755b3ca4083236fc25f338d4a5e2beea638de9ec9b8aa747(
    *,
    files_to_export: typing.Sequence[builtins.str],
    max_size: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.TrainedModelExportsMaxSizeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca5f74802d989477fae0c194b8e00db0cc46628fd33f6510e7c587aca08bc18(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de366777da0a88ecb80544d0e9eba5f5e0e2ac02672ed77ec02ec56b53edd1e4(
    *,
    container_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    max_output_size: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.TrainedModelInferenceMaxOutputSizeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7061520f7e14394fa17e9f7e854292f1ccd5d6879e78660211f4451b7a2d1788(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbad9b346056b9eeff87d26d1b24512d18861219bfdb711bfb734705c7501883(
    *,
    container_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.LogsConfigurationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    container_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.MetricsConfigurationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_artifact_size: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.TrainedModelArtifactMaxSizeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b4b3cd92b818e3351d55fc0aef8aa822e344f046e6128a3609fd0cb332a274(
    *,
    configured_model_algorithm_arn: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    privacy_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithmAssociation.PrivacyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8630df9152fcd414f9145fb10a14422c79abb7df8b8b60682f7b9630d74ce2(
    *,
    name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    inference_container_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithm.InferenceContainerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    training_container_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredModelAlgorithm.ContainerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__038c489df01bd94323363a194424fbe900aac226689cefa852a1f05e78d3bf55(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    role_arn: builtins.str,
    training_data: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9550e7cc74f3a3279d5dadd02f957b89e1799245db85d81f550168acf07d3e4e(
    resource: _ITrainingDatasetRef_e0f12c42,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78cf47e6a5adfa0a4a705f563e7416bb97dce81c2248e22f49d4a1a299157dfd(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9028b0a86b67eeece54985e3b32f00cd36517f094fd9d81836504af70a287532(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a85a48fae07d74ac7e0c59e9b85c0b8f0441d9c407bfe3085fc7206894045b9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494f55ff0a6978c4165f5d363cd591484cf83133d7818ceede53e907d0c936c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd3ad8ea8435bdf184f933dfcef7f130800d9b2a40eae3e2318bb9c9a09e4e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1942d638c495e8ce078a6ab83bfe20a886d72c3fb786c501cd684c593146ac(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTrainingDataset.DatasetProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1072b383b65b621f0fc0b4b9426fe6c12552a36489cacafc4d1d23d46a07fc1f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b6f50dc896f0f57ebfe75a224d400087cca80791cfac1f7d4afe9d1151d747(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15de5d6643671de2a88fad9d9afaad1a33eaa500023772c59a4b9d5f2c0e5ca5(
    *,
    column_name: builtins.str,
    column_types: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d605167b33212652a5badb6d4db40ca8e474bafedbd9c8b5354317bb8e696966(
    *,
    glue_data_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.GlueDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab93d97f5b26accc73a8c37bd47a1cbf272dd2d33e0ff1a267931c622072b676(
    *,
    data_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    schema: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.ColumnSchemaProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a3a37ec245bf1288fe1fb7ea7c3d9b1d3b4642f41f30639da52a4dca9bd86c(
    *,
    input_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetInputConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960bc53c7c406ea248f393051fd58abbf5074d22e0eb6439f849d7558cb02ffd(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
    catalog_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a83ce04ef3c373a0c189c16bb2a7e23aea1fda52268a69a4e97e560d76564547(
    *,
    name: builtins.str,
    role_arn: builtins.str,
    training_data: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrainingDataset.DatasetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

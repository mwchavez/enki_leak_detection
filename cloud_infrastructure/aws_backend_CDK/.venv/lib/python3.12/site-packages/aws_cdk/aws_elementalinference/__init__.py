r'''
# AWS::ElementalInference Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_elementalinference as elementalinference
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ElementalInference construct libraries](https://constructs.dev/search?q=elementalinference)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ElementalInference resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElementalInference.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ElementalInference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElementalInference.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_elementalinference import (
    FeedReference as _FeedReference_81ef993e, IFeedRef as _IFeedRef_98e7be84
)


@jsii.implements(_IInspectable_c2943556, _IFeedRef_98e7be84, _ITaggableV2_4e6798f8)
class CfnFeed(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed",
):
    '''Represents a feed that receives media for inference processing.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html
    :cloudformationResource: AWS::ElementalInference::Feed
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elementalinference as elementalinference
        
        # cropping: Any
        
        cfn_feed = elementalinference.CfnFeed(self, "MyCfnFeed",
            name="name",
            outputs=[elementalinference.CfnFeed.GetOutputProperty(
                name="name",
                output_config=elementalinference.CfnFeed.OutputConfigProperty(
                    clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                        callback_metadata="callbackMetadata"
                    ),
                    cropping=cropping
                ),
                status="status",
        
                # the properties below are optional
                description="description"
            )],
        
            # the properties below are optional
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        outputs: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFeed.GetOutputProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElementalInference::Feed``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: 
        :param outputs: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__086c1fcdd22f4573bbf9e5858e698d4a67c6e5f5679291a457c0399ac83d35d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFeedProps(name=name, outputs=outputs, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFeed")
    @builtins.classmethod
    def arn_for_feed(cls, resource: "_IFeedRef_98e7be84") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0e3705d6c009d3ad14dba82dc352718235a5afb9e6f07c2dfec5360885f5b8f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFeed", [resource]))

    @jsii.member(jsii_name="isCfnFeed")
    @builtins.classmethod
    def is_cfn_feed(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFeed.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9717524a84639953c97d1079ee02198d0c70203475e0a48c5a4ff3f60d192471)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFeed", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a16b23304f2dde726d178cff21ddda9392321b31d4d71b68e4b79cc737bc01da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cc422f59d4b34fb0f9a25421f746cad0611bf7d1f39c981e4e55506b7df2ef3)
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
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDataEndpoints")
    def attr_data_endpoints(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: DataEndpoints
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDataEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="feedRef")
    def feed_ref(self) -> "_FeedReference_81ef993e":
        '''A reference to a Feed resource.'''
        return typing.cast("_FeedReference_81ef993e", jsii.get(self, "feedRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d75eaca9c34446747fb20283badafe891b40a3fba2ee34a519fcaf304f16dd07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFeed.GetOutputProperty"]]]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFeed.GetOutputProperty"]]], jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFeed.GetOutputProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5c56fe45498c7c2ef7666681ed87b6d6305ad4ea8b27076706113d35691a314)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e0bc362d8a7be8bdb4db49c0fb751ca65a9bf66da03ffdc2fb00af3e5efb90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.ClippingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"callback_metadata": "callbackMetadata"},
    )
    class ClippingConfigProperty:
        def __init__(
            self,
            *,
            callback_metadata: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param callback_metadata: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-clippingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                clipping_config_property = elementalinference.CfnFeed.ClippingConfigProperty(
                    callback_metadata="callbackMetadata"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6a4ba370813bfb444bc9ceafafb712ea485e1284fa02f399aac4531d0015262)
                check_type(argname="argument callback_metadata", value=callback_metadata, expected_type=type_hints["callback_metadata"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if callback_metadata is not None:
                self._values["callback_metadata"] = callback_metadata

        @builtins.property
        def callback_metadata(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-clippingconfig.html#cfn-elementalinference-feed-clippingconfig-callbackmetadata
            '''
            result = self._values.get("callback_metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClippingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.GetOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "output_config": "outputConfig",
            "status": "status",
            "description": "description",
        },
    )
    class GetOutputProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            output_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFeed.OutputConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            status: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: 
            :param output_config: 
            :param status: 
            :param description: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                # cropping: Any
                
                get_output_property = elementalinference.CfnFeed.GetOutputProperty(
                    name="name",
                    output_config=elementalinference.CfnFeed.OutputConfigProperty(
                        clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                            callback_metadata="callbackMetadata"
                        ),
                        cropping=cropping
                    ),
                    status="status",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7c0accadaf3abd8820d59ff8ea7b283716805039f5029d7aafb4b9c614a96cb)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "output_config": output_config,
                "status": status,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnFeed.OutputConfigProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-outputconfig
            '''
            result = self._values.get("output_config")
            assert result is not None, "Required property 'output_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFeed.OutputConfigProperty"], result)

        @builtins.property
        def status(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-getoutput.html#cfn-elementalinference-feed-getoutput-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GetOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeed.OutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"clipping": "clipping", "cropping": "cropping"},
    )
    class OutputConfigProperty:
        def __init__(
            self,
            *,
            clipping: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFeed.ClippingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cropping: typing.Any = None,
        ) -> None:
            '''
            :param clipping: 
            :param cropping: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_elementalinference as elementalinference
                
                # cropping: Any
                
                output_config_property = elementalinference.CfnFeed.OutputConfigProperty(
                    clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                        callback_metadata="callbackMetadata"
                    ),
                    cropping=cropping
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2903ddb4ce42c6a1ffd01fed7c6276e891d4bc19ee8d5416c7af548c5968e928)
                check_type(argname="argument clipping", value=clipping, expected_type=type_hints["clipping"])
                check_type(argname="argument cropping", value=cropping, expected_type=type_hints["cropping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if clipping is not None:
                self._values["clipping"] = clipping
            if cropping is not None:
                self._values["cropping"] = cropping

        @builtins.property
        def clipping(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFeed.ClippingConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html#cfn-elementalinference-feed-outputconfig-clipping
            '''
            result = self._values.get("clipping")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFeed.ClippingConfigProperty"]], result)

        @builtins.property
        def cropping(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elementalinference-feed-outputconfig.html#cfn-elementalinference-feed-outputconfig-cropping
            '''
            result = self._values.get("cropping")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_elementalinference.CfnFeedProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "outputs": "outputs", "tags": "tags"},
)
class CfnFeedProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        outputs: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFeed.GetOutputProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFeed``.

        :param name: 
        :param outputs: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_elementalinference as elementalinference
            
            # cropping: Any
            
            cfn_feed_props = elementalinference.CfnFeedProps(
                name="name",
                outputs=[elementalinference.CfnFeed.GetOutputProperty(
                    name="name",
                    output_config=elementalinference.CfnFeed.OutputConfigProperty(
                        clipping=elementalinference.CfnFeed.ClippingConfigProperty(
                            callback_metadata="callbackMetadata"
                        ),
                        cropping=cropping
                    ),
                    status="status",
            
                    # the properties below are optional
                    description="description"
                )],
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20c116466754eabef3c4516fae5bfe05f1720d03f7fdf1d8e53dfff7e268dd1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "outputs": outputs,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFeed.GetOutputProperty"]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-outputs
        '''
        result = self._values.get("outputs")
        assert result is not None, "Required property 'outputs' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFeed.GetOutputProperty"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elementalinference-feed.html#cfn-elementalinference-feed-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFeedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFeed",
    "CfnFeedProps",
]

publication.publish()

def _typecheckingstub__086c1fcdd22f4573bbf9e5858e698d4a67c6e5f5679291a457c0399ac83d35d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    outputs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeed.GetOutputProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e3705d6c009d3ad14dba82dc352718235a5afb9e6f07c2dfec5360885f5b8f(
    resource: _IFeedRef_98e7be84,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9717524a84639953c97d1079ee02198d0c70203475e0a48c5a4ff3f60d192471(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16b23304f2dde726d178cff21ddda9392321b31d4d71b68e4b79cc737bc01da(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc422f59d4b34fb0f9a25421f746cad0611bf7d1f39c981e4e55506b7df2ef3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75eaca9c34446747fb20283badafe891b40a3fba2ee34a519fcaf304f16dd07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c56fe45498c7c2ef7666681ed87b6d6305ad4ea8b27076706113d35691a314(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeed.GetOutputProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e0bc362d8a7be8bdb4db49c0fb751ca65a9bf66da03ffdc2fb00af3e5efb90(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a4ba370813bfb444bc9ceafafb712ea485e1284fa02f399aac4531d0015262(
    *,
    callback_metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c0accadaf3abd8820d59ff8ea7b283716805039f5029d7aafb4b9c614a96cb(
    *,
    name: builtins.str,
    output_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeed.OutputConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    status: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2903ddb4ce42c6a1ffd01fed7c6276e891d4bc19ee8d5416c7af548c5968e928(
    *,
    clipping: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeed.ClippingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cropping: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20c116466754eabef3c4516fae5bfe05f1720d03f7fdf1d8e53dfff7e268dd1(
    *,
    name: builtins.str,
    outputs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeed.GetOutputProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

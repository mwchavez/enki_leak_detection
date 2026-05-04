r'''
# AWS::Braket Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_braket as braket
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Braket construct libraries](https://constructs.dev/search?q=braket)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Braket resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Braket.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Braket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Braket.html).

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
from ..interfaces.aws_braket import (
    ISpendingLimitRef as _ISpendingLimitRef_c3305421,
    SpendingLimitReference as _SpendingLimitReference_fac52b6f,
)


@jsii.implements(_IInspectable_c2943556, _ISpendingLimitRef_c3305421, _ITaggableV2_4e6798f8)
class CfnSpendingLimit(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_braket.CfnSpendingLimit",
):
    '''Creates a spending limit for a specified quantum device.

    Spending limits help you control costs by setting maximum amounts that can be spent on quantum computing tasks within a specified time period.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-braket-spendinglimit.html
    :cloudformationResource: AWS::Braket::SpendingLimit
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_braket as braket
        
        cfn_spending_limit = braket.CfnSpendingLimit(self, "MyCfnSpendingLimit",
            device_arn="deviceArn",
            spending_limit="spendingLimit",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            time_period=braket.CfnSpendingLimit.TimePeriodProperty(
                end_at="endAt",
                start_at="startAt"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        device_arn: builtins.str,
        spending_limit: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        time_period: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSpendingLimit.TimePeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Braket::SpendingLimit``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param device_arn: The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.
        :param spending_limit: The maximum amount that can be spent on the specified device, in USD.
        :param tags: The tags to apply to the spending limit.
        :param time_period: Defines a time range for spending limits, specifying when the limit is active.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c35c7c6e8ca9e275973dad9bd6ceae11c5bfb55d638d0828c196300ab9d14fe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSpendingLimitProps(
            device_arn=device_arn,
            spending_limit=spending_limit,
            tags=tags,
            time_period=time_period,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSpendingLimit")
    @builtins.classmethod
    def arn_for_spending_limit(
        cls,
        resource: "_ISpendingLimitRef_c3305421",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f300f7aff60a3c9cdaf9438a696c90b73bf3848c152ccbfa1b2299361415e51)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSpendingLimit", [resource]))

    @jsii.member(jsii_name="isCfnSpendingLimit")
    @builtins.classmethod
    def is_cfn_spending_limit(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSpendingLimit.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb08e44816f639c1366677c788c1c7663da3bdeab949fa853e759c018c68363)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSpendingLimit", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7836aabd9049cb0890dcfd861d30fc4a91909f9c9bddfb04418c2e8935fe92f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8efc42070409da980e6fb943ee279a64a55bd7c598d8d5d7a13cf241d172b267)
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
        '''The date and time when the spending limit was created, in ISO 8601 format.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrQueuedSpend")
    def attr_queued_spend(self) -> builtins.str:
        '''The amount currently queued for spending on the device, in USD.

        :cloudformationAttribute: QueuedSpend
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueuedSpend"))

    @builtins.property
    @jsii.member(jsii_name="attrSpendingLimitArn")
    def attr_spending_limit_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that uniquely identifies the spending limit.

        :cloudformationAttribute: SpendingLimitArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSpendingLimitArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalSpend")
    def attr_total_spend(self) -> builtins.str:
        '''The total amount spent on the device so far during the current time period, in USD.

        :cloudformationAttribute: TotalSpend
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTotalSpend"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The date and time when the spending limit was last modified, in ISO 8601 format.

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
    @jsii.member(jsii_name="spendingLimitRef")
    def spending_limit_ref(self) -> "_SpendingLimitReference_fac52b6f":
        '''A reference to a SpendingLimit resource.'''
        return typing.cast("_SpendingLimitReference_fac52b6f", jsii.get(self, "spendingLimitRef"))

    @builtins.property
    @jsii.member(jsii_name="deviceArn")
    def device_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.'''
        return typing.cast(builtins.str, jsii.get(self, "deviceArn"))

    @device_arn.setter
    def device_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f6d466fba6fb5cff7f993a0ed644bfbb81208b7620fe51c2805da61528eccaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spendingLimit")
    def spending_limit(self) -> builtins.str:
        '''The maximum amount that can be spent on the specified device, in USD.'''
        return typing.cast(builtins.str, jsii.get(self, "spendingLimit"))

    @spending_limit.setter
    def spending_limit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592d36586a0598b3a37d4c9242bce72e812df6669395ff61be0ccabc55ae48b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spendingLimit", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags to apply to the spending limit.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577fd669a8435ef4fb18677e0b0ac3cc393d2c2a53b237359eb2fcf5ff4ab3ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timePeriod")
    def time_period(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSpendingLimit.TimePeriodProperty"]]:
        '''Defines a time range for spending limits, specifying when the limit is active.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSpendingLimit.TimePeriodProperty"]], jsii.get(self, "timePeriod"))

    @time_period.setter
    def time_period(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSpendingLimit.TimePeriodProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f35f17e99f158d6d3f7600fabad60df67dbe994b5dc8fdaa2d5674aa0a1b4270)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timePeriod", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_braket.CfnSpendingLimit.TimePeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"end_at": "endAt", "start_at": "startAt"},
    )
    class TimePeriodProperty:
        def __init__(self, *, end_at: builtins.str, start_at: builtins.str) -> None:
            '''Defines a time range for spending limits, specifying when the limit is active.

            :param end_at: The end date and time for the spending limit period, in ISO 8601 format.
            :param start_at: The start date and time for the spending limit period, in ISO 8601 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-braket-spendinglimit-timeperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_braket as braket
                
                time_period_property = braket.CfnSpendingLimit.TimePeriodProperty(
                    end_at="endAt",
                    start_at="startAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c51c3cfb7b70039911e5320b94944c5ed6e1ee01b46dd11a73a5569cbc861d1a)
                check_type(argname="argument end_at", value=end_at, expected_type=type_hints["end_at"])
                check_type(argname="argument start_at", value=start_at, expected_type=type_hints["start_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_at": end_at,
                "start_at": start_at,
            }

        @builtins.property
        def end_at(self) -> builtins.str:
            '''The end date and time for the spending limit period, in ISO 8601 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-braket-spendinglimit-timeperiod.html#cfn-braket-spendinglimit-timeperiod-endat
            '''
            result = self._values.get("end_at")
            assert result is not None, "Required property 'end_at' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_at(self) -> builtins.str:
            '''The start date and time for the spending limit period, in ISO 8601 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-braket-spendinglimit-timeperiod.html#cfn-braket-spendinglimit-timeperiod-startat
            '''
            result = self._values.get("start_at")
            assert result is not None, "Required property 'start_at' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimePeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_braket.CfnSpendingLimitProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_arn": "deviceArn",
        "spending_limit": "spendingLimit",
        "tags": "tags",
        "time_period": "timePeriod",
    },
)
class CfnSpendingLimitProps:
    def __init__(
        self,
        *,
        device_arn: builtins.str,
        spending_limit: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        time_period: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSpendingLimit.TimePeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSpendingLimit``.

        :param device_arn: The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.
        :param spending_limit: The maximum amount that can be spent on the specified device, in USD.
        :param tags: The tags to apply to the spending limit.
        :param time_period: Defines a time range for spending limits, specifying when the limit is active.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-braket-spendinglimit.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_braket as braket
            
            cfn_spending_limit_props = braket.CfnSpendingLimitProps(
                device_arn="deviceArn",
                spending_limit="spendingLimit",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                time_period=braket.CfnSpendingLimit.TimePeriodProperty(
                    end_at="endAt",
                    start_at="startAt"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2856750c1b4e9bfabaacdc3d240dbdc8ec3d01b1c0bf9d961cf82c89cc9fdd56)
            check_type(argname="argument device_arn", value=device_arn, expected_type=type_hints["device_arn"])
            check_type(argname="argument spending_limit", value=spending_limit, expected_type=type_hints["spending_limit"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_arn": device_arn,
            "spending_limit": spending_limit,
        }
        if tags is not None:
            self._values["tags"] = tags
        if time_period is not None:
            self._values["time_period"] = time_period

    @builtins.property
    def device_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-braket-spendinglimit.html#cfn-braket-spendinglimit-devicearn
        '''
        result = self._values.get("device_arn")
        assert result is not None, "Required property 'device_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spending_limit(self) -> builtins.str:
        '''The maximum amount that can be spent on the specified device, in USD.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-braket-spendinglimit.html#cfn-braket-spendinglimit-spendinglimit
        '''
        result = self._values.get("spending_limit")
        assert result is not None, "Required property 'spending_limit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags to apply to the spending limit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-braket-spendinglimit.html#cfn-braket-spendinglimit-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def time_period(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSpendingLimit.TimePeriodProperty"]]:
        '''Defines a time range for spending limits, specifying when the limit is active.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-braket-spendinglimit.html#cfn-braket-spendinglimit-timeperiod
        '''
        result = self._values.get("time_period")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSpendingLimit.TimePeriodProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSpendingLimitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSpendingLimit",
    "CfnSpendingLimitProps",
]

publication.publish()

def _typecheckingstub__1c35c7c6e8ca9e275973dad9bd6ceae11c5bfb55d638d0828c196300ab9d14fe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    device_arn: builtins.str,
    spending_limit: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSpendingLimit.TimePeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f300f7aff60a3c9cdaf9438a696c90b73bf3848c152ccbfa1b2299361415e51(
    resource: _ISpendingLimitRef_c3305421,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb08e44816f639c1366677c788c1c7663da3bdeab949fa853e759c018c68363(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7836aabd9049cb0890dcfd861d30fc4a91909f9c9bddfb04418c2e8935fe92f5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8efc42070409da980e6fb943ee279a64a55bd7c598d8d5d7a13cf241d172b267(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f6d466fba6fb5cff7f993a0ed644bfbb81208b7620fe51c2805da61528eccaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592d36586a0598b3a37d4c9242bce72e812df6669395ff61be0ccabc55ae48b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577fd669a8435ef4fb18677e0b0ac3cc393d2c2a53b237359eb2fcf5ff4ab3ff(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f35f17e99f158d6d3f7600fabad60df67dbe994b5dc8fdaa2d5674aa0a1b4270(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSpendingLimit.TimePeriodProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c51c3cfb7b70039911e5320b94944c5ed6e1ee01b46dd11a73a5569cbc861d1a(
    *,
    end_at: builtins.str,
    start_at: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2856750c1b4e9bfabaacdc3d240dbdc8ec3d01b1c0bf9d961cf82c89cc9fdd56(
    *,
    device_arn: builtins.str,
    spending_limit: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSpendingLimit.TimePeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

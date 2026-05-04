r'''
# AWS::UXC Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_uxc as uxc
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for UXC construct libraries](https://constructs.dev/search?q=uxc)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::UXC resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_UXC.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::UXC](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_UXC.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_uxc import (
    AccountCustomizationReference as _AccountCustomizationReference_0125a280,
    IAccountCustomizationRef as _IAccountCustomizationRef_810be58f,
)


@jsii.implements(_IInspectable_c2943556, _IAccountCustomizationRef_810be58f)
class CfnAccountCustomization(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_uxc.CfnAccountCustomization",
):
    '''Resource schema for managing AWS account-level UX customization settings, including account color, visible services, and visible regions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-uxc-accountcustomization.html
    :cloudformationResource: AWS::UXC::AccountCustomization
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_uxc as uxc
        
        cfn_account_customization = uxc.CfnAccountCustomization(self, "MyCfnAccountCustomization",
            account_color="accountColor",
            visible_regions=["visibleRegions"],
            visible_services=["visibleServices"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        account_color: typing.Optional[builtins.str] = None,
        visible_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        visible_services: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::UXC::AccountCustomization``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_color: The color theme assigned to the account for visual identification in the AWS Console.
        :param visible_regions: A list of AWS region identifiers visible to the account in the AWS Console.
        :param visible_services: A list of AWS service identifiers visible to the account in the AWS Console.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37c3b0d81c6b7512bc96c1c47c66ff0d335f357bc15062efd61024a544724110)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountCustomizationProps(
            account_color=account_color,
            visible_regions=visible_regions,
            visible_services=visible_services,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnAccountCustomization")
    @builtins.classmethod
    def is_cfn_account_customization(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAccountCustomization.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c8c620c8dd0a4e833234db63f5d93ade58fc126bbe58e7f39258f2c75352d9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAccountCustomization", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd6eb1c7925d951608c029acd52255f9764cb4bb949698dc09fa593f648014ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f44f9dfa72f040bcf16ba6635b9f0b72e82f46b90b3b6674e6047f2cdbed7485)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="accountCustomizationRef")
    def account_customization_ref(self) -> "_AccountCustomizationReference_0125a280":
        '''A reference to a AccountCustomization resource.'''
        return typing.cast("_AccountCustomizationReference_0125a280", jsii.get(self, "accountCustomizationRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''The AWS account ID that this customization belongs to.

        This is automatically determined from the caller's identity.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountColor")
    def account_color(self) -> typing.Optional[builtins.str]:
        '''The color theme assigned to the account for visual identification in the AWS Console.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountColor"))

    @account_color.setter
    def account_color(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fb8c33ae449fd87ad7af669a2c39936de2c4feb6e650c02c6a8b93dd1570ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountColor", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="visibleRegions")
    def visible_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS region identifiers visible to the account in the AWS Console.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "visibleRegions"))

    @visible_regions.setter
    def visible_regions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a55eb948736eaf0670badbd62d8e1ebbf2c698792a92b39d1dcc56ab066af92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleRegions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="visibleServices")
    def visible_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS service identifiers visible to the account in the AWS Console.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "visibleServices"))

    @visible_services.setter
    def visible_services(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96dac46328c85397990b4e60031f31361219f12ab70c79223e8b87d9aea08886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibleServices", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_uxc.CfnAccountCustomizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_color": "accountColor",
        "visible_regions": "visibleRegions",
        "visible_services": "visibleServices",
    },
)
class CfnAccountCustomizationProps:
    def __init__(
        self,
        *,
        account_color: typing.Optional[builtins.str] = None,
        visible_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        visible_services: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccountCustomization``.

        :param account_color: The color theme assigned to the account for visual identification in the AWS Console.
        :param visible_regions: A list of AWS region identifiers visible to the account in the AWS Console.
        :param visible_services: A list of AWS service identifiers visible to the account in the AWS Console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-uxc-accountcustomization.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_uxc as uxc
            
            cfn_account_customization_props = uxc.CfnAccountCustomizationProps(
                account_color="accountColor",
                visible_regions=["visibleRegions"],
                visible_services=["visibleServices"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2da66c4c7da714261fc3babf37cab227f03a7b15ede0ef0e55a3145b55332a)
            check_type(argname="argument account_color", value=account_color, expected_type=type_hints["account_color"])
            check_type(argname="argument visible_regions", value=visible_regions, expected_type=type_hints["visible_regions"])
            check_type(argname="argument visible_services", value=visible_services, expected_type=type_hints["visible_services"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_color is not None:
            self._values["account_color"] = account_color
        if visible_regions is not None:
            self._values["visible_regions"] = visible_regions
        if visible_services is not None:
            self._values["visible_services"] = visible_services

    @builtins.property
    def account_color(self) -> typing.Optional[builtins.str]:
        '''The color theme assigned to the account for visual identification in the AWS Console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-uxc-accountcustomization.html#cfn-uxc-accountcustomization-accountcolor
        '''
        result = self._values.get("account_color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visible_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS region identifiers visible to the account in the AWS Console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-uxc-accountcustomization.html#cfn-uxc-accountcustomization-visibleregions
        '''
        result = self._values.get("visible_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def visible_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AWS service identifiers visible to the account in the AWS Console.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-uxc-accountcustomization.html#cfn-uxc-accountcustomization-visibleservices
        '''
        result = self._values.get("visible_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountCustomizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccountCustomization",
    "CfnAccountCustomizationProps",
]

publication.publish()

def _typecheckingstub__37c3b0d81c6b7512bc96c1c47c66ff0d335f357bc15062efd61024a544724110(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_color: typing.Optional[builtins.str] = None,
    visible_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    visible_services: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c8c620c8dd0a4e833234db63f5d93ade58fc126bbe58e7f39258f2c75352d9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd6eb1c7925d951608c029acd52255f9764cb4bb949698dc09fa593f648014ae(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f44f9dfa72f040bcf16ba6635b9f0b72e82f46b90b3b6674e6047f2cdbed7485(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fb8c33ae449fd87ad7af669a2c39936de2c4feb6e650c02c6a8b93dd1570ef4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a55eb948736eaf0670badbd62d8e1ebbf2c698792a92b39d1dcc56ab066af92(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96dac46328c85397990b4e60031f31361219f12ab70c79223e8b87d9aea08886(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2da66c4c7da714261fc3babf37cab227f03a7b15ede0ef0e55a3145b55332a(
    *,
    account_color: typing.Optional[builtins.str] = None,
    visible_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    visible_services: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

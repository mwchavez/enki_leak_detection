r'''
# AWS::Route53GlobalResolver Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_route53globalresolver as route53globalresolver
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Route53GlobalResolver construct libraries](https://constructs.dev/search?q=route53globalresolver)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Route53GlobalResolver resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53GlobalResolver.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Route53GlobalResolver](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53GlobalResolver.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_route53globalresolver import (
    AccessSourceReference as _AccessSourceReference_3bb9cfc2,
    AccessTokenReference as _AccessTokenReference_38473d18,
    DnsViewReference as _DnsViewReference_5e401e00,
    FirewallDomainListReference as _FirewallDomainListReference_6219a1bd,
    FirewallRuleReference as _FirewallRuleReference_9ac24181,
    GlobalResolverReference as _GlobalResolverReference_f82bf8b1,
    HostedZoneAssociationReference as _HostedZoneAssociationReference_75cb03f5,
    IAccessSourceRef as _IAccessSourceRef_1db97119,
    IAccessTokenRef as _IAccessTokenRef_b08178a7,
    IDnsViewRef as _IDnsViewRef_cc315308,
    IFirewallDomainListRef as _IFirewallDomainListRef_9fe4e2fb,
    IFirewallRuleRef as _IFirewallRuleRef_6295af58,
    IGlobalResolverRef as _IGlobalResolverRef_e2deb39d,
    IHostedZoneAssociationRef as _IHostedZoneAssociationRef_f6749a8d,
)


@jsii.implements(_IInspectable_c2943556, _IAccessSourceRef_1db97119, _ITaggableV2_4e6798f8)
class CfnAccessSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnAccessSource",
):
    '''Resource schema for AWS::Route53GlobalResolver::AccessSource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html
    :cloudformationResource: AWS::Route53GlobalResolver::AccessSource
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_access_source = route53globalresolver.CfnAccessSource(self, "MyCfnAccessSource",
            cidr="cidr",
            dns_view_id="dnsViewId",
            protocol="protocol",
        
            # the properties below are optional
            client_token="clientToken",
            ip_address_type="ipAddressType",
            name="name",
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
        cidr: builtins.str,
        dns_view_id: builtins.str,
        protocol: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::AccessSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cidr: 
        :param dns_view_id: 
        :param protocol: 
        :param client_token: 
        :param ip_address_type: 
        :param name: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e26e227e8b54f12cab6d99359743bad21bc5f9bb5d04e4c30fc1b3deea2b91d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessSourceProps(
            cidr=cidr,
            dns_view_id=dns_view_id,
            protocol=protocol,
            client_token=client_token,
            ip_address_type=ip_address_type,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAccessSource")
    @builtins.classmethod
    def arn_for_access_source(
        cls,
        resource: "_IAccessSourceRef_1db97119",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e03274618d5d2e93650f0be017e364784edc53006e272e106bb7cf38a7cfaf1)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAccessSource", [resource]))

    @jsii.member(jsii_name="isCfnAccessSource")
    @builtins.classmethod
    def is_cfn_access_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAccessSource.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05603aac4da0889d167bb1387eabd33b6fecfac386e077073db14ba1ac5905d1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAccessSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ccd8f9ba4eef07d166aece09cb53abc570035042a9b8212d3c028dac9d57409)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7123f2aaf7effe01c513196a1156c24fcfd15a53b9d6db929d6bc3a36f3f9471)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="accessSourceRef")
    def access_source_ref(self) -> "_AccessSourceReference_3bb9cfc2":
        '''A reference to a AccessSource resource.'''
        return typing.cast("_AccessSourceReference_3bb9cfc2", jsii.get(self, "accessSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessSourceId")
    def attr_access_source_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AccessSourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessSourceId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc669c1f788dfe513d35b84e76f6ab663967b55f657ce94818e351138c4e9dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dnsViewId")
    def dns_view_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsViewId"))

    @dns_view_id.setter
    def dns_view_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b8ccb772e4fc895f76707e5058eeed752ae1f36d776224e2363c15bd318c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsViewId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde1a183981630a3fffc38ddff8a3f6febb6937b3c5949799453e30cbc7310a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96ff0bae281a0a2532fce6d0ea5b7198a748c1e755f444a05f921f6932093028)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05f8e72a9b2ca81a1f33202e71d4ddca48f4342a704a4421f5b0bb4a40fd1ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41c9d2a0bbfe1d84266d379f49840e2dab332041118d9c1df05a2b456cced6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0ecd9ff59b993b152a551949ae0b2ad042a6ef742c7fab5e74e60e49795dfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnAccessSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cidr": "cidr",
        "dns_view_id": "dnsViewId",
        "protocol": "protocol",
        "client_token": "clientToken",
        "ip_address_type": "ipAddressType",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAccessSourceProps:
    def __init__(
        self,
        *,
        cidr: builtins.str,
        dns_view_id: builtins.str,
        protocol: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessSource``.

        :param cidr: 
        :param dns_view_id: 
        :param protocol: 
        :param client_token: 
        :param ip_address_type: 
        :param name: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_access_source_props = route53globalresolver.CfnAccessSourceProps(
                cidr="cidr",
                dns_view_id="dnsViewId",
                protocol="protocol",
            
                # the properties below are optional
                client_token="clientToken",
                ip_address_type="ipAddressType",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2356855e49ab75da15cc0328069114313fafa0ff86a20d803b7c2be30c7b45)
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument dns_view_id", value=dns_view_id, expected_type=type_hints["dns_view_id"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr": cidr,
            "dns_view_id": dns_view_id,
            "protocol": protocol,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cidr(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-cidr
        '''
        result = self._values.get("cidr")
        assert result is not None, "Required property 'cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_view_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-dnsviewid
        '''
        result = self._values.get("dns_view_id")
        assert result is not None, "Required property 'dns_view_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesssource.html#cfn-route53globalresolver-accesssource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IAccessTokenRef_b08178a7, _ITaggableV2_4e6798f8)
class CfnAccessToken(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnAccessToken",
):
    '''Resource schema for AWS::Route53GlobalResolver::AccessToken.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html
    :cloudformationResource: AWS::Route53GlobalResolver::AccessToken
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_access_token = route53globalresolver.CfnAccessToken(self, "MyCfnAccessToken",
            dns_view_id="dnsViewId",
        
            # the properties below are optional
            client_token="clientToken",
            expires_at="expiresAt",
            name="name",
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
        dns_view_id: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        expires_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::AccessToken``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dns_view_id: 
        :param client_token: 
        :param expires_at: 
        :param name: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ba20f227121b366c42a9c098db67c39a85a9415f50b946dafad20209022b25)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessTokenProps(
            dns_view_id=dns_view_id,
            client_token=client_token,
            expires_at=expires_at,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAccessToken")
    @builtins.classmethod
    def arn_for_access_token(
        cls,
        resource: "_IAccessTokenRef_b08178a7",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bd9a24451fa5b1382911f1e89ae8067a394ff17c9e74aa6e7f52032fd523cc4)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAccessToken", [resource]))

    @jsii.member(jsii_name="isCfnAccessToken")
    @builtins.classmethod
    def is_cfn_access_token(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAccessToken.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c38c4bd39315438fbb6061db5804f6f55b7a3f1f8bc3fafa525198836eda5ee1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAccessToken", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04ef7a912a877531ae4298ea3f8bbf620dd209ba529c38ca67e6707431b584f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__882301402f4fbd8cac64cf2b9e02bcccd51a3c37d41129fc2914c0f40a7d0ee2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenRef")
    def access_token_ref(self) -> "_AccessTokenReference_38473d18":
        '''A reference to a AccessToken resource.'''
        return typing.cast("_AccessTokenReference_38473d18", jsii.get(self, "accessTokenRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessTokenId")
    def attr_access_token_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AccessTokenId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessTokenId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrGlobalResolverId")
    def attr_global_resolver_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: GlobalResolverId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGlobalResolverId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrValue")
    def attr_value(self) -> builtins.str:
        '''
        :cloudformationAttribute: Value
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValue"))

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
    @jsii.member(jsii_name="dnsViewId")
    def dns_view_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsViewId"))

    @dns_view_id.setter
    def dns_view_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1efd29213f22f5d27bdc1cc739dc8378215bc1eaa8894d05398b746c14b5f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsViewId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b704c3f64f2cbd55623b131a5af32dc3d8408a339cad0a16a258b0b8a6cccd09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expiresAt")
    def expires_at(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresAt"))

    @expires_at.setter
    def expires_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e6d199b63f268f056a2ec1768cde0c3075bc16623f4a5462963cebef8eed62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresAt", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceddf2530916a54b784424c359bbba7fb09d8ec8158118d8d6aaeac3513a2101)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605d3f9cf55610f9b074c8814ec1cb33c3e2e73976521352747a92132b766b4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnAccessTokenProps",
    jsii_struct_bases=[],
    name_mapping={
        "dns_view_id": "dnsViewId",
        "client_token": "clientToken",
        "expires_at": "expiresAt",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAccessTokenProps:
    def __init__(
        self,
        *,
        dns_view_id: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        expires_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessToken``.

        :param dns_view_id: 
        :param client_token: 
        :param expires_at: 
        :param name: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_access_token_props = route53globalresolver.CfnAccessTokenProps(
                dns_view_id="dnsViewId",
            
                # the properties below are optional
                client_token="clientToken",
                expires_at="expiresAt",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c886d3ce6884b3f680b0cccc4106854b2a78d4361077ac1940c2e5c6f37ece2)
            check_type(argname="argument dns_view_id", value=dns_view_id, expected_type=type_hints["dns_view_id"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument expires_at", value=expires_at, expected_type=type_hints["expires_at"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dns_view_id": dns_view_id,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if expires_at is not None:
            self._values["expires_at"] = expires_at
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dns_view_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html#cfn-route53globalresolver-accesstoken-dnsviewid
        '''
        result = self._values.get("dns_view_id")
        assert result is not None, "Required property 'dns_view_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html#cfn-route53globalresolver-accesstoken-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires_at(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html#cfn-route53globalresolver-accesstoken-expiresat
        '''
        result = self._values.get("expires_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html#cfn-route53globalresolver-accesstoken-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-accesstoken.html#cfn-route53globalresolver-accesstoken-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessTokenProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IDnsViewRef_cc315308, _ITaggableV2_4e6798f8)
class CfnDnsView(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnDnsView",
):
    '''Resource schema for AWS::Route53GlobalResolver::DnsView.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html
    :cloudformationResource: AWS::Route53GlobalResolver::DnsView
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_dns_view = route53globalresolver.CfnDnsView(self, "MyCfnDnsView",
            global_resolver_id="globalResolverId",
            name="name",
        
            # the properties below are optional
            client_token="clientToken",
            description="description",
            dnssec_validation="dnssecValidation",
            edns_client_subnet="ednsClientSubnet",
            firewall_rules_fail_open="firewallRulesFailOpen",
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
        global_resolver_id: builtins.str,
        name: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        dnssec_validation: typing.Optional[builtins.str] = None,
        edns_client_subnet: typing.Optional[builtins.str] = None,
        firewall_rules_fail_open: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::DnsView``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param global_resolver_id: 
        :param name: 
        :param client_token: 
        :param description: 
        :param dnssec_validation: 
        :param edns_client_subnet: 
        :param firewall_rules_fail_open: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9f4752adcdd6e72c7cd34b7681a4f92727b18fe01a3115c9611f42ee1775ee6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDnsViewProps(
            global_resolver_id=global_resolver_id,
            name=name,
            client_token=client_token,
            description=description,
            dnssec_validation=dnssec_validation,
            edns_client_subnet=edns_client_subnet,
            firewall_rules_fail_open=firewall_rules_fail_open,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDnsView")
    @builtins.classmethod
    def arn_for_dns_view(cls, resource: "_IDnsViewRef_cc315308") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc442efadfd1cffb86a82368e040b1113a0526c334e4ce810913bd4849e3b852)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDnsView", [resource]))

    @jsii.member(jsii_name="isCfnDnsView")
    @builtins.classmethod
    def is_cfn_dns_view(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDnsView.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b490856e9824a822de72942079e730d873721191b46d3867b0115aa63a0f0cb6)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDnsView", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b49489960a5f211b491107ec4bfc87ea246355380d030e95060c24632c1e5bba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d035f1bbfd9ba07f376bc462754e909ab7a57439d520db08f74c23003e35854d)
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsViewId")
    def attr_dns_view_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DnsViewId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsViewId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="dnsViewRef")
    def dns_view_ref(self) -> "_DnsViewReference_5e401e00":
        '''A reference to a DnsView resource.'''
        return typing.cast("_DnsViewReference_5e401e00", jsii.get(self, "dnsViewRef"))

    @builtins.property
    @jsii.member(jsii_name="globalResolverId")
    def global_resolver_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalResolverId"))

    @global_resolver_id.setter
    def global_resolver_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e41cd1cd94d8741ef44561111afff11465dce8754456d1c2c0987fe154e2e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalResolverId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d66be568aecf026fd401f159dca8b5c47f937b6ff71b44ac4c62ce5d7a3f589)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8ff87145e371ec40ce7499f914ee608c1a6a6b3345c9dd2f5e20b9afa6d8a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e85643d8d0b6b9b57cc22f783f11c470345f91c02f53a59d91316150515984e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dnssecValidation")
    def dnssec_validation(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnssecValidation"))

    @dnssec_validation.setter
    def dnssec_validation(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b193bb7e640cfea3c0075dc77d73f04a82fb0538fe217dba438b07798d6491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnssecValidation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ednsClientSubnet")
    def edns_client_subnet(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ednsClientSubnet"))

    @edns_client_subnet.setter
    def edns_client_subnet(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd9245b51907f66af0986bb95821f553943007f6946c5c3e7a22198fbc4d77e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ednsClientSubnet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="firewallRulesFailOpen")
    def firewall_rules_fail_open(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallRulesFailOpen"))

    @firewall_rules_fail_open.setter
    def firewall_rules_fail_open(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4ac4a77283d843638e97abdf381cd9c32eba01be2e86932b682e2aeee7d1718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallRulesFailOpen", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42aed69fa5596ce5731b95fd083072e7a440119751d0837291fec5eb338ad3d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnDnsViewProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_resolver_id": "globalResolverId",
        "name": "name",
        "client_token": "clientToken",
        "description": "description",
        "dnssec_validation": "dnssecValidation",
        "edns_client_subnet": "ednsClientSubnet",
        "firewall_rules_fail_open": "firewallRulesFailOpen",
        "tags": "tags",
    },
)
class CfnDnsViewProps:
    def __init__(
        self,
        *,
        global_resolver_id: builtins.str,
        name: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        dnssec_validation: typing.Optional[builtins.str] = None,
        edns_client_subnet: typing.Optional[builtins.str] = None,
        firewall_rules_fail_open: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDnsView``.

        :param global_resolver_id: 
        :param name: 
        :param client_token: 
        :param description: 
        :param dnssec_validation: 
        :param edns_client_subnet: 
        :param firewall_rules_fail_open: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_dns_view_props = route53globalresolver.CfnDnsViewProps(
                global_resolver_id="globalResolverId",
                name="name",
            
                # the properties below are optional
                client_token="clientToken",
                description="description",
                dnssec_validation="dnssecValidation",
                edns_client_subnet="ednsClientSubnet",
                firewall_rules_fail_open="firewallRulesFailOpen",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be47ce035c982759ab526e0529caaa98a67680691f036975711a8fc5d4a202b3)
            check_type(argname="argument global_resolver_id", value=global_resolver_id, expected_type=type_hints["global_resolver_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dnssec_validation", value=dnssec_validation, expected_type=type_hints["dnssec_validation"])
            check_type(argname="argument edns_client_subnet", value=edns_client_subnet, expected_type=type_hints["edns_client_subnet"])
            check_type(argname="argument firewall_rules_fail_open", value=firewall_rules_fail_open, expected_type=type_hints["firewall_rules_fail_open"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_resolver_id": global_resolver_id,
            "name": name,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if description is not None:
            self._values["description"] = description
        if dnssec_validation is not None:
            self._values["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            self._values["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            self._values["firewall_rules_fail_open"] = firewall_rules_fail_open
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_resolver_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-globalresolverid
        '''
        result = self._values.get("global_resolver_id")
        assert result is not None, "Required property 'global_resolver_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dnssec_validation(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-dnssecvalidation
        '''
        result = self._values.get("dnssec_validation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edns_client_subnet(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-ednsclientsubnet
        '''
        result = self._values.get("edns_client_subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firewall_rules_fail_open(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-firewallrulesfailopen
        '''
        result = self._values.get("firewall_rules_fail_open")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-dnsview.html#cfn-route53globalresolver-dnsview-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDnsViewProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFirewallDomainListRef_9fe4e2fb, _ITaggableV2_4e6798f8)
class CfnFirewallDomainList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnFirewallDomainList",
):
    '''Resource schema for AWS::Route53GlobalResolver::FirewallDomainList.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html
    :cloudformationResource: AWS::Route53GlobalResolver::FirewallDomainList
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_firewall_domain_list = route53globalresolver.CfnFirewallDomainList(self, "MyCfnFirewallDomainList",
            global_resolver_id="globalResolverId",
            name="name",
        
            # the properties below are optional
            client_token="clientToken",
            description="description",
            domain_file_url="domainFileUrl",
            domains=["domains"],
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
        global_resolver_id: builtins.str,
        name: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::FirewallDomainList``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param global_resolver_id: 
        :param name: 
        :param client_token: 
        :param description: 
        :param domain_file_url: S3 URL to import domains from.
        :param domains: An inline list of domains to use for this domain list.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e446398d49f5f497ed38c697da2d836f26ea7124989f1921b6b1ef9c449f57d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallDomainListProps(
            global_resolver_id=global_resolver_id,
            name=name,
            client_token=client_token,
            description=description,
            domain_file_url=domain_file_url,
            domains=domains,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFirewallDomainList")
    @builtins.classmethod
    def arn_for_firewall_domain_list(
        cls,
        resource: "_IFirewallDomainListRef_9fe4e2fb",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19474410306aa2384dcd6bdbcaaadf6b36be962c6d51ee32fe7036441649d773)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFirewallDomainList", [resource]))

    @jsii.member(jsii_name="isCfnFirewallDomainList")
    @builtins.classmethod
    def is_cfn_firewall_domain_list(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFirewallDomainList.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3156089d9b1f04e4beb6cc12926d5b242645cce554891de44987a1184cd28b1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFirewallDomainList", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60fd40c31a28b2d5ab6de007c5f03584b6e7e07b78aedd82036414b78dfc3017)
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
            type_hints = typing.get_type_hints(_typecheckingstub__04ecdcc4256b26330346af2135b7866fb7262051a1a5f74cc45c0981fdb59c69)
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainCount")
    def attr_domain_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: DomainCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDomainCount"))

    @builtins.property
    @jsii.member(jsii_name="attrFirewallDomainListId")
    def attr_firewall_domain_list_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: FirewallDomainListId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallDomainListId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''
        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="firewallDomainListRef")
    def firewall_domain_list_ref(self) -> "_FirewallDomainListReference_6219a1bd":
        '''A reference to a FirewallDomainList resource.'''
        return typing.cast("_FirewallDomainListReference_6219a1bd", jsii.get(self, "firewallDomainListRef"))

    @builtins.property
    @jsii.member(jsii_name="globalResolverId")
    def global_resolver_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalResolverId"))

    @global_resolver_id.setter
    def global_resolver_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b3677ff1f7ee302b88b5cb36d8b2dbb2aede7b72da92bcd6de78284559334f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalResolverId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860763fdea89f756c6c90d95e5087d27a33ed47e8027548e3f61222562908c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84eca686d85cb13c5722a2285bde95d87f6847e52d5fb465ef94942de5197cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eea47993f183bb17d4d3b44850ff6b8583ee9017b513c8fbe2776ab8cda9579)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainFileUrl")
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''S3 URL to import domains from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainFileUrl"))

    @domain_file_url.setter
    def domain_file_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef515883247b8072fc18a08dec90a59230966b8a0efa777e4fe6af7cb0d9fa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainFileUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An inline list of domains to use for this domain list.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__070c5ecfb715828169cae58ca6834d54dfb1f94ad146cf4c311bdabeb5336560)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domains", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a595596d23fe50bb26e322a036c3596920a5ce2e75e91f14b2a5eba1065e2645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnFirewallDomainListProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_resolver_id": "globalResolverId",
        "name": "name",
        "client_token": "clientToken",
        "description": "description",
        "domain_file_url": "domainFileUrl",
        "domains": "domains",
        "tags": "tags",
    },
)
class CfnFirewallDomainListProps:
    def __init__(
        self,
        *,
        global_resolver_id: builtins.str,
        name: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewallDomainList``.

        :param global_resolver_id: 
        :param name: 
        :param client_token: 
        :param description: 
        :param domain_file_url: S3 URL to import domains from.
        :param domains: An inline list of domains to use for this domain list.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_firewall_domain_list_props = route53globalresolver.CfnFirewallDomainListProps(
                global_resolver_id="globalResolverId",
                name="name",
            
                # the properties below are optional
                client_token="clientToken",
                description="description",
                domain_file_url="domainFileUrl",
                domains=["domains"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d198a7489a5e52354a6e7aa2cc4b677925fb253ffe4562fee89db32fca188fc)
            check_type(argname="argument global_resolver_id", value=global_resolver_id, expected_type=type_hints["global_resolver_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_file_url", value=domain_file_url, expected_type=type_hints["domain_file_url"])
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_resolver_id": global_resolver_id,
            "name": name,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if description is not None:
            self._values["description"] = description
        if domain_file_url is not None:
            self._values["domain_file_url"] = domain_file_url
        if domains is not None:
            self._values["domains"] = domains
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_resolver_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-globalresolverid
        '''
        result = self._values.get("global_resolver_id")
        assert result is not None, "Required property 'global_resolver_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''S3 URL to import domains from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-domainfileurl
        '''
        result = self._values.get("domain_file_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An inline list of domains to use for this domain list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-domains
        '''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewalldomainlist.html#cfn-route53globalresolver-firewalldomainlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallDomainListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFirewallRuleRef_6295af58)
class CfnFirewallRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnFirewallRule",
):
    '''Resource schema for AWS::Route53GlobalResolver::FirewallRule.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html
    :cloudformationResource: AWS::Route53GlobalResolver::FirewallRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_firewall_rule = route53globalresolver.CfnFirewallRule(self, "MyCfnFirewallRule",
            action="action",
            dns_view_id="dnsViewId",
            name="name",
        
            # the properties below are optional
            block_override_dns_type="blockOverrideDnsType",
            block_override_domain="blockOverrideDomain",
            block_override_ttl=123,
            block_response="blockResponse",
            client_token="clientToken",
            confidence_threshold="confidenceThreshold",
            description="description",
            dns_advanced_protection="dnsAdvancedProtection",
            firewall_domain_list_id="firewallDomainListId",
            priority=123,
            q_type="qType"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        action: builtins.str,
        dns_view_id: builtins.str,
        name: builtins.str,
        block_override_dns_type: typing.Optional[builtins.str] = None,
        block_override_domain: typing.Optional[builtins.str] = None,
        block_override_ttl: typing.Optional[jsii.Number] = None,
        block_response: typing.Optional[builtins.str] = None,
        client_token: typing.Optional[builtins.str] = None,
        confidence_threshold: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        dns_advanced_protection: typing.Optional[builtins.str] = None,
        firewall_domain_list_id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        q_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::FirewallRule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: 
        :param dns_view_id: 
        :param name: 
        :param block_override_dns_type: 
        :param block_override_domain: 
        :param block_override_ttl: 
        :param block_response: 
        :param client_token: 
        :param confidence_threshold: 
        :param description: 
        :param dns_advanced_protection: 
        :param firewall_domain_list_id: 
        :param priority: 
        :param q_type: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6583b9c78ed44e0741a9157f77381d7e0d146fddaecf32085a2ec279acc3c2e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFirewallRuleProps(
            action=action,
            dns_view_id=dns_view_id,
            name=name,
            block_override_dns_type=block_override_dns_type,
            block_override_domain=block_override_domain,
            block_override_ttl=block_override_ttl,
            block_response=block_response,
            client_token=client_token,
            confidence_threshold=confidence_threshold,
            description=description,
            dns_advanced_protection=dns_advanced_protection,
            firewall_domain_list_id=firewall_domain_list_id,
            priority=priority,
            q_type=q_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnFirewallRule")
    @builtins.classmethod
    def is_cfn_firewall_rule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFirewallRule.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33d1a1948e0858fe4536c23a3492cecb0c4fc7517de4ac60ac9e802720c30e0)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFirewallRule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7e62d2bd41c552313dfa6ecccf16fcc964601515f9f78a4232df1e5c2385568)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b03320d9333ed0a6f4578084157955464912cd3481ba4e258fa9e6e4403f41b)
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
    @jsii.member(jsii_name="attrFirewallRuleId")
    def attr_firewall_rule_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: FirewallRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFirewallRuleId"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryType")
    def attr_query_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: QueryType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryType"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="firewallRuleRef")
    def firewall_rule_ref(self) -> "_FirewallRuleReference_9ac24181":
        '''A reference to a FirewallRule resource.'''
        return typing.cast("_FirewallRuleReference_9ac24181", jsii.get(self, "firewallRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df53bebd126372c73837119fcb380b046153e8eba79d94322613b67d6538d1ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dnsViewId")
    def dns_view_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsViewId"))

    @dns_view_id.setter
    def dns_view_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebf9dd4c773dfb353399502591dc55c1f9260be931a82f6c050e1cda4772f95e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsViewId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a296c65c3bba86a2f84d9b49148c39a35f4cc07d53258ba1189913bdb9db65c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="blockOverrideDnsType")
    def block_override_dns_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockOverrideDnsType"))

    @block_override_dns_type.setter
    def block_override_dns_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d2a00b7a7f3c8557c4d29a9084b0056e619989cad0c6d5e535086ee266f06b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideDnsType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="blockOverrideDomain")
    def block_override_domain(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockOverrideDomain"))

    @block_override_domain.setter
    def block_override_domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2dcc3ab9abeb84a1233e0ed3dfc8a4ad7cf0ee0476b7e6508dfec7ebb39ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideDomain", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="blockOverrideTtl")
    def block_override_ttl(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "blockOverrideTtl"))

    @block_override_ttl.setter
    def block_override_ttl(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__623f287e789666287232f4cdcfd802c7bca918fb304365a548202f5bf55a6253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockOverrideTtl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="blockResponse")
    def block_response(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockResponse"))

    @block_response.setter
    def block_response(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c6e5756daa4edb39cdc5dd742884a967e531ef9f34ba1facf352ec6677ae832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockResponse", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab86dd47e7897a324abbcaeec22c0d6eeaf3762deeac7bc9a309d0151a9b81ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="confidenceThreshold")
    def confidence_threshold(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "confidenceThreshold"))

    @confidence_threshold.setter
    def confidence_threshold(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d37fc845269f164fa0cf3e48990af182d9dc1686dbd3b7dbb7701b86396aa39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidenceThreshold", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60c174302408bcfaa2815c8a3f8096e3837ee1bf6e8a7b7e38e29dfc2a3616c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dnsAdvancedProtection")
    def dns_advanced_protection(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsAdvancedProtection"))

    @dns_advanced_protection.setter
    def dns_advanced_protection(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b77040a4e57b230dd8671210a76850893595b710bff3f20978a08200ddbb8ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsAdvancedProtection", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListId")
    def firewall_domain_list_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firewallDomainListId"))

    @firewall_domain_list_id.setter
    def firewall_domain_list_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112a6c71e13eebf15e9566e12ee5442386f646f6017070613764c16fbd87a1ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firewallDomainListId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac571aadf8e72a4bf0c10c3647247c011960f4fd372b4f5155fdf082977ca7ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="qType")
    def q_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qType"))

    @q_type.setter
    def q_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af647b4d580894203899eba8b4aa5d78ceb0fa976874ea177ea5eb4020a98154)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qType", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnFirewallRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "dns_view_id": "dnsViewId",
        "name": "name",
        "block_override_dns_type": "blockOverrideDnsType",
        "block_override_domain": "blockOverrideDomain",
        "block_override_ttl": "blockOverrideTtl",
        "block_response": "blockResponse",
        "client_token": "clientToken",
        "confidence_threshold": "confidenceThreshold",
        "description": "description",
        "dns_advanced_protection": "dnsAdvancedProtection",
        "firewall_domain_list_id": "firewallDomainListId",
        "priority": "priority",
        "q_type": "qType",
    },
)
class CfnFirewallRuleProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        dns_view_id: builtins.str,
        name: builtins.str,
        block_override_dns_type: typing.Optional[builtins.str] = None,
        block_override_domain: typing.Optional[builtins.str] = None,
        block_override_ttl: typing.Optional[jsii.Number] = None,
        block_response: typing.Optional[builtins.str] = None,
        client_token: typing.Optional[builtins.str] = None,
        confidence_threshold: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        dns_advanced_protection: typing.Optional[builtins.str] = None,
        firewall_domain_list_id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        q_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFirewallRule``.

        :param action: 
        :param dns_view_id: 
        :param name: 
        :param block_override_dns_type: 
        :param block_override_domain: 
        :param block_override_ttl: 
        :param block_response: 
        :param client_token: 
        :param confidence_threshold: 
        :param description: 
        :param dns_advanced_protection: 
        :param firewall_domain_list_id: 
        :param priority: 
        :param q_type: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_firewall_rule_props = route53globalresolver.CfnFirewallRuleProps(
                action="action",
                dns_view_id="dnsViewId",
                name="name",
            
                # the properties below are optional
                block_override_dns_type="blockOverrideDnsType",
                block_override_domain="blockOverrideDomain",
                block_override_ttl=123,
                block_response="blockResponse",
                client_token="clientToken",
                confidence_threshold="confidenceThreshold",
                description="description",
                dns_advanced_protection="dnsAdvancedProtection",
                firewall_domain_list_id="firewallDomainListId",
                priority=123,
                q_type="qType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed0b3cd14f9eb8ed481db1c0eb01b2961bc4aaf2fa720f8f0998729ce22ea47e)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument dns_view_id", value=dns_view_id, expected_type=type_hints["dns_view_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument block_override_dns_type", value=block_override_dns_type, expected_type=type_hints["block_override_dns_type"])
            check_type(argname="argument block_override_domain", value=block_override_domain, expected_type=type_hints["block_override_domain"])
            check_type(argname="argument block_override_ttl", value=block_override_ttl, expected_type=type_hints["block_override_ttl"])
            check_type(argname="argument block_response", value=block_response, expected_type=type_hints["block_response"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument confidence_threshold", value=confidence_threshold, expected_type=type_hints["confidence_threshold"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dns_advanced_protection", value=dns_advanced_protection, expected_type=type_hints["dns_advanced_protection"])
            check_type(argname="argument firewall_domain_list_id", value=firewall_domain_list_id, expected_type=type_hints["firewall_domain_list_id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument q_type", value=q_type, expected_type=type_hints["q_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "dns_view_id": dns_view_id,
            "name": name,
        }
        if block_override_dns_type is not None:
            self._values["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            self._values["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            self._values["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            self._values["block_response"] = block_response
        if client_token is not None:
            self._values["client_token"] = client_token
        if confidence_threshold is not None:
            self._values["confidence_threshold"] = confidence_threshold
        if description is not None:
            self._values["description"] = description
        if dns_advanced_protection is not None:
            self._values["dns_advanced_protection"] = dns_advanced_protection
        if firewall_domain_list_id is not None:
            self._values["firewall_domain_list_id"] = firewall_domain_list_id
        if priority is not None:
            self._values["priority"] = priority
        if q_type is not None:
            self._values["q_type"] = q_type

    @builtins.property
    def action(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_view_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-dnsviewid
        '''
        result = self._values.get("dns_view_id")
        assert result is not None, "Required property 'dns_view_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def block_override_dns_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-blockoverridednstype
        '''
        result = self._values.get("block_override_dns_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_override_domain(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-blockoverridedomain
        '''
        result = self._values.get("block_override_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_override_ttl(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-blockoverridettl
        '''
        result = self._values.get("block_override_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def block_response(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-blockresponse
        '''
        result = self._values.get("block_response")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def confidence_threshold(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-confidencethreshold
        '''
        result = self._values.get("confidence_threshold")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_advanced_protection(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-dnsadvancedprotection
        '''
        result = self._values.get("dns_advanced_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firewall_domain_list_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-firewalldomainlistid
        '''
        result = self._values.get("firewall_domain_list_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def q_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-firewallrule.html#cfn-route53globalresolver-firewallrule-qtype
        '''
        result = self._values.get("q_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IGlobalResolverRef_e2deb39d, _ITaggableV2_4e6798f8)
class CfnGlobalResolver(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnGlobalResolver",
):
    '''Resource schema for AWS::Route53GlobalResolver::GlobalResolver.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html
    :cloudformationResource: AWS::Route53GlobalResolver::GlobalResolver
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_global_resolver = route53globalresolver.CfnGlobalResolver(self, "MyCfnGlobalResolver",
            name="name",
            regions=["regions"],
        
            # the properties below are optional
            client_token="clientToken",
            description="description",
            ip_address_type="ipAddressType",
            observability_region="observabilityRegion",
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
        regions: typing.Sequence[builtins.str],
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        observability_region: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::GlobalResolver``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: 
        :param regions: 
        :param client_token: 
        :param description: 
        :param ip_address_type: 
        :param observability_region: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da7e79855025c0b30f6623575b9427a70db31e48fe2bbbcb7afe985433e2ca60)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGlobalResolverProps(
            name=name,
            regions=regions,
            client_token=client_token,
            description=description,
            ip_address_type=ip_address_type,
            observability_region=observability_region,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGlobalResolver")
    @builtins.classmethod
    def arn_for_global_resolver(
        cls,
        resource: "_IGlobalResolverRef_e2deb39d",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586f8599fc720ab431e4bbff7f3f0e54c43a9c6e4c5e61ec51598ee274df065e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGlobalResolver", [resource]))

    @jsii.member(jsii_name="isCfnGlobalResolver")
    @builtins.classmethod
    def is_cfn_global_resolver(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGlobalResolver.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1480ed04d9a64f793fbcb9b37f7bf0d263f0561598d9eae1efe6f4fd99627dad)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGlobalResolver", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97d150f595f1701196870035d68c5f82f675b3f5b2179dcbcd83ed1ced124d77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0846fb5dc8a488f6d34e544d26c231a88b4a157f5b038a038db0139214418d2b)
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
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsName")
    def attr_dns_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDnsName"))

    @builtins.property
    @jsii.member(jsii_name="attrGlobalResolverId")
    def attr_global_resolver_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: GlobalResolverId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGlobalResolverId"))

    @builtins.property
    @jsii.member(jsii_name="attrIPv4Addresses")
    def attr_i_pv4_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: IPv4Addresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrIPv4Addresses"))

    @builtins.property
    @jsii.member(jsii_name="attrIPv6Addresses")
    def attr_i_pv6_addresses(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: IPv6Addresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrIPv6Addresses"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="globalResolverRef")
    def global_resolver_ref(self) -> "_GlobalResolverReference_f82bf8b1":
        '''A reference to a GlobalResolver resource.'''
        return typing.cast("_GlobalResolverReference_f82bf8b1", jsii.get(self, "globalResolverRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b0b88d079d01a31e037efeb79e04d03e3f7da29d7941fcccd8de7adbc9b7b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f3bb4b7d0ee02337d106ffbb96ceb04b04cbdde26596fba5617fee79d9198a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5a9c32e120d7e538e67450c181d308e40dff28ea7634fa76434845ad86845f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6686dda6b1be0eda3a74814ee144f9054a0a0fb013f592f6a0cc1f775872d119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9433c2948ee91ed9b3d248955e1206060c64874da48552c56de02de2bc0c6413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="observabilityRegion")
    def observability_region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "observabilityRegion"))

    @observability_region.setter
    def observability_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1883445fceb6de947e1368c84caea5d6c108abbb4e30a6ac67ca90321709662b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "observabilityRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d6cd6a2341e5166e822efce47afc74733f3e9cc782b993eb7d84b7f054a88d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnGlobalResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "regions": "regions",
        "client_token": "clientToken",
        "description": "description",
        "ip_address_type": "ipAddressType",
        "observability_region": "observabilityRegion",
        "tags": "tags",
    },
)
class CfnGlobalResolverProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        regions: typing.Sequence[builtins.str],
        client_token: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        ip_address_type: typing.Optional[builtins.str] = None,
        observability_region: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGlobalResolver``.

        :param name: 
        :param regions: 
        :param client_token: 
        :param description: 
        :param ip_address_type: 
        :param observability_region: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_global_resolver_props = route53globalresolver.CfnGlobalResolverProps(
                name="name",
                regions=["regions"],
            
                # the properties below are optional
                client_token="clientToken",
                description="description",
                ip_address_type="ipAddressType",
                observability_region="observabilityRegion",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d94144306c30ab10b09fa1fa56f25eff66f288d01a5a061658e600765089cf3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument observability_region", value=observability_region, expected_type=type_hints["observability_region"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "regions": regions,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if description is not None:
            self._values["description"] = description
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if observability_region is not None:
            self._values["observability_region"] = observability_region
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regions(self) -> typing.List[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-regions
        '''
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def observability_region(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-observabilityregion
        '''
        result = self._values.get("observability_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-globalresolver.html#cfn-route53globalresolver-globalresolver-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IHostedZoneAssociationRef_f6749a8d)
class CfnHostedZoneAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnHostedZoneAssociation",
):
    '''Resource schema for AWS::Route53GlobalResolver::HostedZoneAssociation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-hostedzoneassociation.html
    :cloudformationResource: AWS::Route53GlobalResolver::HostedZoneAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53globalresolver as route53globalresolver
        
        cfn_hosted_zone_association = route53globalresolver.CfnHostedZoneAssociation(self, "MyCfnHostedZoneAssociation",
            hosted_zone_id="hostedZoneId",
            name="name",
            resource_arn="resourceArn"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
        name: builtins.str,
        resource_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Route53GlobalResolver::HostedZoneAssociation``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param hosted_zone_id: 
        :param name: 
        :param resource_arn: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86aca272912e382b469d5a6ebe30c8093c67fe4df8cac87a140c06ca9ba524ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHostedZoneAssociationProps(
            hosted_zone_id=hosted_zone_id, name=name, resource_arn=resource_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnHostedZoneAssociation")
    @builtins.classmethod
    def is_cfn_hosted_zone_association(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnHostedZoneAssociation.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee8a96623207e3c6d861f24a1f5272f8588cf8154f9d588b4ed1fa985bd315e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnHostedZoneAssociation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__477a0e76bde0ecc042a52896ee90e244d93fb83398556b5b877c940edcc781de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3435c2d6adb1a07d9bbdea5368e2a8f54d7e26c2d6da1de3222a61e3469df57b)
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
    @jsii.member(jsii_name="attrHostedZoneAssociationId")
    def attr_hosted_zone_association_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: HostedZoneAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostedZoneAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="attrHostedZoneName")
    def attr_hosted_zone_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: HostedZoneName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostedZoneName"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="hostedZoneAssociationRef")
    def hosted_zone_association_ref(self) -> "_HostedZoneAssociationReference_75cb03f5":
        '''A reference to a HostedZoneAssociation resource.'''
        return typing.cast("_HostedZoneAssociationReference_75cb03f5", jsii.get(self, "hostedZoneAssociationRef"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbb5a6954a76832bfa5c14791783f4bc2c24e7208fd17b213381ac5552bd6465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfd94f6bc8ede6ffd2798c84c13a8a4816676b86e722597b58bd30d0910ebbab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52611d2cdfc48b952a63f9e11c8048c2c21550a2505957903d99faa929e34c15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53globalresolver.CfnHostedZoneAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_id": "hostedZoneId",
        "name": "name",
        "resource_arn": "resourceArn",
    },
)
class CfnHostedZoneAssociationProps:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        name: builtins.str,
        resource_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnHostedZoneAssociation``.

        :param hosted_zone_id: 
        :param name: 
        :param resource_arn: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-hostedzoneassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53globalresolver as route53globalresolver
            
            cfn_hosted_zone_association_props = route53globalresolver.CfnHostedZoneAssociationProps(
                hosted_zone_id="hostedZoneId",
                name="name",
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f301180b16ce475b31d287759a5bcf71bfb875fbbf65e153c81976641304316d)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "name": name,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-hostedzoneassociation.html#cfn-route53globalresolver-hostedzoneassociation-hostedzoneid
        '''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-hostedzoneassociation.html#cfn-route53globalresolver-hostedzoneassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53globalresolver-hostedzoneassociation.html#cfn-route53globalresolver-hostedzoneassociation-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostedZoneAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessSource",
    "CfnAccessSourceProps",
    "CfnAccessToken",
    "CfnAccessTokenProps",
    "CfnDnsView",
    "CfnDnsViewProps",
    "CfnFirewallDomainList",
    "CfnFirewallDomainListProps",
    "CfnFirewallRule",
    "CfnFirewallRuleProps",
    "CfnGlobalResolver",
    "CfnGlobalResolverProps",
    "CfnHostedZoneAssociation",
    "CfnHostedZoneAssociationProps",
]

publication.publish()

def _typecheckingstub__1e26e227e8b54f12cab6d99359743bad21bc5f9bb5d04e4c30fc1b3deea2b91d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cidr: builtins.str,
    dns_view_id: builtins.str,
    protocol: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e03274618d5d2e93650f0be017e364784edc53006e272e106bb7cf38a7cfaf1(
    resource: _IAccessSourceRef_1db97119,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05603aac4da0889d167bb1387eabd33b6fecfac386e077073db14ba1ac5905d1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ccd8f9ba4eef07d166aece09cb53abc570035042a9b8212d3c028dac9d57409(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7123f2aaf7effe01c513196a1156c24fcfd15a53b9d6db929d6bc3a36f3f9471(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc669c1f788dfe513d35b84e76f6ab663967b55f657ce94818e351138c4e9dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b8ccb772e4fc895f76707e5058eeed752ae1f36d776224e2363c15bd318c2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde1a183981630a3fffc38ddff8a3f6febb6937b3c5949799453e30cbc7310a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ff0bae281a0a2532fce6d0ea5b7198a748c1e755f444a05f921f6932093028(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05f8e72a9b2ca81a1f33202e71d4ddca48f4342a704a4421f5b0bb4a40fd1ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41c9d2a0bbfe1d84266d379f49840e2dab332041118d9c1df05a2b456cced6d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0ecd9ff59b993b152a551949ae0b2ad042a6ef742c7fab5e74e60e49795dfd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2356855e49ab75da15cc0328069114313fafa0ff86a20d803b7c2be30c7b45(
    *,
    cidr: builtins.str,
    dns_view_id: builtins.str,
    protocol: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ba20f227121b366c42a9c098db67c39a85a9415f50b946dafad20209022b25(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dns_view_id: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    expires_at: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd9a24451fa5b1382911f1e89ae8067a394ff17c9e74aa6e7f52032fd523cc4(
    resource: _IAccessTokenRef_b08178a7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c38c4bd39315438fbb6061db5804f6f55b7a3f1f8bc3fafa525198836eda5ee1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04ef7a912a877531ae4298ea3f8bbf620dd209ba529c38ca67e6707431b584f8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882301402f4fbd8cac64cf2b9e02bcccd51a3c37d41129fc2914c0f40a7d0ee2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1efd29213f22f5d27bdc1cc739dc8378215bc1eaa8894d05398b746c14b5f58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b704c3f64f2cbd55623b131a5af32dc3d8408a339cad0a16a258b0b8a6cccd09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e6d199b63f268f056a2ec1768cde0c3075bc16623f4a5462963cebef8eed62(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceddf2530916a54b784424c359bbba7fb09d8ec8158118d8d6aaeac3513a2101(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605d3f9cf55610f9b074c8814ec1cb33c3e2e73976521352747a92132b766b4c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c886d3ce6884b3f680b0cccc4106854b2a78d4361077ac1940c2e5c6f37ece2(
    *,
    dns_view_id: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    expires_at: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9f4752adcdd6e72c7cd34b7681a4f92727b18fe01a3115c9611f42ee1775ee6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    global_resolver_id: builtins.str,
    name: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    dnssec_validation: typing.Optional[builtins.str] = None,
    edns_client_subnet: typing.Optional[builtins.str] = None,
    firewall_rules_fail_open: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc442efadfd1cffb86a82368e040b1113a0526c334e4ce810913bd4849e3b852(
    resource: _IDnsViewRef_cc315308,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b490856e9824a822de72942079e730d873721191b46d3867b0115aa63a0f0cb6(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49489960a5f211b491107ec4bfc87ea246355380d030e95060c24632c1e5bba(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d035f1bbfd9ba07f376bc462754e909ab7a57439d520db08f74c23003e35854d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e41cd1cd94d8741ef44561111afff11465dce8754456d1c2c0987fe154e2e9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d66be568aecf026fd401f159dca8b5c47f937b6ff71b44ac4c62ce5d7a3f589(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8ff87145e371ec40ce7499f914ee608c1a6a6b3345c9dd2f5e20b9afa6d8a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e85643d8d0b6b9b57cc22f783f11c470345f91c02f53a59d91316150515984e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b193bb7e640cfea3c0075dc77d73f04a82fb0538fe217dba438b07798d6491(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd9245b51907f66af0986bb95821f553943007f6946c5c3e7a22198fbc4d77e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ac4a77283d843638e97abdf381cd9c32eba01be2e86932b682e2aeee7d1718(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42aed69fa5596ce5731b95fd083072e7a440119751d0837291fec5eb338ad3d2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be47ce035c982759ab526e0529caaa98a67680691f036975711a8fc5d4a202b3(
    *,
    global_resolver_id: builtins.str,
    name: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    dnssec_validation: typing.Optional[builtins.str] = None,
    edns_client_subnet: typing.Optional[builtins.str] = None,
    firewall_rules_fail_open: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e446398d49f5f497ed38c697da2d836f26ea7124989f1921b6b1ef9c449f57d1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    global_resolver_id: builtins.str,
    name: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    domain_file_url: typing.Optional[builtins.str] = None,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19474410306aa2384dcd6bdbcaaadf6b36be962c6d51ee32fe7036441649d773(
    resource: _IFirewallDomainListRef_9fe4e2fb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3156089d9b1f04e4beb6cc12926d5b242645cce554891de44987a1184cd28b1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60fd40c31a28b2d5ab6de007c5f03584b6e7e07b78aedd82036414b78dfc3017(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04ecdcc4256b26330346af2135b7866fb7262051a1a5f74cc45c0981fdb59c69(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b3677ff1f7ee302b88b5cb36d8b2dbb2aede7b72da92bcd6de78284559334f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860763fdea89f756c6c90d95e5087d27a33ed47e8027548e3f61222562908c56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84eca686d85cb13c5722a2285bde95d87f6847e52d5fb465ef94942de5197cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eea47993f183bb17d4d3b44850ff6b8583ee9017b513c8fbe2776ab8cda9579(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef515883247b8072fc18a08dec90a59230966b8a0efa777e4fe6af7cb0d9fa8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__070c5ecfb715828169cae58ca6834d54dfb1f94ad146cf4c311bdabeb5336560(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a595596d23fe50bb26e322a036c3596920a5ce2e75e91f14b2a5eba1065e2645(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d198a7489a5e52354a6e7aa2cc4b677925fb253ffe4562fee89db32fca188fc(
    *,
    global_resolver_id: builtins.str,
    name: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    domain_file_url: typing.Optional[builtins.str] = None,
    domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6583b9c78ed44e0741a9157f77381d7e0d146fddaecf32085a2ec279acc3c2e6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: builtins.str,
    dns_view_id: builtins.str,
    name: builtins.str,
    block_override_dns_type: typing.Optional[builtins.str] = None,
    block_override_domain: typing.Optional[builtins.str] = None,
    block_override_ttl: typing.Optional[jsii.Number] = None,
    block_response: typing.Optional[builtins.str] = None,
    client_token: typing.Optional[builtins.str] = None,
    confidence_threshold: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    dns_advanced_protection: typing.Optional[builtins.str] = None,
    firewall_domain_list_id: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    q_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33d1a1948e0858fe4536c23a3492cecb0c4fc7517de4ac60ac9e802720c30e0(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e62d2bd41c552313dfa6ecccf16fcc964601515f9f78a4232df1e5c2385568(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b03320d9333ed0a6f4578084157955464912cd3481ba4e258fa9e6e4403f41b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df53bebd126372c73837119fcb380b046153e8eba79d94322613b67d6538d1ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebf9dd4c773dfb353399502591dc55c1f9260be931a82f6c050e1cda4772f95e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a296c65c3bba86a2f84d9b49148c39a35f4cc07d53258ba1189913bdb9db65c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d2a00b7a7f3c8557c4d29a9084b0056e619989cad0c6d5e535086ee266f06b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2dcc3ab9abeb84a1233e0ed3dfc8a4ad7cf0ee0476b7e6508dfec7ebb39ffd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__623f287e789666287232f4cdcfd802c7bca918fb304365a548202f5bf55a6253(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c6e5756daa4edb39cdc5dd742884a967e531ef9f34ba1facf352ec6677ae832(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab86dd47e7897a324abbcaeec22c0d6eeaf3762deeac7bc9a309d0151a9b81ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d37fc845269f164fa0cf3e48990af182d9dc1686dbd3b7dbb7701b86396aa39(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60c174302408bcfaa2815c8a3f8096e3837ee1bf6e8a7b7e38e29dfc2a3616c5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b77040a4e57b230dd8671210a76850893595b710bff3f20978a08200ddbb8ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112a6c71e13eebf15e9566e12ee5442386f646f6017070613764c16fbd87a1ea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac571aadf8e72a4bf0c10c3647247c011960f4fd372b4f5155fdf082977ca7ac(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af647b4d580894203899eba8b4aa5d78ceb0fa976874ea177ea5eb4020a98154(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed0b3cd14f9eb8ed481db1c0eb01b2961bc4aaf2fa720f8f0998729ce22ea47e(
    *,
    action: builtins.str,
    dns_view_id: builtins.str,
    name: builtins.str,
    block_override_dns_type: typing.Optional[builtins.str] = None,
    block_override_domain: typing.Optional[builtins.str] = None,
    block_override_ttl: typing.Optional[jsii.Number] = None,
    block_response: typing.Optional[builtins.str] = None,
    client_token: typing.Optional[builtins.str] = None,
    confidence_threshold: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    dns_advanced_protection: typing.Optional[builtins.str] = None,
    firewall_domain_list_id: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    q_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da7e79855025c0b30f6623575b9427a70db31e48fe2bbbcb7afe985433e2ca60(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    regions: typing.Sequence[builtins.str],
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    observability_region: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586f8599fc720ab431e4bbff7f3f0e54c43a9c6e4c5e61ec51598ee274df065e(
    resource: _IGlobalResolverRef_e2deb39d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1480ed04d9a64f793fbcb9b37f7bf0d263f0561598d9eae1efe6f4fd99627dad(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d150f595f1701196870035d68c5f82f675b3f5b2179dcbcd83ed1ced124d77(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0846fb5dc8a488f6d34e544d26c231a88b4a157f5b038a038db0139214418d2b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b0b88d079d01a31e037efeb79e04d03e3f7da29d7941fcccd8de7adbc9b7b1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3bb4b7d0ee02337d106ffbb96ceb04b04cbdde26596fba5617fee79d9198a9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5a9c32e120d7e538e67450c181d308e40dff28ea7634fa76434845ad86845f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6686dda6b1be0eda3a74814ee144f9054a0a0fb013f592f6a0cc1f775872d119(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9433c2948ee91ed9b3d248955e1206060c64874da48552c56de02de2bc0c6413(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1883445fceb6de947e1368c84caea5d6c108abbb4e30a6ac67ca90321709662b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d6cd6a2341e5166e822efce47afc74733f3e9cc782b993eb7d84b7f054a88d7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d94144306c30ab10b09fa1fa56f25eff66f288d01a5a061658e600765089cf3(
    *,
    name: builtins.str,
    regions: typing.Sequence[builtins.str],
    client_token: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    ip_address_type: typing.Optional[builtins.str] = None,
    observability_region: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86aca272912e382b469d5a6ebe30c8093c67fe4df8cac87a140c06ca9ba524ef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone_id: builtins.str,
    name: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee8a96623207e3c6d861f24a1f5272f8588cf8154f9d588b4ed1fa985bd315e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__477a0e76bde0ecc042a52896ee90e244d93fb83398556b5b877c940edcc781de(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3435c2d6adb1a07d9bbdea5368e2a8f54d7e26c2d6da1de3222a61e3469df57b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb5a6954a76832bfa5c14791783f4bc2c24e7208fd17b213381ac5552bd6465(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfd94f6bc8ede6ffd2798c84c13a8a4816676b86e722597b58bd30d0910ebbab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52611d2cdfc48b952a63f9e11c8048c2c21550a2505957903d99faa929e34c15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f301180b16ce475b31d287759a5bcf71bfb875fbbf65e153c81976641304316d(
    *,
    hosted_zone_id: builtins.str,
    name: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

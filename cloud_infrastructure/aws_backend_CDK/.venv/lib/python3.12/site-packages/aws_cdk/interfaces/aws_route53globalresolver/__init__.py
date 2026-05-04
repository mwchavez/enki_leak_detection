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

from ..._jsii import *

import constructs as _constructs_77d1e7e8
from .. import IEnvironmentAware as _IEnvironmentAware_f39049ee


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.AccessSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_source_arn": "accessSourceArn",
        "access_source_id": "accessSourceId",
    },
)
class AccessSourceReference:
    def __init__(
        self,
        *,
        access_source_arn: builtins.str,
        access_source_id: builtins.str,
    ) -> None:
        '''A reference to a AccessSource resource.

        :param access_source_arn: The ARN of the AccessSource resource.
        :param access_source_id: The AccessSourceId of the AccessSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            access_source_reference = interfaces_route53globalresolver.AccessSourceReference(
                access_source_arn="accessSourceArn",
                access_source_id="accessSourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f0ce7d97f9a2c92f3f5ab1e18d9fc6e63b320e0328b2f33f2c7f13a7fa617d)
            check_type(argname="argument access_source_arn", value=access_source_arn, expected_type=type_hints["access_source_arn"])
            check_type(argname="argument access_source_id", value=access_source_id, expected_type=type_hints["access_source_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_source_arn": access_source_arn,
            "access_source_id": access_source_id,
        }

    @builtins.property
    def access_source_arn(self) -> builtins.str:
        '''The ARN of the AccessSource resource.'''
        result = self._values.get("access_source_arn")
        assert result is not None, "Required property 'access_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_source_id(self) -> builtins.str:
        '''The AccessSourceId of the AccessSource resource.'''
        result = self._values.get("access_source_id")
        assert result is not None, "Required property 'access_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.AccessTokenReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_token_arn": "accessTokenArn",
        "access_token_id": "accessTokenId",
    },
)
class AccessTokenReference:
    def __init__(
        self,
        *,
        access_token_arn: builtins.str,
        access_token_id: builtins.str,
    ) -> None:
        '''A reference to a AccessToken resource.

        :param access_token_arn: The ARN of the AccessToken resource.
        :param access_token_id: The AccessTokenId of the AccessToken resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            access_token_reference = interfaces_route53globalresolver.AccessTokenReference(
                access_token_arn="accessTokenArn",
                access_token_id="accessTokenId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98cee02a2dfca9b88f3bd39bb0d554f4c48f820540347722509412f153f73b06)
            check_type(argname="argument access_token_arn", value=access_token_arn, expected_type=type_hints["access_token_arn"])
            check_type(argname="argument access_token_id", value=access_token_id, expected_type=type_hints["access_token_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_token_arn": access_token_arn,
            "access_token_id": access_token_id,
        }

    @builtins.property
    def access_token_arn(self) -> builtins.str:
        '''The ARN of the AccessToken resource.'''
        result = self._values.get("access_token_arn")
        assert result is not None, "Required property 'access_token_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token_id(self) -> builtins.str:
        '''The AccessTokenId of the AccessToken resource.'''
        result = self._values.get("access_token_id")
        assert result is not None, "Required property 'access_token_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessTokenReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.DnsViewReference",
    jsii_struct_bases=[],
    name_mapping={"dns_view_arn": "dnsViewArn", "dns_view_id": "dnsViewId"},
)
class DnsViewReference:
    def __init__(
        self,
        *,
        dns_view_arn: builtins.str,
        dns_view_id: builtins.str,
    ) -> None:
        '''A reference to a DnsView resource.

        :param dns_view_arn: The ARN of the DnsView resource.
        :param dns_view_id: The DnsViewId of the DnsView resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            dns_view_reference = interfaces_route53globalresolver.DnsViewReference(
                dns_view_arn="dnsViewArn",
                dns_view_id="dnsViewId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b167048e4403682296955837adb0768b6706101640638d7d952381cf815ad7)
            check_type(argname="argument dns_view_arn", value=dns_view_arn, expected_type=type_hints["dns_view_arn"])
            check_type(argname="argument dns_view_id", value=dns_view_id, expected_type=type_hints["dns_view_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dns_view_arn": dns_view_arn,
            "dns_view_id": dns_view_id,
        }

    @builtins.property
    def dns_view_arn(self) -> builtins.str:
        '''The ARN of the DnsView resource.'''
        result = self._values.get("dns_view_arn")
        assert result is not None, "Required property 'dns_view_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_view_id(self) -> builtins.str:
        '''The DnsViewId of the DnsView resource.'''
        result = self._values.get("dns_view_id")
        assert result is not None, "Required property 'dns_view_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsViewReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.FirewallDomainListReference",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_domain_list_arn": "firewallDomainListArn",
        "firewall_domain_list_id": "firewallDomainListId",
    },
)
class FirewallDomainListReference:
    def __init__(
        self,
        *,
        firewall_domain_list_arn: builtins.str,
        firewall_domain_list_id: builtins.str,
    ) -> None:
        '''A reference to a FirewallDomainList resource.

        :param firewall_domain_list_arn: The ARN of the FirewallDomainList resource.
        :param firewall_domain_list_id: The FirewallDomainListId of the FirewallDomainList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            firewall_domain_list_reference = interfaces_route53globalresolver.FirewallDomainListReference(
                firewall_domain_list_arn="firewallDomainListArn",
                firewall_domain_list_id="firewallDomainListId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__804423d53d3464a344630b833888fe53bd940428ecfda86c08f66df6fba11b2f)
            check_type(argname="argument firewall_domain_list_arn", value=firewall_domain_list_arn, expected_type=type_hints["firewall_domain_list_arn"])
            check_type(argname="argument firewall_domain_list_id", value=firewall_domain_list_id, expected_type=type_hints["firewall_domain_list_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_domain_list_arn": firewall_domain_list_arn,
            "firewall_domain_list_id": firewall_domain_list_id,
        }

    @builtins.property
    def firewall_domain_list_arn(self) -> builtins.str:
        '''The ARN of the FirewallDomainList resource.'''
        result = self._values.get("firewall_domain_list_arn")
        assert result is not None, "Required property 'firewall_domain_list_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_domain_list_id(self) -> builtins.str:
        '''The FirewallDomainListId of the FirewallDomainList resource.'''
        result = self._values.get("firewall_domain_list_id")
        assert result is not None, "Required property 'firewall_domain_list_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallDomainListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.FirewallRuleReference",
    jsii_struct_bases=[],
    name_mapping={"firewall_rule_id": "firewallRuleId"},
)
class FirewallRuleReference:
    def __init__(self, *, firewall_rule_id: builtins.str) -> None:
        '''A reference to a FirewallRule resource.

        :param firewall_rule_id: The FirewallRuleId of the FirewallRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            firewall_rule_reference = interfaces_route53globalresolver.FirewallRuleReference(
                firewall_rule_id="firewallRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f0b5a545a9a92094e9582b077cad510fb651ce72ecc1efff50098781a03e1d1)
            check_type(argname="argument firewall_rule_id", value=firewall_rule_id, expected_type=type_hints["firewall_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_rule_id": firewall_rule_id,
        }

    @builtins.property
    def firewall_rule_id(self) -> builtins.str:
        '''The FirewallRuleId of the FirewallRule resource.'''
        result = self._values.get("firewall_rule_id")
        assert result is not None, "Required property 'firewall_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.GlobalResolverReference",
    jsii_struct_bases=[],
    name_mapping={
        "global_resolver_arn": "globalResolverArn",
        "global_resolver_id": "globalResolverId",
    },
)
class GlobalResolverReference:
    def __init__(
        self,
        *,
        global_resolver_arn: builtins.str,
        global_resolver_id: builtins.str,
    ) -> None:
        '''A reference to a GlobalResolver resource.

        :param global_resolver_arn: The ARN of the GlobalResolver resource.
        :param global_resolver_id: The GlobalResolverId of the GlobalResolver resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            global_resolver_reference = interfaces_route53globalresolver.GlobalResolverReference(
                global_resolver_arn="globalResolverArn",
                global_resolver_id="globalResolverId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1141a3caf74fb76b667a399fd59cfff0e1d3f9c4a87c1003c9b7d37aeda010)
            check_type(argname="argument global_resolver_arn", value=global_resolver_arn, expected_type=type_hints["global_resolver_arn"])
            check_type(argname="argument global_resolver_id", value=global_resolver_id, expected_type=type_hints["global_resolver_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_resolver_arn": global_resolver_arn,
            "global_resolver_id": global_resolver_id,
        }

    @builtins.property
    def global_resolver_arn(self) -> builtins.str:
        '''The ARN of the GlobalResolver resource.'''
        result = self._values.get("global_resolver_arn")
        assert result is not None, "Required property 'global_resolver_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_resolver_id(self) -> builtins.str:
        '''The GlobalResolverId of the GlobalResolver resource.'''
        result = self._values.get("global_resolver_id")
        assert result is not None, "Required property 'global_resolver_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalResolverReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.HostedZoneAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_association_id": "hostedZoneAssociationId"},
)
class HostedZoneAssociationReference:
    def __init__(self, *, hosted_zone_association_id: builtins.str) -> None:
        '''A reference to a HostedZoneAssociation resource.

        :param hosted_zone_association_id: The HostedZoneAssociationId of the HostedZoneAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53globalresolver as interfaces_route53globalresolver
            
            hosted_zone_association_reference = interfaces_route53globalresolver.HostedZoneAssociationReference(
                hosted_zone_association_id="hostedZoneAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40a4f2751aeb02ce2d4be9c6762ddcf84547cfee1e971d2cb868e2125992a24)
            check_type(argname="argument hosted_zone_association_id", value=hosted_zone_association_id, expected_type=type_hints["hosted_zone_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_association_id": hosted_zone_association_id,
        }

    @builtins.property
    def hosted_zone_association_id(self) -> builtins.str:
        '''The HostedZoneAssociationId of the HostedZoneAssociation resource.'''
        result = self._values.get("hosted_zone_association_id")
        assert result is not None, "Required property 'hosted_zone_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IAccessSourceRef"
)
class IAccessSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessSourceRef")
    def access_source_ref(self) -> "AccessSourceReference":
        '''(experimental) A reference to a AccessSource resource.

        :stability: experimental
        '''
        ...


class _IAccessSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IAccessSourceRef"

    @builtins.property
    @jsii.member(jsii_name="accessSourceRef")
    def access_source_ref(self) -> "AccessSourceReference":
        '''(experimental) A reference to a AccessSource resource.

        :stability: experimental
        '''
        return typing.cast("AccessSourceReference", jsii.get(self, "accessSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessSourceRef).__jsii_proxy_class__ = lambda : _IAccessSourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IAccessTokenRef"
)
class IAccessTokenRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessToken.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessTokenRef")
    def access_token_ref(self) -> "AccessTokenReference":
        '''(experimental) A reference to a AccessToken resource.

        :stability: experimental
        '''
        ...


class _IAccessTokenRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessToken.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IAccessTokenRef"

    @builtins.property
    @jsii.member(jsii_name="accessTokenRef")
    def access_token_ref(self) -> "AccessTokenReference":
        '''(experimental) A reference to a AccessToken resource.

        :stability: experimental
        '''
        return typing.cast("AccessTokenReference", jsii.get(self, "accessTokenRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessTokenRef).__jsii_proxy_class__ = lambda : _IAccessTokenRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IDnsViewRef"
)
class IDnsViewRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DnsView.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dnsViewRef")
    def dns_view_ref(self) -> "DnsViewReference":
        '''(experimental) A reference to a DnsView resource.

        :stability: experimental
        '''
        ...


class _IDnsViewRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DnsView.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IDnsViewRef"

    @builtins.property
    @jsii.member(jsii_name="dnsViewRef")
    def dns_view_ref(self) -> "DnsViewReference":
        '''(experimental) A reference to a DnsView resource.

        :stability: experimental
        '''
        return typing.cast("DnsViewReference", jsii.get(self, "dnsViewRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDnsViewRef).__jsii_proxy_class__ = lambda : _IDnsViewRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IFirewallDomainListRef"
)
class IFirewallDomainListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallDomainList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListRef")
    def firewall_domain_list_ref(self) -> "FirewallDomainListReference":
        '''(experimental) A reference to a FirewallDomainList resource.

        :stability: experimental
        '''
        ...


class _IFirewallDomainListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallDomainList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IFirewallDomainListRef"

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListRef")
    def firewall_domain_list_ref(self) -> "FirewallDomainListReference":
        '''(experimental) A reference to a FirewallDomainList resource.

        :stability: experimental
        '''
        return typing.cast("FirewallDomainListReference", jsii.get(self, "firewallDomainListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallDomainListRef).__jsii_proxy_class__ = lambda : _IFirewallDomainListRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IFirewallRuleRef"
)
class IFirewallRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallRuleRef")
    def firewall_rule_ref(self) -> "FirewallRuleReference":
        '''(experimental) A reference to a FirewallRule resource.

        :stability: experimental
        '''
        ...


class _IFirewallRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IFirewallRuleRef"

    @builtins.property
    @jsii.member(jsii_name="firewallRuleRef")
    def firewall_rule_ref(self) -> "FirewallRuleReference":
        '''(experimental) A reference to a FirewallRule resource.

        :stability: experimental
        '''
        return typing.cast("FirewallRuleReference", jsii.get(self, "firewallRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallRuleRef).__jsii_proxy_class__ = lambda : _IFirewallRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IGlobalResolverRef"
)
class IGlobalResolverRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalResolver.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="globalResolverRef")
    def global_resolver_ref(self) -> "GlobalResolverReference":
        '''(experimental) A reference to a GlobalResolver resource.

        :stability: experimental
        '''
        ...


class _IGlobalResolverRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalResolver.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IGlobalResolverRef"

    @builtins.property
    @jsii.member(jsii_name="globalResolverRef")
    def global_resolver_ref(self) -> "GlobalResolverReference":
        '''(experimental) A reference to a GlobalResolver resource.

        :stability: experimental
        '''
        return typing.cast("GlobalResolverReference", jsii.get(self, "globalResolverRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGlobalResolverRef).__jsii_proxy_class__ = lambda : _IGlobalResolverRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53globalresolver.IHostedZoneAssociationRef"
)
class IHostedZoneAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HostedZoneAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hostedZoneAssociationRef")
    def hosted_zone_association_ref(self) -> "HostedZoneAssociationReference":
        '''(experimental) A reference to a HostedZoneAssociation resource.

        :stability: experimental
        '''
        ...


class _IHostedZoneAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HostedZoneAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53globalresolver.IHostedZoneAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="hostedZoneAssociationRef")
    def hosted_zone_association_ref(self) -> "HostedZoneAssociationReference":
        '''(experimental) A reference to a HostedZoneAssociation resource.

        :stability: experimental
        '''
        return typing.cast("HostedZoneAssociationReference", jsii.get(self, "hostedZoneAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostedZoneAssociationRef).__jsii_proxy_class__ = lambda : _IHostedZoneAssociationRefProxy


__all__ = [
    "AccessSourceReference",
    "AccessTokenReference",
    "DnsViewReference",
    "FirewallDomainListReference",
    "FirewallRuleReference",
    "GlobalResolverReference",
    "HostedZoneAssociationReference",
    "IAccessSourceRef",
    "IAccessTokenRef",
    "IDnsViewRef",
    "IFirewallDomainListRef",
    "IFirewallRuleRef",
    "IGlobalResolverRef",
    "IHostedZoneAssociationRef",
]

publication.publish()

def _typecheckingstub__d5f0ce7d97f9a2c92f3f5ab1e18d9fc6e63b320e0328b2f33f2c7f13a7fa617d(
    *,
    access_source_arn: builtins.str,
    access_source_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98cee02a2dfca9b88f3bd39bb0d554f4c48f820540347722509412f153f73b06(
    *,
    access_token_arn: builtins.str,
    access_token_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b167048e4403682296955837adb0768b6706101640638d7d952381cf815ad7(
    *,
    dns_view_arn: builtins.str,
    dns_view_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804423d53d3464a344630b833888fe53bd940428ecfda86c08f66df6fba11b2f(
    *,
    firewall_domain_list_arn: builtins.str,
    firewall_domain_list_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f0b5a545a9a92094e9582b077cad510fb651ce72ecc1efff50098781a03e1d1(
    *,
    firewall_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1141a3caf74fb76b667a399fd59cfff0e1d3f9c4a87c1003c9b7d37aeda010(
    *,
    global_resolver_arn: builtins.str,
    global_resolver_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40a4f2751aeb02ce2d4be9c6762ddcf84547cfee1e971d2cb868e2125992a24(
    *,
    hosted_zone_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessSourceRef, IAccessTokenRef, IDnsViewRef, IFirewallDomainListRef, IFirewallRuleRef, IGlobalResolverRef, IHostedZoneAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])

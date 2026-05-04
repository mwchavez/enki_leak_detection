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
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.AgentSpaceReference",
    jsii_struct_bases=[],
    name_mapping={"agent_space_id": "agentSpaceId"},
)
class AgentSpaceReference:
    def __init__(self, *, agent_space_id: builtins.str) -> None:
        '''A reference to a AgentSpace resource.

        :param agent_space_id: The AgentSpaceId of the AgentSpace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            agent_space_reference = interfaces_securityagent.AgentSpaceReference(
                agent_space_id="agentSpaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80dedf4a214ecd7806d810d851b3baa4ed59f4243fc9421cf67a698090d71a90)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the AgentSpace resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentSpaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId"},
)
class ApplicationReference:
    def __init__(self, *, application_id: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_id: The ApplicationId of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            application_reference = interfaces_securityagent.ApplicationReference(
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a74a282e747b054b47e21cebc993013e9c4a786746342d0a3b2c5e0aa3202151)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Application resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IAgentSpaceRef")
class IAgentSpaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        ...


class _IAgentSpaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IAgentSpaceRef"

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        return typing.cast("AgentSpaceReference", jsii.get(self, "agentSpaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentSpaceRef).__jsii_proxy_class__ = lambda : _IAgentSpaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IApplicationRef")
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.IPentestRef")
class IPentestRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pentest.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pentestRef")
    def pentest_ref(self) -> "PentestReference":
        '''(experimental) A reference to a Pentest resource.

        :stability: experimental
        '''
        ...


class _IPentestRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pentest.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.IPentestRef"

    @builtins.property
    @jsii.member(jsii_name="pentestRef")
    def pentest_ref(self) -> "PentestReference":
        '''(experimental) A reference to a Pentest resource.

        :stability: experimental
        '''
        return typing.cast("PentestReference", jsii.get(self, "pentestRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPentestRef).__jsii_proxy_class__ = lambda : _IPentestRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityagent.ITargetDomainRef")
class ITargetDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TargetDomain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="targetDomainRef")
    def target_domain_ref(self) -> "TargetDomainReference":
        '''(experimental) A reference to a TargetDomain resource.

        :stability: experimental
        '''
        ...


class _ITargetDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TargetDomain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityagent.ITargetDomainRef"

    @builtins.property
    @jsii.member(jsii_name="targetDomainRef")
    def target_domain_ref(self) -> "TargetDomainReference":
        '''(experimental) A reference to a TargetDomain resource.

        :stability: experimental
        '''
        return typing.cast("TargetDomainReference", jsii.get(self, "targetDomainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITargetDomainRef).__jsii_proxy_class__ = lambda : _ITargetDomainRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.PentestReference",
    jsii_struct_bases=[],
    name_mapping={"agent_space_id": "agentSpaceId", "pentest_id": "pentestId"},
)
class PentestReference:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        pentest_id: builtins.str,
    ) -> None:
        '''A reference to a Pentest resource.

        :param agent_space_id: The AgentSpaceId of the Pentest resource.
        :param pentest_id: The PentestId of the Pentest resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            pentest_reference = interfaces_securityagent.PentestReference(
                agent_space_id="agentSpaceId",
                pentest_id="pentestId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1adadeed55a2da3dec371b1cd0d9d6711c5766263216b8243bedad0c33c21f40)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument pentest_id", value=pentest_id, expected_type=type_hints["pentest_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "pentest_id": pentest_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the Pentest resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pentest_id(self) -> builtins.str:
        '''The PentestId of the Pentest resource.'''
        result = self._values.get("pentest_id")
        assert result is not None, "Required property 'pentest_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PentestReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityagent.TargetDomainReference",
    jsii_struct_bases=[],
    name_mapping={"target_domain_id": "targetDomainId"},
)
class TargetDomainReference:
    def __init__(self, *, target_domain_id: builtins.str) -> None:
        '''A reference to a TargetDomain resource.

        :param target_domain_id: The TargetDomainId of the TargetDomain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityagent as interfaces_securityagent
            
            target_domain_reference = interfaces_securityagent.TargetDomainReference(
                target_domain_id="targetDomainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a75929dd06e26264ee7207057716102e007a7dbc3560e3d13e615050563c4f66)
            check_type(argname="argument target_domain_id", value=target_domain_id, expected_type=type_hints["target_domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_domain_id": target_domain_id,
        }

    @builtins.property
    def target_domain_id(self) -> builtins.str:
        '''The TargetDomainId of the TargetDomain resource.'''
        result = self._values.get("target_domain_id")
        assert result is not None, "Required property 'target_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetDomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentSpaceReference",
    "ApplicationReference",
    "IAgentSpaceRef",
    "IApplicationRef",
    "IPentestRef",
    "ITargetDomainRef",
    "PentestReference",
    "TargetDomainReference",
]

publication.publish()

def _typecheckingstub__80dedf4a214ecd7806d810d851b3baa4ed59f4243fc9421cf67a698090d71a90(
    *,
    agent_space_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74a282e747b054b47e21cebc993013e9c4a786746342d0a3b2c5e0aa3202151(
    *,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1adadeed55a2da3dec371b1cd0d9d6711c5766263216b8243bedad0c33c21f40(
    *,
    agent_space_id: builtins.str,
    pentest_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a75929dd06e26264ee7207057716102e007a7dbc3560e3d13e615050563c4f66(
    *,
    target_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentSpaceRef, IApplicationRef, IPentestRef, ITargetDomainRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])

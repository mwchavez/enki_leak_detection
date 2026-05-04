r'''
# AWS::Interconnect Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_interconnect as interconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Interconnect construct libraries](https://constructs.dev/search?q=interconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Interconnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Interconnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Interconnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Interconnect.html).

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
from ..interfaces.aws_interconnect import (
    ConnectionReference as _ConnectionReference_047fec56,
    IConnectionRef as _IConnectionRef_0c40873a,
)


@jsii.implements(_IInspectable_c2943556, _IConnectionRef_0c40873a, _ITaggableV2_4e6798f8)
class CfnConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_interconnect.CfnConnection",
):
    '''Resource Type definition for AWS::Interconnect::Connection.

    Creates a managed network connection between AWS and a partner cloud service provider.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html
    :cloudformationResource: AWS::Interconnect::Connection
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_interconnect as interconnect
        
        cfn_connection = interconnect.CfnConnection(self, "MyCfnConnection",
            attach_point=interconnect.CfnConnection.AttachPointProperty(
                arn="arn",
                direct_connect_gateway="directConnectGateway"
            ),
        
            # the properties below are optional
            activation_key="activationKey",
            bandwidth="bandwidth",
            description="description",
            environment_id="environmentId",
            remote_owner_account="remoteOwnerAccount",
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
        attach_point: typing.Union["_IResolvable_da3f097b", typing.Union["CfnConnection.AttachPointProperty", typing.Dict[builtins.str, typing.Any]]],
        activation_key: typing.Optional[builtins.str] = None,
        bandwidth: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        environment_id: typing.Optional[builtins.str] = None,
        remote_owner_account: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Interconnect::Connection``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param attach_point: The logical attachment point in your AWS network where the managed connection will be connected.
        :param activation_key: The activation key for accepting a connection proposal from a partner CSP. Mutually exclusive with EnvironmentId.
        :param bandwidth: The bandwidth of the connection (e.g., 50Mbps, 1Gbps). Required when creating a connection through AWS.
        :param description: A description of the connection.
        :param environment_id: The ID of the environment for the connection. Required when creating a connection through AWS. Mutually exclusive with ActivationKey.
        :param remote_owner_account: The account ID of the remote owner. Required when creating a connection through AWS.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5322b288c96cd17f9fbc54392674c0dccc316142d9aef64c4d019d598f73055c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectionProps(
            attach_point=attach_point,
            activation_key=activation_key,
            bandwidth=bandwidth,
            description=description,
            environment_id=environment_id,
            remote_owner_account=remote_owner_account,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForConnection")
    @builtins.classmethod
    def arn_for_connection(cls, resource: "_IConnectionRef_0c40873a") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eac7fb1098204c93e8f09de8d57d46dcea98c572828c0892375111cbc6e86887)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForConnection", [resource]))

    @jsii.member(jsii_name="isCfnConnection")
    @builtins.classmethod
    def is_cfn_connection(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnConnection.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed20d9f56b8304bed259a8524a69b8f26458779e2ca99bef55d1392a7e5db03)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnConnection", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e437b186458bf9fb8c98d0499ca7e4edf0b54f2ffdeb0f43b50eb1412622741b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a6b9d3e4f8accf2e72caafac67f65894e3b9732d3f36f395fa94c06b31a3acb)
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
        '''The Amazon Resource Name (ARN) of the connection.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBillingTier")
    def attr_billing_tier(self) -> jsii.Number:
        '''The billing tier for the connection.

        :cloudformationAttribute: BillingTier
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrBillingTier"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionId")
    def attr_connection_id(self) -> builtins.str:
        '''The unique identifier for the connection.

        :cloudformationAttribute: ConnectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccount")
    def attr_owner_account(self) -> builtins.str:
        '''The AWS account ID of the connection owner.

        :cloudformationAttribute: OwnerAccount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccount"))

    @builtins.property
    @jsii.member(jsii_name="attrProvider")
    def attr_provider(self) -> "_IResolvable_da3f097b":
        '''The partner cloud service provider.

        :cloudformationAttribute: Provider
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrProvider"))

    @builtins.property
    @jsii.member(jsii_name="attrSharedId")
    def attr_shared_id(self) -> builtins.str:
        '''The shared identifier for the connection pairing.

        :cloudformationAttribute: SharedId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSharedId"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the connection.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of managed connection.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "_ConnectionReference_047fec56":
        '''A reference to a Connection resource.'''
        return typing.cast("_ConnectionReference_047fec56", jsii.get(self, "connectionRef"))

    @builtins.property
    @jsii.member(jsii_name="attachPoint")
    def attach_point(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnConnection.AttachPointProperty"]:
        '''The logical attachment point in your AWS network where the managed connection will be connected.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnConnection.AttachPointProperty"], jsii.get(self, "attachPoint"))

    @attach_point.setter
    def attach_point(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnConnection.AttachPointProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c80d063ffb285bf84baa9239f57f5d87fc438aa3f332f516b2d65fb1ec4060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachPoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="activationKey")
    def activation_key(self) -> typing.Optional[builtins.str]:
        '''The activation key for accepting a connection proposal from a partner CSP.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activationKey"))

    @activation_key.setter
    def activation_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8664aa84e91d29ecc699ec958553a69e044af56762112f809f6928150178dd21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activationKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bandwidth")
    def bandwidth(self) -> typing.Optional[builtins.str]:
        '''The bandwidth of the connection (e.g., 50Mbps, 1Gbps). Required when creating a connection through AWS.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bandwidth"))

    @bandwidth.setter
    def bandwidth(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce84311dc1fd6f57c60190aa10351aaa48c21fbd679fbe809aefb6f7f25f95d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22080276e4ef4897625bd06a5d83a96f9117b6bbe341f253670dbd3f925a6ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the environment for the connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30654aa478a8acabb61aa09f432905f049778c774ffa31f2c091a08bc504b8e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remoteOwnerAccount")
    def remote_owner_account(self) -> typing.Optional[builtins.str]:
        '''The account ID of the remote owner.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteOwnerAccount"))

    @remote_owner_account.setter
    def remote_owner_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73cac1b1c84365dc4a0fec3786c9b3ed3dc6b6ee937776a548294d2b000bb848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteOwnerAccount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af4d1b1015450c3da10b12c3a7fadb981f662fa7b38e03b6dd1718c96d24949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_interconnect.CfnConnection.AttachPointProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "direct_connect_gateway": "directConnectGateway"},
    )
    class AttachPointProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            direct_connect_gateway: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The logical attachment point in your AWS network where the managed connection will be connected.

            :param arn: The ARN of the resource to attach to.
            :param direct_connect_gateway: The ID of the Direct Connect Gateway to attach to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-interconnect-connection-attachpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_interconnect as interconnect
                
                attach_point_property = interconnect.CfnConnection.AttachPointProperty(
                    arn="arn",
                    direct_connect_gateway="directConnectGateway"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91163144a780d720177f5433f006c18ac1a50c0c43e4683613a19f41d4e14f42)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument direct_connect_gateway", value=direct_connect_gateway, expected_type=type_hints["direct_connect_gateway"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if direct_connect_gateway is not None:
                self._values["direct_connect_gateway"] = direct_connect_gateway

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the resource to attach to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-interconnect-connection-attachpoint.html#cfn-interconnect-connection-attachpoint-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def direct_connect_gateway(self) -> typing.Optional[builtins.str]:
            '''The ID of the Direct Connect Gateway to attach to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-interconnect-connection-attachpoint.html#cfn-interconnect-connection-attachpoint-directconnectgateway
            '''
            result = self._values.get("direct_connect_gateway")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttachPointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_interconnect.CfnConnection.ProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_service_provider": "cloudServiceProvider",
            "last_mile_provider": "lastMileProvider",
        },
    )
    class ProviderProperty:
        def __init__(
            self,
            *,
            cloud_service_provider: typing.Optional[builtins.str] = None,
            last_mile_provider: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The partner cloud service provider.

            :param cloud_service_provider: The name of the cloud service provider.
            :param last_mile_provider: The name of the last mile provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-interconnect-connection-provider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_interconnect as interconnect
                
                provider_property = interconnect.CfnConnection.ProviderProperty(
                    cloud_service_provider="cloudServiceProvider",
                    last_mile_provider="lastMileProvider"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e79d4c39ca0048c28c9c9e4ba53d1acb9c018bfd06ffdae81292fd94a39eeb5f)
                check_type(argname="argument cloud_service_provider", value=cloud_service_provider, expected_type=type_hints["cloud_service_provider"])
                check_type(argname="argument last_mile_provider", value=last_mile_provider, expected_type=type_hints["last_mile_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_service_provider is not None:
                self._values["cloud_service_provider"] = cloud_service_provider
            if last_mile_provider is not None:
                self._values["last_mile_provider"] = last_mile_provider

        @builtins.property
        def cloud_service_provider(self) -> typing.Optional[builtins.str]:
            '''The name of the cloud service provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-interconnect-connection-provider.html#cfn-interconnect-connection-provider-cloudserviceprovider
            '''
            result = self._values.get("cloud_service_provider")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_mile_provider(self) -> typing.Optional[builtins.str]:
            '''The name of the last mile provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-interconnect-connection-provider.html#cfn-interconnect-connection-provider-lastmileprovider
            '''
            result = self._values.get("last_mile_provider")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_interconnect.CfnConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "attach_point": "attachPoint",
        "activation_key": "activationKey",
        "bandwidth": "bandwidth",
        "description": "description",
        "environment_id": "environmentId",
        "remote_owner_account": "remoteOwnerAccount",
        "tags": "tags",
    },
)
class CfnConnectionProps:
    def __init__(
        self,
        *,
        attach_point: typing.Union["_IResolvable_da3f097b", typing.Union["CfnConnection.AttachPointProperty", typing.Dict[builtins.str, typing.Any]]],
        activation_key: typing.Optional[builtins.str] = None,
        bandwidth: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        environment_id: typing.Optional[builtins.str] = None,
        remote_owner_account: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnection``.

        :param attach_point: The logical attachment point in your AWS network where the managed connection will be connected.
        :param activation_key: The activation key for accepting a connection proposal from a partner CSP. Mutually exclusive with EnvironmentId.
        :param bandwidth: The bandwidth of the connection (e.g., 50Mbps, 1Gbps). Required when creating a connection through AWS.
        :param description: A description of the connection.
        :param environment_id: The ID of the environment for the connection. Required when creating a connection through AWS. Mutually exclusive with ActivationKey.
        :param remote_owner_account: The account ID of the remote owner. Required when creating a connection through AWS.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_interconnect as interconnect
            
            cfn_connection_props = interconnect.CfnConnectionProps(
                attach_point=interconnect.CfnConnection.AttachPointProperty(
                    arn="arn",
                    direct_connect_gateway="directConnectGateway"
                ),
            
                # the properties below are optional
                activation_key="activationKey",
                bandwidth="bandwidth",
                description="description",
                environment_id="environmentId",
                remote_owner_account="remoteOwnerAccount",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d36102c989a8481b5f4d0aa7d5e93231210a776a41ca90ae2e2a0c1d6ec24e5)
            check_type(argname="argument attach_point", value=attach_point, expected_type=type_hints["attach_point"])
            check_type(argname="argument activation_key", value=activation_key, expected_type=type_hints["activation_key"])
            check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument remote_owner_account", value=remote_owner_account, expected_type=type_hints["remote_owner_account"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attach_point": attach_point,
        }
        if activation_key is not None:
            self._values["activation_key"] = activation_key
        if bandwidth is not None:
            self._values["bandwidth"] = bandwidth
        if description is not None:
            self._values["description"] = description
        if environment_id is not None:
            self._values["environment_id"] = environment_id
        if remote_owner_account is not None:
            self._values["remote_owner_account"] = remote_owner_account
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def attach_point(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnConnection.AttachPointProperty"]:
        '''The logical attachment point in your AWS network where the managed connection will be connected.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-attachpoint
        '''
        result = self._values.get("attach_point")
        assert result is not None, "Required property 'attach_point' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnConnection.AttachPointProperty"], result)

    @builtins.property
    def activation_key(self) -> typing.Optional[builtins.str]:
        '''The activation key for accepting a connection proposal from a partner CSP.

        Mutually exclusive with EnvironmentId.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-activationkey
        '''
        result = self._values.get("activation_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bandwidth(self) -> typing.Optional[builtins.str]:
        '''The bandwidth of the connection (e.g., 50Mbps, 1Gbps). Required when creating a connection through AWS.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-bandwidth
        '''
        result = self._values.get("bandwidth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the environment for the connection.

        Required when creating a connection through AWS. Mutually exclusive with ActivationKey.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-environmentid
        '''
        result = self._values.get("environment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_owner_account(self) -> typing.Optional[builtins.str]:
        '''The account ID of the remote owner.

        Required when creating a connection through AWS.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-remoteowneraccount
        '''
        result = self._values.get("remote_owner_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-interconnect-connection.html#cfn-interconnect-connection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnection",
    "CfnConnectionProps",
]

publication.publish()

def _typecheckingstub__5322b288c96cd17f9fbc54392674c0dccc316142d9aef64c4d019d598f73055c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    attach_point: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AttachPointProperty, typing.Dict[builtins.str, typing.Any]]],
    activation_key: typing.Optional[builtins.str] = None,
    bandwidth: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    environment_id: typing.Optional[builtins.str] = None,
    remote_owner_account: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eac7fb1098204c93e8f09de8d57d46dcea98c572828c0892375111cbc6e86887(
    resource: _IConnectionRef_0c40873a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed20d9f56b8304bed259a8524a69b8f26458779e2ca99bef55d1392a7e5db03(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e437b186458bf9fb8c98d0499ca7e4edf0b54f2ffdeb0f43b50eb1412622741b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a6b9d3e4f8accf2e72caafac67f65894e3b9732d3f36f395fa94c06b31a3acb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c80d063ffb285bf84baa9239f57f5d87fc438aa3f332f516b2d65fb1ec4060(
    value: typing.Union[_IResolvable_da3f097b, CfnConnection.AttachPointProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8664aa84e91d29ecc699ec958553a69e044af56762112f809f6928150178dd21(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce84311dc1fd6f57c60190aa10351aaa48c21fbd679fbe809aefb6f7f25f95d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22080276e4ef4897625bd06a5d83a96f9117b6bbe341f253670dbd3f925a6ae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30654aa478a8acabb61aa09f432905f049778c774ffa31f2c091a08bc504b8e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cac1b1c84365dc4a0fec3786c9b3ed3dc6b6ee937776a548294d2b000bb848(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af4d1b1015450c3da10b12c3a7fadb981f662fa7b38e03b6dd1718c96d24949(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91163144a780d720177f5433f006c18ac1a50c0c43e4683613a19f41d4e14f42(
    *,
    arn: typing.Optional[builtins.str] = None,
    direct_connect_gateway: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79d4c39ca0048c28c9c9e4ba53d1acb9c018bfd06ffdae81292fd94a39eeb5f(
    *,
    cloud_service_provider: typing.Optional[builtins.str] = None,
    last_mile_provider: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d36102c989a8481b5f4d0aa7d5e93231210a776a41ca90ae2e2a0c1d6ec24e5(
    *,
    attach_point: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnection.AttachPointProperty, typing.Dict[builtins.str, typing.Any]]],
    activation_key: typing.Optional[builtins.str] = None,
    bandwidth: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    environment_id: typing.Optional[builtins.str] = None,
    remote_owner_account: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

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
    jsii_type="aws-cdk-lib.interfaces.aws_s3files.AccessPointReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_point_arn": "accessPointArn",
        "access_point_id": "accessPointId",
    },
)
class AccessPointReference:
    def __init__(
        self,
        *,
        access_point_arn: builtins.str,
        access_point_id: builtins.str,
    ) -> None:
        '''A reference to a AccessPoint resource.

        :param access_point_arn: The ARN of the AccessPoint resource.
        :param access_point_id: The AccessPointId of the AccessPoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3files as interfaces_s3files
            
            access_point_reference = interfaces_s3files.AccessPointReference(
                access_point_arn="accessPointArn",
                access_point_id="accessPointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d8292ad24c15f1775d3f1e33e17d9614177190ac15468bd3a79855e159f7af3)
            check_type(argname="argument access_point_arn", value=access_point_arn, expected_type=type_hints["access_point_arn"])
            check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_point_arn": access_point_arn,
            "access_point_id": access_point_id,
        }

    @builtins.property
    def access_point_arn(self) -> builtins.str:
        '''The ARN of the AccessPoint resource.'''
        result = self._values.get("access_point_arn")
        assert result is not None, "Required property 'access_point_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_point_id(self) -> builtins.str:
        '''The AccessPointId of the AccessPoint resource.'''
        result = self._values.get("access_point_id")
        assert result is not None, "Required property 'access_point_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3files.FileSystemPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId"},
)
class FileSystemPolicyReference:
    def __init__(self, *, file_system_id: builtins.str) -> None:
        '''A reference to a FileSystemPolicy resource.

        :param file_system_id: The FileSystemId of the FileSystemPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3files as interfaces_s3files
            
            file_system_policy_reference = interfaces_s3files.FileSystemPolicyReference(
                file_system_id="fileSystemId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1498df5bb66bb0f2d22bcf24016066a5dfcae1a2a034e34cf7346e4be12d6250)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
        }

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The FileSystemId of the FileSystemPolicy resource.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3files.FileSystemReference",
    jsii_struct_bases=[],
    name_mapping={"file_system_arn": "fileSystemArn"},
)
class FileSystemReference:
    def __init__(self, *, file_system_arn: builtins.str) -> None:
        '''A reference to a FileSystem resource.

        :param file_system_arn: The FileSystemArn of the FileSystem resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3files as interfaces_s3files
            
            file_system_reference = interfaces_s3files.FileSystemReference(
                file_system_arn="fileSystemArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4975421ac615ba8e89a441e928f37471f5d3e89b1d9fc809de8c21f5a6949b5)
            check_type(argname="argument file_system_arn", value=file_system_arn, expected_type=type_hints["file_system_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_arn": file_system_arn,
        }

    @builtins.property
    def file_system_arn(self) -> builtins.str:
        '''The FileSystemArn of the FileSystem resource.'''
        result = self._values.get("file_system_arn")
        assert result is not None, "Required property 'file_system_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3files.IAccessPointRef")
class IAccessPointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        ...


class _IAccessPointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3files.IAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointReference", jsii.get(self, "accessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointRef).__jsii_proxy_class__ = lambda : _IAccessPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3files.IFileSystemPolicyRef")
class IFileSystemPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystemPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fileSystemPolicyRef")
    def file_system_policy_ref(self) -> "FileSystemPolicyReference":
        '''(experimental) A reference to a FileSystemPolicy resource.

        :stability: experimental
        '''
        ...


class _IFileSystemPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystemPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3files.IFileSystemPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="fileSystemPolicyRef")
    def file_system_policy_ref(self) -> "FileSystemPolicyReference":
        '''(experimental) A reference to a FileSystemPolicy resource.

        :stability: experimental
        '''
        return typing.cast("FileSystemPolicyReference", jsii.get(self, "fileSystemPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSystemPolicyRef).__jsii_proxy_class__ = lambda : _IFileSystemPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3files.IFileSystemRef")
class IFileSystemRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystem.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "FileSystemReference":
        '''(experimental) A reference to a FileSystem resource.

        :stability: experimental
        '''
        ...


class _IFileSystemRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystem.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3files.IFileSystemRef"

    @builtins.property
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "FileSystemReference":
        '''(experimental) A reference to a FileSystem resource.

        :stability: experimental
        '''
        return typing.cast("FileSystemReference", jsii.get(self, "fileSystemRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSystemRef).__jsii_proxy_class__ = lambda : _IFileSystemRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3files.IMountTargetRef")
class IMountTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MountTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mountTargetRef")
    def mount_target_ref(self) -> "MountTargetReference":
        '''(experimental) A reference to a MountTarget resource.

        :stability: experimental
        '''
        ...


class _IMountTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MountTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3files.IMountTargetRef"

    @builtins.property
    @jsii.member(jsii_name="mountTargetRef")
    def mount_target_ref(self) -> "MountTargetReference":
        '''(experimental) A reference to a MountTarget resource.

        :stability: experimental
        '''
        return typing.cast("MountTargetReference", jsii.get(self, "mountTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMountTargetRef).__jsii_proxy_class__ = lambda : _IMountTargetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3files.MountTargetReference",
    jsii_struct_bases=[],
    name_mapping={"mount_target_id": "mountTargetId"},
)
class MountTargetReference:
    def __init__(self, *, mount_target_id: builtins.str) -> None:
        '''A reference to a MountTarget resource.

        :param mount_target_id: The MountTargetId of the MountTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3files as interfaces_s3files
            
            mount_target_reference = interfaces_s3files.MountTargetReference(
                mount_target_id="mountTargetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b63fc91aa063efff738c4df140762ee44f66e6f8dd8d49c8884be5693dfc10f)
            check_type(argname="argument mount_target_id", value=mount_target_id, expected_type=type_hints["mount_target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mount_target_id": mount_target_id,
        }

    @builtins.property
    def mount_target_id(self) -> builtins.str:
        '''The MountTargetId of the MountTarget resource.'''
        result = self._values.get("mount_target_id")
        assert result is not None, "Required property 'mount_target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessPointReference",
    "FileSystemPolicyReference",
    "FileSystemReference",
    "IAccessPointRef",
    "IFileSystemPolicyRef",
    "IFileSystemRef",
    "IMountTargetRef",
    "MountTargetReference",
]

publication.publish()

def _typecheckingstub__7d8292ad24c15f1775d3f1e33e17d9614177190ac15468bd3a79855e159f7af3(
    *,
    access_point_arn: builtins.str,
    access_point_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1498df5bb66bb0f2d22bcf24016066a5dfcae1a2a034e34cf7346e4be12d6250(
    *,
    file_system_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4975421ac615ba8e89a441e928f37471f5d3e89b1d9fc809de8c21f5a6949b5(
    *,
    file_system_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b63fc91aa063efff738c4df140762ee44f66e6f8dd8d49c8884be5693dfc10f(
    *,
    mount_target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPointRef, IFileSystemPolicyRef, IFileSystemRef, IMountTargetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])

r'''
# AWS::S3Files Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3files as s3files
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Files construct libraries](https://constructs.dev/search?q=s3files)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Files resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Files.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Files](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Files.html).

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
from ..interfaces.aws_s3files import (
    AccessPointReference as _AccessPointReference_43fd163f,
    FileSystemPolicyReference as _FileSystemPolicyReference_10ae5ae0,
    FileSystemReference as _FileSystemReference_63976c73,
    IAccessPointRef as _IAccessPointRef_95e8d0d6,
    IFileSystemPolicyRef as _IFileSystemPolicyRef_f41c1127,
    IFileSystemRef as _IFileSystemRef_f26f446c,
    IMountTargetRef as _IMountTargetRef_57587992,
    MountTargetReference as _MountTargetReference_c9c3f8f9,
)


@jsii.implements(_IInspectable_c2943556, _IAccessPointRef_95e8d0d6, _ITaggableV2_4e6798f8)
class CfnAccessPoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3files.CfnAccessPoint",
):
    '''Resource Type definition for AWS::S3Files::AccessPoint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html
    :cloudformationResource: AWS::S3Files::AccessPoint
    :exampleMetadata: infused

    Example::

        import aws_cdk as cdk
        import aws_cdk.aws_ec2 as ec2
        import aws_cdk.aws_s3 as s3
        import aws_cdk.aws_s3files as s3files
        
        
        vpc = ec2.Vpc(self, "Vpc")
        
        # Versioning is required — S3 Files relies on object versions for consistency.
        bucket = s3.Bucket(self, "Bucket", versioned=True)
        
        # S3 Files assumes this role to sync data between S3 and the file system.
        role = iam.Role(self, "S3FilesRole",
            assumed_by=iam.ServicePrincipal("elasticfilesystem.amazonaws.com")
        )
        
        # S3 permissions: read/write access to the bucket and objects
        role.add_to_policy(iam.PolicyStatement(
            actions=["s3:ListBucket*"],
            resources=[bucket.bucket_arn]
        ))
        role.add_to_policy(iam.PolicyStatement(
            actions=["s3:AbortMultipartUpload", "s3:DeleteObject", "s3:GetObject*", "s3:List*", "s3:PutObject*"],
            resources=[bucket.arn_for_objects("*")]
        ))
        
        # EventBridge permissions: S3 Files creates rules prefixed "DO-NOT-DELETE-S3-Files"
        # to detect S3 object changes and trigger data synchronization.
        role.add_to_policy(iam.PolicyStatement(
            actions=["events:DeleteRule", "events:DisableRule", "events:EnableRule", "events:PutRule", "events:PutTargets", "events:RemoveTargets"
            ],
            resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/DO-NOT-DELETE-S3-Files*"],
            conditions={"StringEquals": {"events:ManagedBy": "elasticfilesystem.amazonaws.com"}}
        ))
        role.add_to_policy(iam.PolicyStatement(
            actions=["events:DescribeRule", "events:ListRuleNamesByTarget", "events:ListRules", "events:ListTargetsByRule"],
            resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/*"]
        ))
        
        file_system = s3files.CfnFileSystem(self, "S3FilesFs",
            bucket=bucket.bucket_arn,
            role_arn=role.role_arn
        )
        
        sg = ec2.SecurityGroup(self, "MountTargetSG", vpc=vpc)
        
        # Create a mount target in each private subnet so Lambda can reach the file system via NFS.
        vpc.private_subnets.for_each((subnet, i) =>
              new s3files.CfnMountTarget(this, `MountTarget${i}`, {
                fileSystemId: fileSystem.attrFileSystemId,
                subnetId: subnet.subnetId,
                securityGroups: [sg.securityGroupId],
              }))
        
        # The access point defines the POSIX identity and root path Lambda uses on the file system.
        access_point = s3files.CfnAccessPoint(self, "AccessPoint",
            file_system_id=file_system.attr_file_system_id,
            root_directory=s3files.CfnAccessPoint.RootDirectoryProperty(
                path="/export/lambda",
                creation_permissions=s3files.CfnAccessPoint.CreationPermissionsProperty(owner_gid="1001", owner_uid="1001", permissions="750")
            ),
            posix_user=s3files.CfnAccessPoint.PosixUserProperty(gid="1001", uid="1001")
        )
        
        fn = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
            vpc=vpc,
            filesystem=lambda_.FileSystem.from_s3_files_access_point(access_point, "/mnt/s3files")
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        file_system_id: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAccessPoint.PosixUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        root_directory: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAccessPoint.RootDirectoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnAccessPoint.AccessPointTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::S3Files::AccessPoint``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param file_system_id: The ID of the S3 Files file system that the access point provides access to.
        :param client_token: (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
        :param posix_user: 
        :param root_directory: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b9f468e522685c39b2f812c91ee48b3106d688efb009da76beffc8ff30b6bc7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPointProps(
            file_system_id=file_system_id,
            client_token=client_token,
            posix_user=posix_user,
            root_directory=root_directory,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAccessPoint")
    @builtins.classmethod
    def arn_for_access_point(
        cls,
        resource: "_IAccessPointRef_95e8d0d6",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc0472630e20f79487c18ab780df06dcc8905e0c8560e2e53a6188c33fc00c5d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAccessPoint", [resource]))

    @jsii.member(jsii_name="isCfnAccessPoint")
    @builtins.classmethod
    def is_cfn_access_point(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAccessPoint.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f892c2d70dd8ae3445d334a24f4404e14706aeca0da2ad71a10709af8776d246)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAccessPoint", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2ab40b244f3ea35d4e5602a51c168ec5fcb478102f4ed2aaf18a6634eb8009)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b34fca81279a380c3bb45f84f16294c9a5d45163b215314ebc25cf29b6d7960)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "_AccessPointReference_43fd163f":
        '''A reference to a AccessPoint resource.'''
        return typing.cast("_AccessPointReference_43fd163f", jsii.get(self, "accessPointRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessPointArn")
    def attr_access_point_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AccessPointArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPointArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessPointId")
    def attr_access_point_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AccessPointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPointId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        '''The ID of the S3 Files file system that the access point provides access to.'''
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6638a43ccd740d1598c498ff27fd0c02d17cfd2dacc462fccc9ea6d69bc49004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''(optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d521ec55804d545621795ce6d385d328f0fa5c55c617ea9aa2f0571ef26ee18d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="posixUser")
    def posix_user(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.PosixUserProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.PosixUserProperty"]], jsii.get(self, "posixUser"))

    @posix_user.setter
    def posix_user(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.PosixUserProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dd64d0b6f9a28352ce6ca67a0dac212a24612b474921f0519dd0182a95e2f72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posixUser", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rootDirectory")
    def root_directory(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.RootDirectoryProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.RootDirectoryProperty"]], jsii.get(self, "rootDirectory"))

    @root_directory.setter
    def root_directory(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.RootDirectoryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7747f5b254b1fc1ca521be95df05679c67957e6cdf8b59d8e6c5d77e25eadee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootDirectory", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]]:
        return typing.cast(typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e3c13fefac42a7104fc340213f460e52a0a03398accefa79093d4eed81a267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnAccessPoint.AccessPointTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AccessPointTagProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-accesspointtag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                access_point_tag_property = s3files.CfnAccessPoint.AccessPointTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bb0e91916a0b43e58884828f3dbf1463e90ee93e65b78ef8597a0a808cdd8cc)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-accesspointtag.html#cfn-s3files-accesspoint-accesspointtag-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-accesspointtag.html#cfn-s3files-accesspoint-accesspointtag-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessPointTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnAccessPoint.CreationPermissionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "owner_gid": "ownerGid",
            "owner_uid": "ownerUid",
            "permissions": "permissions",
        },
    )
    class CreationPermissionsProperty:
        def __init__(
            self,
            *,
            owner_gid: builtins.str,
            owner_uid: builtins.str,
            permissions: builtins.str,
        ) -> None:
            '''
            :param owner_gid: Specifies the POSIX group ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
            :param owner_uid: Specifies the POSIX user ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
            :param permissions: Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-creationpermissions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                creation_permissions_property = s3files.CfnAccessPoint.CreationPermissionsProperty(
                    owner_gid="ownerGid",
                    owner_uid="ownerUid",
                    permissions="permissions"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64dee1499b8ed7247677773dd8e075f590088b3354fd7a3f0725741456561b4f)
                check_type(argname="argument owner_gid", value=owner_gid, expected_type=type_hints["owner_gid"])
                check_type(argname="argument owner_uid", value=owner_uid, expected_type=type_hints["owner_uid"])
                check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "owner_gid": owner_gid,
                "owner_uid": owner_uid,
                "permissions": permissions,
            }

        @builtins.property
        def owner_gid(self) -> builtins.str:
            '''Specifies the POSIX group ID to apply to the RootDirectory.

            Accepts values from 0 to 2^32 (4294967295).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-creationpermissions.html#cfn-s3files-accesspoint-creationpermissions-ownergid
            '''
            result = self._values.get("owner_gid")
            assert result is not None, "Required property 'owner_gid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_uid(self) -> builtins.str:
            '''Specifies the POSIX user ID to apply to the RootDirectory.

            Accepts values from 0 to 2^32 (4294967295).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-creationpermissions.html#cfn-s3files-accesspoint-creationpermissions-owneruid
            '''
            result = self._values.get("owner_uid")
            assert result is not None, "Required property 'owner_uid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def permissions(self) -> builtins.str:
            '''Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-creationpermissions.html#cfn-s3files-accesspoint-creationpermissions-permissions
            '''
            result = self._values.get("permissions")
            assert result is not None, "Required property 'permissions' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreationPermissionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnAccessPoint.PosixUserProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "uid": "uid", "secondary_gids": "secondaryGids"},
    )
    class PosixUserProperty:
        def __init__(
            self,
            *,
            gid: builtins.str,
            uid: builtins.str,
            secondary_gids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param gid: The POSIX group ID used for all file system operations using this access point.
            :param uid: The POSIX user ID used for all file system operations using this access point.
            :param secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-posixuser.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                posix_user_property = s3files.CfnAccessPoint.PosixUserProperty(
                    gid="gid",
                    uid="uid",
                
                    # the properties below are optional
                    secondary_gids=["secondaryGids"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__72e8bb1979aab86f50f291bb117c741f1cbe3845c4b0b7627006d22e32f345be)
                check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
                check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
                check_type(argname="argument secondary_gids", value=secondary_gids, expected_type=type_hints["secondary_gids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gid": gid,
                "uid": uid,
            }
            if secondary_gids is not None:
                self._values["secondary_gids"] = secondary_gids

        @builtins.property
        def gid(self) -> builtins.str:
            '''The POSIX group ID used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-posixuser.html#cfn-s3files-accesspoint-posixuser-gid
            '''
            result = self._values.get("gid")
            assert result is not None, "Required property 'gid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def uid(self) -> builtins.str:
            '''The POSIX user ID used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-posixuser.html#cfn-s3files-accesspoint-posixuser-uid
            '''
            result = self._values.get("uid")
            assert result is not None, "Required property 'uid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secondary_gids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Secondary POSIX group IDs used for all file system operations using this access point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-posixuser.html#cfn-s3files-accesspoint-posixuser-secondarygids
            '''
            result = self._values.get("secondary_gids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PosixUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnAccessPoint.RootDirectoryProperty",
        jsii_struct_bases=[],
        name_mapping={"creation_permissions": "creationPermissions", "path": "path"},
    )
    class RootDirectoryProperty:
        def __init__(
            self,
            *,
            creation_permissions: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAccessPoint.CreationPermissionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param creation_permissions: 
            :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationPermissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-rootdirectory.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                root_directory_property = s3files.CfnAccessPoint.RootDirectoryProperty(
                    creation_permissions=s3files.CfnAccessPoint.CreationPermissionsProperty(
                        owner_gid="ownerGid",
                        owner_uid="ownerUid",
                        permissions="permissions"
                    ),
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f27edad22a8d6693b1475985adea760c15603adefa150c1149356ff1a3e6c02c)
                check_type(argname="argument creation_permissions", value=creation_permissions, expected_type=type_hints["creation_permissions"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if creation_permissions is not None:
                self._values["creation_permissions"] = creation_permissions
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def creation_permissions(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.CreationPermissionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-rootdirectory.html#cfn-s3files-accesspoint-rootdirectory-creationpermissions
            '''
            result = self._values.get("creation_permissions")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.CreationPermissionsProperty"]], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system.

            A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the CreationPermissions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-accesspoint-rootdirectory.html#cfn-s3files-accesspoint-rootdirectory-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RootDirectoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3files.CfnAccessPointProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "client_token": "clientToken",
        "posix_user": "posixUser",
        "root_directory": "rootDirectory",
        "tags": "tags",
    },
)
class CfnAccessPointProps:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAccessPoint.PosixUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        root_directory: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAccessPoint.RootDirectoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnAccessPoint.AccessPointTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccessPoint``.

        :param file_system_id: The ID of the S3 Files file system that the access point provides access to.
        :param client_token: (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
        :param posix_user: 
        :param root_directory: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html
        :exampleMetadata: infused

        Example::

            import aws_cdk as cdk
            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_s3files as s3files
            
            
            vpc = ec2.Vpc(self, "Vpc")
            
            # Versioning is required — S3 Files relies on object versions for consistency.
            bucket = s3.Bucket(self, "Bucket", versioned=True)
            
            # S3 Files assumes this role to sync data between S3 and the file system.
            role = iam.Role(self, "S3FilesRole",
                assumed_by=iam.ServicePrincipal("elasticfilesystem.amazonaws.com")
            )
            
            # S3 permissions: read/write access to the bucket and objects
            role.add_to_policy(iam.PolicyStatement(
                actions=["s3:ListBucket*"],
                resources=[bucket.bucket_arn]
            ))
            role.add_to_policy(iam.PolicyStatement(
                actions=["s3:AbortMultipartUpload", "s3:DeleteObject", "s3:GetObject*", "s3:List*", "s3:PutObject*"],
                resources=[bucket.arn_for_objects("*")]
            ))
            
            # EventBridge permissions: S3 Files creates rules prefixed "DO-NOT-DELETE-S3-Files"
            # to detect S3 object changes and trigger data synchronization.
            role.add_to_policy(iam.PolicyStatement(
                actions=["events:DeleteRule", "events:DisableRule", "events:EnableRule", "events:PutRule", "events:PutTargets", "events:RemoveTargets"
                ],
                resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/DO-NOT-DELETE-S3-Files*"],
                conditions={"StringEquals": {"events:ManagedBy": "elasticfilesystem.amazonaws.com"}}
            ))
            role.add_to_policy(iam.PolicyStatement(
                actions=["events:DescribeRule", "events:ListRuleNamesByTarget", "events:ListRules", "events:ListTargetsByRule"],
                resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/*"]
            ))
            
            file_system = s3files.CfnFileSystem(self, "S3FilesFs",
                bucket=bucket.bucket_arn,
                role_arn=role.role_arn
            )
            
            sg = ec2.SecurityGroup(self, "MountTargetSG", vpc=vpc)
            
            # Create a mount target in each private subnet so Lambda can reach the file system via NFS.
            vpc.private_subnets.for_each((subnet, i) =>
                  new s3files.CfnMountTarget(this, `MountTarget${i}`, {
                    fileSystemId: fileSystem.attrFileSystemId,
                    subnetId: subnet.subnetId,
                    securityGroups: [sg.securityGroupId],
                  }))
            
            # The access point defines the POSIX identity and root path Lambda uses on the file system.
            access_point = s3files.CfnAccessPoint(self, "AccessPoint",
                file_system_id=file_system.attr_file_system_id,
                root_directory=s3files.CfnAccessPoint.RootDirectoryProperty(
                    path="/export/lambda",
                    creation_permissions=s3files.CfnAccessPoint.CreationPermissionsProperty(owner_gid="1001", owner_uid="1001", permissions="750")
                ),
                posix_user=s3files.CfnAccessPoint.PosixUserProperty(gid="1001", uid="1001")
            )
            
            fn = lambda_.Function(self, "MyFunction",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
                vpc=vpc,
                filesystem=lambda_.FileSystem.from_s3_files_access_point(access_point, "/mnt/s3files")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a4c6eb05f458fd13b1994bef00d25ed8d97a6dfd3c1923e17fc4c9b45339d6)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument posix_user", value=posix_user, expected_type=type_hints["posix_user"])
            check_type(argname="argument root_directory", value=root_directory, expected_type=type_hints["root_directory"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if posix_user is not None:
            self._values["posix_user"] = posix_user
        if root_directory is not None:
            self._values["root_directory"] = root_directory
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The ID of the S3 Files file system that the access point provides access to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html#cfn-s3files-accesspoint-filesystemid
        '''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''(optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html#cfn-s3files-accesspoint-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_user(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.PosixUserProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html#cfn-s3files-accesspoint-posixuser
        '''
        result = self._values.get("posix_user")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.PosixUserProperty"]], result)

    @builtins.property
    def root_directory(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.RootDirectoryProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html#cfn-s3files-accesspoint-rootdirectory
        '''
        result = self._values.get("root_directory")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAccessPoint.RootDirectoryProperty"]], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-accesspoint.html#cfn-s3files-accesspoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnAccessPoint.AccessPointTagProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFileSystemRef_f26f446c, _ITaggableV2_4e6798f8)
class CfnFileSystem(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystem",
):
    '''Resource Type definition for AWS::S3Files::FileSystem.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html
    :cloudformationResource: AWS::S3Files::FileSystem
    :exampleMetadata: infused

    Example::

        import aws_cdk as cdk
        import aws_cdk.aws_ec2 as ec2
        import aws_cdk.aws_s3 as s3
        import aws_cdk.aws_s3files as s3files
        
        
        vpc = ec2.Vpc(self, "Vpc")
        
        # Versioning is required — S3 Files relies on object versions for consistency.
        bucket = s3.Bucket(self, "Bucket", versioned=True)
        
        # S3 Files assumes this role to sync data between S3 and the file system.
        role = iam.Role(self, "S3FilesRole",
            assumed_by=iam.ServicePrincipal("elasticfilesystem.amazonaws.com")
        )
        
        # S3 permissions: read/write access to the bucket and objects
        role.add_to_policy(iam.PolicyStatement(
            actions=["s3:ListBucket*"],
            resources=[bucket.bucket_arn]
        ))
        role.add_to_policy(iam.PolicyStatement(
            actions=["s3:AbortMultipartUpload", "s3:DeleteObject", "s3:GetObject*", "s3:List*", "s3:PutObject*"],
            resources=[bucket.arn_for_objects("*")]
        ))
        
        # EventBridge permissions: S3 Files creates rules prefixed "DO-NOT-DELETE-S3-Files"
        # to detect S3 object changes and trigger data synchronization.
        role.add_to_policy(iam.PolicyStatement(
            actions=["events:DeleteRule", "events:DisableRule", "events:EnableRule", "events:PutRule", "events:PutTargets", "events:RemoveTargets"
            ],
            resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/DO-NOT-DELETE-S3-Files*"],
            conditions={"StringEquals": {"events:ManagedBy": "elasticfilesystem.amazonaws.com"}}
        ))
        role.add_to_policy(iam.PolicyStatement(
            actions=["events:DescribeRule", "events:ListRuleNamesByTarget", "events:ListRules", "events:ListTargetsByRule"],
            resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/*"]
        ))
        
        file_system = s3files.CfnFileSystem(self, "S3FilesFs",
            bucket=bucket.bucket_arn,
            role_arn=role.role_arn
        )
        
        sg = ec2.SecurityGroup(self, "MountTargetSG", vpc=vpc)
        
        # Create a mount target in each private subnet so Lambda can reach the file system via NFS.
        vpc.private_subnets.for_each((subnet, i) =>
              new s3files.CfnMountTarget(this, `MountTarget${i}`, {
                fileSystemId: fileSystem.attrFileSystemId,
                subnetId: subnet.subnetId,
                securityGroups: [sg.securityGroupId],
              }))
        
        # The access point defines the POSIX identity and root path Lambda uses on the file system.
        access_point = s3files.CfnAccessPoint(self, "AccessPoint",
            file_system_id=file_system.attr_file_system_id,
            root_directory=s3files.CfnAccessPoint.RootDirectoryProperty(
                path="/export/lambda",
                creation_permissions=s3files.CfnAccessPoint.CreationPermissionsProperty(owner_gid="1001", owner_uid="1001", permissions="750")
            ),
            posix_user=s3files.CfnAccessPoint.PosixUserProperty(gid="1001", uid="1001")
        )
        
        fn = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
            vpc=vpc,
            filesystem=lambda_.FileSystem.from_s3_files_access_point(access_point, "/mnt/s3files")
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        bucket: builtins.str,
        role_arn: builtins.str,
        accept_bucket_warning: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        client_token: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        synchronization_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFileSystem.SynchronizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::S3Files::FileSystem``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bucket: 
        :param role_arn: 
        :param accept_bucket_warning: 
        :param client_token: 
        :param kms_key_id: 
        :param prefix: 
        :param synchronization_configuration: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab24a73fd9d4673c787d6f2acab8028c126e7f2dd156ff9fa3ea50eb9a881af3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFileSystemProps(
            bucket=bucket,
            role_arn=role_arn,
            accept_bucket_warning=accept_bucket_warning,
            client_token=client_token,
            kms_key_id=kms_key_id,
            prefix=prefix,
            synchronization_configuration=synchronization_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFileSystem")
    @builtins.classmethod
    def arn_for_file_system(cls, resource: "_IFileSystemRef_f26f446c") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb952617b8412ec816ab17bfc8531f9f6462339d6034fb1d8e38d372b2656c6c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFileSystem", [resource]))

    @jsii.member(jsii_name="isCfnFileSystem")
    @builtins.classmethod
    def is_cfn_file_system(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFileSystem.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032928fdc17fdf0eab550c75497960599fffd43416bdabe4596ea58568f62a22)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFileSystem", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5109febb1ad1b583871e454c6dc8c432b7fd86e8b1834ae51245492217a82e02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__445b42eaab09c902bd878bd86935c02ed804956b9a61e74ac0aa5cfc98667b1e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrFileSystemArn")
    def attr_file_system_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: FileSystemArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFileSystemArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFileSystemId")
    def attr_file_system_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: FileSystemId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFileSystemId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

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
    @jsii.member(jsii_name="attrSynchronizationConfigurationLatestVersionNumber")
    def attr_synchronization_configuration_latest_version_number(self) -> jsii.Number:
        '''
        :cloudformationAttribute: SynchronizationConfiguration.LatestVersionNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSynchronizationConfigurationLatestVersionNumber"))

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
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "_FileSystemReference_63976c73":
        '''A reference to a FileSystem resource.'''
        return typing.cast("_FileSystemReference_63976c73", jsii.get(self, "fileSystemRef"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f807bf240a3dc28518036657781fe74bb69bf042a4a017da015393388c2328be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b63a6b8d1f0f4596963203ec76e1e7234d62c7c844067d85ef658080f6674b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="acceptBucketWarning")
    def accept_bucket_warning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "acceptBucketWarning"))

    @accept_bucket_warning.setter
    def accept_bucket_warning(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfcdf1b911d66287232e5949e8529bbee619d3b5899517129f2d423c2c468b17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptBucketWarning", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4325c2c9995d5bbe01429f3f7a13d4b4e8552120ea30f3c94f64b68368a9c31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67467712ab0b724bf3d3f9acec4d575d3a4ceb10851fe8f6203787266419f84e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bbd50c736c0c28e27bcdd66f7d1904e9804cae199011de0c657a46a46a8bafc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="synchronizationConfiguration")
    def synchronization_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.SynchronizationConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.SynchronizationConfigurationProperty"]], jsii.get(self, "synchronizationConfiguration"))

    @synchronization_configuration.setter
    def synchronization_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.SynchronizationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc34f7e36e687a91d6dc3e62b4bcf2b7537bf4a02df57bbccae58cb9964b7b80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synchronizationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327e518bd5a4d3a4bf4d7bc675cab0d028b3d45bbf08f16311a0e427007acef3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystem.ExpirationDataRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"days_after_last_access": "daysAfterLastAccess"},
    )
    class ExpirationDataRuleProperty:
        def __init__(self, *, days_after_last_access: jsii.Number) -> None:
            '''
            :param days_after_last_access: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-expirationdatarule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                expiration_data_rule_property = s3files.CfnFileSystem.ExpirationDataRuleProperty(
                    days_after_last_access=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76a1907458dd6df077e1efef5dc427fd4c5473c269fb090da597f82050b0a2c6)
                check_type(argname="argument days_after_last_access", value=days_after_last_access, expected_type=type_hints["days_after_last_access"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "days_after_last_access": days_after_last_access,
            }

        @builtins.property
        def days_after_last_access(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-expirationdatarule.html#cfn-s3files-filesystem-expirationdatarule-daysafterlastaccess
            '''
            result = self._values.get("days_after_last_access")
            assert result is not None, "Required property 'days_after_last_access' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpirationDataRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystem.ImportDataRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "prefix": "prefix",
            "size_less_than": "sizeLessThan",
            "trigger": "trigger",
        },
    )
    class ImportDataRuleProperty:
        def __init__(
            self,
            *,
            prefix: builtins.str,
            size_less_than: jsii.Number,
            trigger: builtins.str,
        ) -> None:
            '''
            :param prefix: 
            :param size_less_than: 
            :param trigger: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-importdatarule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                import_data_rule_property = s3files.CfnFileSystem.ImportDataRuleProperty(
                    prefix="prefix",
                    size_less_than=123,
                    trigger="trigger"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e26f3cfd5846b7f063bb4b9ee19f903620be2d839d98177879332ef5247c0799)
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument size_less_than", value=size_less_than, expected_type=type_hints["size_less_than"])
                check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "prefix": prefix,
                "size_less_than": size_less_than,
                "trigger": trigger,
            }

        @builtins.property
        def prefix(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-importdatarule.html#cfn-s3files-filesystem-importdatarule-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def size_less_than(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-importdatarule.html#cfn-s3files-filesystem-importdatarule-sizelessthan
            '''
            result = self._values.get("size_less_than")
            assert result is not None, "Required property 'size_less_than' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def trigger(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-importdatarule.html#cfn-s3files-filesystem-importdatarule-trigger
            '''
            result = self._values.get("trigger")
            assert result is not None, "Required property 'trigger' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImportDataRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystem.SynchronizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expiration_data_rules": "expirationDataRules",
            "import_data_rules": "importDataRules",
            "latest_version_number": "latestVersionNumber",
        },
    )
    class SynchronizationConfigurationProperty:
        def __init__(
            self,
            *,
            expiration_data_rules: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFileSystem.ExpirationDataRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
            import_data_rules: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFileSystem.ImportDataRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
            latest_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param expiration_data_rules: 
            :param import_data_rules: 
            :param latest_version_number: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-synchronizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3files as s3files
                
                synchronization_configuration_property = s3files.CfnFileSystem.SynchronizationConfigurationProperty(
                    expiration_data_rules=[s3files.CfnFileSystem.ExpirationDataRuleProperty(
                        days_after_last_access=123
                    )],
                    import_data_rules=[s3files.CfnFileSystem.ImportDataRuleProperty(
                        prefix="prefix",
                        size_less_than=123,
                        trigger="trigger"
                    )],
                
                    # the properties below are optional
                    latest_version_number=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b04bd708d813e597066ac833db30afce7aeec22039315ee5ef6206a997bc06e)
                check_type(argname="argument expiration_data_rules", value=expiration_data_rules, expected_type=type_hints["expiration_data_rules"])
                check_type(argname="argument import_data_rules", value=import_data_rules, expected_type=type_hints["import_data_rules"])
                check_type(argname="argument latest_version_number", value=latest_version_number, expected_type=type_hints["latest_version_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expiration_data_rules": expiration_data_rules,
                "import_data_rules": import_data_rules,
            }
            if latest_version_number is not None:
                self._values["latest_version_number"] = latest_version_number

        @builtins.property
        def expiration_data_rules(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.ExpirationDataRuleProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-synchronizationconfiguration.html#cfn-s3files-filesystem-synchronizationconfiguration-expirationdatarules
            '''
            result = self._values.get("expiration_data_rules")
            assert result is not None, "Required property 'expiration_data_rules' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.ExpirationDataRuleProperty"]]], result)

        @builtins.property
        def import_data_rules(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.ImportDataRuleProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-synchronizationconfiguration.html#cfn-s3files-filesystem-synchronizationconfiguration-importdatarules
            '''
            result = self._values.get("import_data_rules")
            assert result is not None, "Required property 'import_data_rules' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.ImportDataRuleProperty"]]], result)

        @builtins.property
        def latest_version_number(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3files-filesystem-synchronizationconfiguration.html#cfn-s3files-filesystem-synchronizationconfiguration-latestversionnumber
            '''
            result = self._values.get("latest_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SynchronizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IFileSystemPolicyRef_f41c1127)
class CfnFileSystemPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystemPolicy",
):
    '''Resource Type definition for AWS::S3Files::FileSystemPolicy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystempolicy.html
    :cloudformationResource: AWS::S3Files::FileSystemPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3files as s3files
        
        # policy: Any
        
        cfn_file_system_policy = s3files.CfnFileSystemPolicy(self, "MyCfnFileSystemPolicy",
            file_system_id="fileSystemId",
            policy=policy
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        file_system_id: builtins.str,
        policy: typing.Any,
    ) -> None:
        '''Create a new ``AWS::S3Files::FileSystemPolicy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param file_system_id: 
        :param policy: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc75d99c547846e5461a176cfda12c742511e5ed44bb84bfd742f95e7a5e88e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFileSystemPolicyProps(file_system_id=file_system_id, policy=policy)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnFileSystemPolicy")
    @builtins.classmethod
    def is_cfn_file_system_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFileSystemPolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d938eade305417a399f213b5d6dbb9aeb2223afcc066e8f41cc779daa5d31ef)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFileSystemPolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66cd4d5110edf513c8fad060766bfd1c87df17b0bd50230614c49b7d5346366)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3993ffa72a4c02d1dc625cc5681f1bfce294d9bb76b08b9b73e6ea32c4e2fc62)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemPolicyRef")
    def file_system_policy_ref(self) -> "_FileSystemPolicyReference_10ae5ae0":
        '''A reference to a FileSystemPolicy resource.'''
        return typing.cast("_FileSystemPolicyReference_10ae5ae0", jsii.get(self, "fileSystemPolicyRef"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59cf1fff18f8f13e65d4cc3c44d5c6c055b0da2e1c861f17d7f153cc66dcd852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa21219069c11b5ff9dc9f759b6bb24a8bc8910de2c2beedf4cfc08bfbaec23e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystemPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"file_system_id": "fileSystemId", "policy": "policy"},
)
class CfnFileSystemPolicyProps:
    def __init__(self, *, file_system_id: builtins.str, policy: typing.Any) -> None:
        '''Properties for defining a ``CfnFileSystemPolicy``.

        :param file_system_id: 
        :param policy: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystempolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3files as s3files
            
            # policy: Any
            
            cfn_file_system_policy_props = s3files.CfnFileSystemPolicyProps(
                file_system_id="fileSystemId",
                policy=policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc610f1b324a97cf4f048f94b96e46ae467ec1a70bf0dbf1feab580b1585cba)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
            "policy": policy,
        }

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystempolicy.html#cfn-s3files-filesystempolicy-filesystemid
        '''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystempolicy.html#cfn-s3files-filesystempolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFileSystemPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3files.CfnFileSystemProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "role_arn": "roleArn",
        "accept_bucket_warning": "acceptBucketWarning",
        "client_token": "clientToken",
        "kms_key_id": "kmsKeyId",
        "prefix": "prefix",
        "synchronization_configuration": "synchronizationConfiguration",
        "tags": "tags",
    },
)
class CfnFileSystemProps:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        role_arn: builtins.str,
        accept_bucket_warning: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        client_token: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        synchronization_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFileSystem.SynchronizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFileSystem``.

        :param bucket: 
        :param role_arn: 
        :param accept_bucket_warning: 
        :param client_token: 
        :param kms_key_id: 
        :param prefix: 
        :param synchronization_configuration: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html
        :exampleMetadata: infused

        Example::

            import aws_cdk as cdk
            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_s3files as s3files
            
            
            vpc = ec2.Vpc(self, "Vpc")
            
            # Versioning is required — S3 Files relies on object versions for consistency.
            bucket = s3.Bucket(self, "Bucket", versioned=True)
            
            # S3 Files assumes this role to sync data between S3 and the file system.
            role = iam.Role(self, "S3FilesRole",
                assumed_by=iam.ServicePrincipal("elasticfilesystem.amazonaws.com")
            )
            
            # S3 permissions: read/write access to the bucket and objects
            role.add_to_policy(iam.PolicyStatement(
                actions=["s3:ListBucket*"],
                resources=[bucket.bucket_arn]
            ))
            role.add_to_policy(iam.PolicyStatement(
                actions=["s3:AbortMultipartUpload", "s3:DeleteObject", "s3:GetObject*", "s3:List*", "s3:PutObject*"],
                resources=[bucket.arn_for_objects("*")]
            ))
            
            # EventBridge permissions: S3 Files creates rules prefixed "DO-NOT-DELETE-S3-Files"
            # to detect S3 object changes and trigger data synchronization.
            role.add_to_policy(iam.PolicyStatement(
                actions=["events:DeleteRule", "events:DisableRule", "events:EnableRule", "events:PutRule", "events:PutTargets", "events:RemoveTargets"
                ],
                resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/DO-NOT-DELETE-S3-Files*"],
                conditions={"StringEquals": {"events:ManagedBy": "elasticfilesystem.amazonaws.com"}}
            ))
            role.add_to_policy(iam.PolicyStatement(
                actions=["events:DescribeRule", "events:ListRuleNamesByTarget", "events:ListRules", "events:ListTargetsByRule"],
                resources=[f"arn:{cdk.Aws.PARTITION}:events:*:*:rule/*"]
            ))
            
            file_system = s3files.CfnFileSystem(self, "S3FilesFs",
                bucket=bucket.bucket_arn,
                role_arn=role.role_arn
            )
            
            sg = ec2.SecurityGroup(self, "MountTargetSG", vpc=vpc)
            
            # Create a mount target in each private subnet so Lambda can reach the file system via NFS.
            vpc.private_subnets.for_each((subnet, i) =>
                  new s3files.CfnMountTarget(this, `MountTarget${i}`, {
                    fileSystemId: fileSystem.attrFileSystemId,
                    subnetId: subnet.subnetId,
                    securityGroups: [sg.securityGroupId],
                  }))
            
            # The access point defines the POSIX identity and root path Lambda uses on the file system.
            access_point = s3files.CfnAccessPoint(self, "AccessPoint",
                file_system_id=file_system.attr_file_system_id,
                root_directory=s3files.CfnAccessPoint.RootDirectoryProperty(
                    path="/export/lambda",
                    creation_permissions=s3files.CfnAccessPoint.CreationPermissionsProperty(owner_gid="1001", owner_uid="1001", permissions="750")
                ),
                posix_user=s3files.CfnAccessPoint.PosixUserProperty(gid="1001", uid="1001")
            )
            
            fn = lambda_.Function(self, "MyFunction",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler")),
                vpc=vpc,
                filesystem=lambda_.FileSystem.from_s3_files_access_point(access_point, "/mnt/s3files")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb096df111262d1729df3bc79ad5d3d9e9e6df365c87bf12f00ce6210b7a315)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument accept_bucket_warning", value=accept_bucket_warning, expected_type=type_hints["accept_bucket_warning"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument synchronization_configuration", value=synchronization_configuration, expected_type=type_hints["synchronization_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "role_arn": role_arn,
        }
        if accept_bucket_warning is not None:
            self._values["accept_bucket_warning"] = accept_bucket_warning
        if client_token is not None:
            self._values["client_token"] = client_token
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if prefix is not None:
            self._values["prefix"] = prefix
        if synchronization_configuration is not None:
            self._values["synchronization_configuration"] = synchronization_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bucket(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-bucket
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accept_bucket_warning(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-acceptbucketwarning
        '''
        result = self._values.get("accept_bucket_warning")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synchronization_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.SynchronizationConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-synchronizationconfiguration
        '''
        result = self._values.get("synchronization_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFileSystem.SynchronizationConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-filesystem.html#cfn-s3files-filesystem-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFileSystemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IMountTargetRef_57587992)
class CfnMountTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3files.CfnMountTarget",
):
    '''Resource Type definition for AWS::S3Files::MountTarget.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html
    :cloudformationResource: AWS::S3Files::MountTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3files as s3files
        
        cfn_mount_target = s3files.CfnMountTarget(self, "MyCfnMountTarget",
            file_system_id="fileSystemId",
            subnet_id="subnetId",
        
            # the properties below are optional
            ip_address_type="ipAddressType",
            ipv4_address="ipv4Address",
            ipv6_address="ipv6Address",
            security_groups=["securityGroups"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        file_system_id: builtins.str,
        subnet_id: builtins.str,
        ip_address_type: typing.Optional[builtins.str] = None,
        ipv4_address: typing.Optional[builtins.str] = None,
        ipv6_address: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::S3Files::MountTarget``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param file_system_id: 
        :param subnet_id: 
        :param ip_address_type: 
        :param ipv4_address: 
        :param ipv6_address: 
        :param security_groups: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9afd4a3eae9a5dc0625007b4a2df718403b378ff5e07aa8ffcfa93c9a53d046)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMountTargetProps(
            file_system_id=file_system_id,
            subnet_id=subnet_id,
            ip_address_type=ip_address_type,
            ipv4_address=ipv4_address,
            ipv6_address=ipv6_address,
            security_groups=security_groups,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnMountTarget")
    @builtins.classmethod
    def is_cfn_mount_target(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnMountTarget.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e72b8f6fad03e4c7b1e6b4c09d4b901e71f7b9648fe3f964118e022adccfcf)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnMountTarget", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e23055abd97201d86bb152595231b0b3346ea003d9d5ee585f10e99c7cfbd4b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6499d4353ea6da4f35dc2332ac9a26e5bc510dbc21a2ecda30e0f06078583ff1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAvailabilityZoneId")
    def attr_availability_zone_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AvailabilityZoneId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAvailabilityZoneId"))

    @builtins.property
    @jsii.member(jsii_name="attrMountTargetId")
    def attr_mount_target_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: MountTargetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMountTargetId"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkInterfaceId")
    def attr_network_interface_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: NetworkInterfaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkInterfaceId"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

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
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: VpcId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="mountTargetRef")
    def mount_target_ref(self) -> "_MountTargetReference_c9c3f8f9":
        '''A reference to a MountTarget resource.'''
        return typing.cast("_MountTargetReference_c9c3f8f9", jsii.get(self, "mountTargetRef"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__326fe98b9aa7b9e0761b3a99021f1dd6b471a6f4d4a9ca0c102e6b195c7ecf58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daab55069ed7af383fae7873019670acde077fe675881a28c9798db68a3ecaae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipAddressType")
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressType"))

    @ip_address_type.setter
    def ip_address_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d28efaecdcc1cd8cd7082a54495fbaf06d90b9998af31551e36609acb8dcc690)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddressType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36202d13fe4264f10d25903dc89da82589244e2cc3341f09f8fc9f1d6c83c8a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6Address")
    def ipv6_address(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6Address"))

    @ipv6_address.setter
    def ipv6_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4adf1a03f0a0b33443e5404167b9ecb7ad83848432d6587ee5863a01d59a3403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Address", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__956b509688210b28bbff0d032e9b0f348325adaeb3713163604385cafefe9f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3files.CfnMountTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "subnet_id": "subnetId",
        "ip_address_type": "ipAddressType",
        "ipv4_address": "ipv4Address",
        "ipv6_address": "ipv6Address",
        "security_groups": "securityGroups",
    },
)
class CfnMountTargetProps:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        subnet_id: builtins.str,
        ip_address_type: typing.Optional[builtins.str] = None,
        ipv4_address: typing.Optional[builtins.str] = None,
        ipv6_address: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMountTarget``.

        :param file_system_id: 
        :param subnet_id: 
        :param ip_address_type: 
        :param ipv4_address: 
        :param ipv6_address: 
        :param security_groups: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3files as s3files
            
            cfn_mount_target_props = s3files.CfnMountTargetProps(
                file_system_id="fileSystemId",
                subnet_id="subnetId",
            
                # the properties below are optional
                ip_address_type="ipAddressType",
                ipv4_address="ipv4Address",
                ipv6_address="ipv6Address",
                security_groups=["securityGroups"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38212c95a0bd3b9103e91e76c4d4b35afbd0a1902d13ea3a4d956445137335a)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument ip_address_type", value=ip_address_type, expected_type=type_hints["ip_address_type"])
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument ipv6_address", value=ipv6_address, expected_type=type_hints["ipv6_address"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
            "subnet_id": subnet_id,
        }
        if ip_address_type is not None:
            self._values["ip_address_type"] = ip_address_type
        if ipv4_address is not None:
            self._values["ipv4_address"] = ipv4_address
        if ipv6_address is not None:
            self._values["ipv6_address"] = ipv6_address
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html#cfn-s3files-mounttarget-filesystemid
        '''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html#cfn-s3files-mounttarget-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_address_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html#cfn-s3files-mounttarget-ipaddresstype
        '''
        result = self._values.get("ip_address_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv4_address(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html#cfn-s3files-mounttarget-ipv4address
        '''
        result = self._values.get("ipv4_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_address(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html#cfn-s3files-mounttarget-ipv6address
        '''
        result = self._values.get("ipv6_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3files-mounttarget.html#cfn-s3files-mounttarget-securitygroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMountTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPoint",
    "CfnAccessPointProps",
    "CfnFileSystem",
    "CfnFileSystemPolicy",
    "CfnFileSystemPolicyProps",
    "CfnFileSystemProps",
    "CfnMountTarget",
    "CfnMountTargetProps",
]

publication.publish()

def _typecheckingstub__0b9f468e522685c39b2f812c91ee48b3106d688efb009da76beffc8ff30b6bc7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    file_system_id: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.PosixUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_directory: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.RootDirectoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnAccessPoint.AccessPointTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc0472630e20f79487c18ab780df06dcc8905e0c8560e2e53a6188c33fc00c5d(
    resource: _IAccessPointRef_95e8d0d6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f892c2d70dd8ae3445d334a24f4404e14706aeca0da2ad71a10709af8776d246(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2ab40b244f3ea35d4e5602a51c168ec5fcb478102f4ed2aaf18a6634eb8009(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b34fca81279a380c3bb45f84f16294c9a5d45163b215314ebc25cf29b6d7960(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6638a43ccd740d1598c498ff27fd0c02d17cfd2dacc462fccc9ea6d69bc49004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d521ec55804d545621795ce6d385d328f0fa5c55c617ea9aa2f0571ef26ee18d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd64d0b6f9a28352ce6ca67a0dac212a24612b474921f0519dd0182a95e2f72(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.PosixUserProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7747f5b254b1fc1ca521be95df05679c67957e6cdf8b59d8e6c5d77e25eadee0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAccessPoint.RootDirectoryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e3c13fefac42a7104fc340213f460e52a0a03398accefa79093d4eed81a267(
    value: typing.Optional[typing.List[CfnAccessPoint.AccessPointTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb0e91916a0b43e58884828f3dbf1463e90ee93e65b78ef8597a0a808cdd8cc(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64dee1499b8ed7247677773dd8e075f590088b3354fd7a3f0725741456561b4f(
    *,
    owner_gid: builtins.str,
    owner_uid: builtins.str,
    permissions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e8bb1979aab86f50f291bb117c741f1cbe3845c4b0b7627006d22e32f345be(
    *,
    gid: builtins.str,
    uid: builtins.str,
    secondary_gids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f27edad22a8d6693b1475985adea760c15603adefa150c1149356ff1a3e6c02c(
    *,
    creation_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.CreationPermissionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a4c6eb05f458fd13b1994bef00d25ed8d97a6dfd3c1923e17fc4c9b45339d6(
    *,
    file_system_id: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.PosixUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    root_directory: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPoint.RootDirectoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnAccessPoint.AccessPointTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab24a73fd9d4673c787d6f2acab8028c126e7f2dd156ff9fa3ea50eb9a881af3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket: builtins.str,
    role_arn: builtins.str,
    accept_bucket_warning: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    client_token: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    synchronization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.SynchronizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb952617b8412ec816ab17bfc8531f9f6462339d6034fb1d8e38d372b2656c6c(
    resource: _IFileSystemRef_f26f446c,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032928fdc17fdf0eab550c75497960599fffd43416bdabe4596ea58568f62a22(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5109febb1ad1b583871e454c6dc8c432b7fd86e8b1834ae51245492217a82e02(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445b42eaab09c902bd878bd86935c02ed804956b9a61e74ac0aa5cfc98667b1e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f807bf240a3dc28518036657781fe74bb69bf042a4a017da015393388c2328be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b63a6b8d1f0f4596963203ec76e1e7234d62c7c844067d85ef658080f6674b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfcdf1b911d66287232e5949e8529bbee619d3b5899517129f2d423c2c468b17(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4325c2c9995d5bbe01429f3f7a13d4b4e8552120ea30f3c94f64b68368a9c31d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67467712ab0b724bf3d3f9acec4d575d3a4ceb10851fe8f6203787266419f84e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bbd50c736c0c28e27bcdd66f7d1904e9804cae199011de0c657a46a46a8bafc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc34f7e36e687a91d6dc3e62b4bcf2b7537bf4a02df57bbccae58cb9964b7b80(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFileSystem.SynchronizationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327e518bd5a4d3a4bf4d7bc675cab0d028b3d45bbf08f16311a0e427007acef3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a1907458dd6df077e1efef5dc427fd4c5473c269fb090da597f82050b0a2c6(
    *,
    days_after_last_access: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e26f3cfd5846b7f063bb4b9ee19f903620be2d839d98177879332ef5247c0799(
    *,
    prefix: builtins.str,
    size_less_than: jsii.Number,
    trigger: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b04bd708d813e597066ac833db30afce7aeec22039315ee5ef6206a997bc06e(
    *,
    expiration_data_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.ExpirationDataRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    import_data_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.ImportDataRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    latest_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc75d99c547846e5461a176cfda12c742511e5ed44bb84bfd742f95e7a5e88e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    file_system_id: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d938eade305417a399f213b5d6dbb9aeb2223afcc066e8f41cc779daa5d31ef(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66cd4d5110edf513c8fad060766bfd1c87df17b0bd50230614c49b7d5346366(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3993ffa72a4c02d1dc625cc5681f1bfce294d9bb76b08b9b73e6ea32c4e2fc62(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59cf1fff18f8f13e65d4cc3c44d5c6c055b0da2e1c861f17d7f153cc66dcd852(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa21219069c11b5ff9dc9f759b6bb24a8bc8910de2c2beedf4cfc08bfbaec23e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc610f1b324a97cf4f048f94b96e46ae467ec1a70bf0dbf1feab580b1585cba(
    *,
    file_system_id: builtins.str,
    policy: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb096df111262d1729df3bc79ad5d3d9e9e6df365c87bf12f00ce6210b7a315(
    *,
    bucket: builtins.str,
    role_arn: builtins.str,
    accept_bucket_warning: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    client_token: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    synchronization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFileSystem.SynchronizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9afd4a3eae9a5dc0625007b4a2df718403b378ff5e07aa8ffcfa93c9a53d046(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    file_system_id: builtins.str,
    subnet_id: builtins.str,
    ip_address_type: typing.Optional[builtins.str] = None,
    ipv4_address: typing.Optional[builtins.str] = None,
    ipv6_address: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e72b8f6fad03e4c7b1e6b4c09d4b901e71f7b9648fe3f964118e022adccfcf(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e23055abd97201d86bb152595231b0b3346ea003d9d5ee585f10e99c7cfbd4b6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6499d4353ea6da4f35dc2332ac9a26e5bc510dbc21a2ecda30e0f06078583ff1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__326fe98b9aa7b9e0761b3a99021f1dd6b471a6f4d4a9ca0c102e6b195c7ecf58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daab55069ed7af383fae7873019670acde077fe675881a28c9798db68a3ecaae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d28efaecdcc1cd8cd7082a54495fbaf06d90b9998af31551e36609acb8dcc690(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36202d13fe4264f10d25903dc89da82589244e2cc3341f09f8fc9f1d6c83c8a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4adf1a03f0a0b33443e5404167b9ecb7ad83848432d6587ee5863a01d59a3403(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__956b509688210b28bbff0d032e9b0f348325adaeb3713163604385cafefe9f7b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38212c95a0bd3b9103e91e76c4d4b35afbd0a1902d13ea3a4d956445137335a(
    *,
    file_system_id: builtins.str,
    subnet_id: builtins.str,
    ip_address_type: typing.Optional[builtins.str] = None,
    ipv4_address: typing.Optional[builtins.str] = None,
    ipv6_address: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

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
    jsii_type="aws-cdk-lib.interfaces.aws_elementalinference.FeedReference",
    jsii_struct_bases=[],
    name_mapping={"feed_arn": "feedArn", "feed_id": "feedId"},
)
class FeedReference:
    def __init__(self, *, feed_arn: builtins.str, feed_id: builtins.str) -> None:
        '''A reference to a Feed resource.

        :param feed_arn: The ARN of the Feed resource.
        :param feed_id: The Id of the Feed resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elementalinference as interfaces_elementalinference
            
            feed_reference = interfaces_elementalinference.FeedReference(
                feed_arn="feedArn",
                feed_id="feedId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dce19c0c5001c89e98590ada4569f19f0ff03b61eaa9b881f707c8de291d35ee)
            check_type(argname="argument feed_arn", value=feed_arn, expected_type=type_hints["feed_arn"])
            check_type(argname="argument feed_id", value=feed_id, expected_type=type_hints["feed_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "feed_arn": feed_arn,
            "feed_id": feed_id,
        }

    @builtins.property
    def feed_arn(self) -> builtins.str:
        '''The ARN of the Feed resource.'''
        result = self._values.get("feed_arn")
        assert result is not None, "Required property 'feed_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def feed_id(self) -> builtins.str:
        '''The Id of the Feed resource.'''
        result = self._values.get("feed_id")
        assert result is not None, "Required property 'feed_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FeedReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elementalinference.IFeedRef")
class IFeedRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Feed.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="feedRef")
    def feed_ref(self) -> "FeedReference":
        '''(experimental) A reference to a Feed resource.

        :stability: experimental
        '''
        ...


class _IFeedRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Feed.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elementalinference.IFeedRef"

    @builtins.property
    @jsii.member(jsii_name="feedRef")
    def feed_ref(self) -> "FeedReference":
        '''(experimental) A reference to a Feed resource.

        :stability: experimental
        '''
        return typing.cast("FeedReference", jsii.get(self, "feedRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFeedRef).__jsii_proxy_class__ = lambda : _IFeedRefProxy


__all__ = [
    "FeedReference",
    "IFeedRef",
]

publication.publish()

def _typecheckingstub__dce19c0c5001c89e98590ada4569f19f0ff03b61eaa9b881f707c8de291d35ee(
    *,
    feed_arn: builtins.str,
    feed_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IFeedRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])

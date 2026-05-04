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
    jsii_type="aws-cdk-lib.interfaces.aws_bcmpricingcalculator.BillScenarioReference",
    jsii_struct_bases=[],
    name_mapping={"bill_scenario_arn": "billScenarioArn"},
)
class BillScenarioReference:
    def __init__(self, *, bill_scenario_arn: builtins.str) -> None:
        '''A reference to a BillScenario resource.

        :param bill_scenario_arn: The Arn of the BillScenario resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bcmpricingcalculator as interfaces_bcmpricingcalculator
            
            bill_scenario_reference = interfaces_bcmpricingcalculator.BillScenarioReference(
                bill_scenario_arn="billScenarioArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a4b8207a20270e6b553edc4af87ceaf942f02e0451a503352b2dd42aa4f4365)
            check_type(argname="argument bill_scenario_arn", value=bill_scenario_arn, expected_type=type_hints["bill_scenario_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bill_scenario_arn": bill_scenario_arn,
        }

    @builtins.property
    def bill_scenario_arn(self) -> builtins.str:
        '''The Arn of the BillScenario resource.'''
        result = self._values.get("bill_scenario_arn")
        assert result is not None, "Required property 'bill_scenario_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillScenarioReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bcmpricingcalculator.IBillScenarioRef"
)
class IBillScenarioRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BillScenario.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="billScenarioRef")
    def bill_scenario_ref(self) -> "BillScenarioReference":
        '''(experimental) A reference to a BillScenario resource.

        :stability: experimental
        '''
        ...


class _IBillScenarioRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BillScenario.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bcmpricingcalculator.IBillScenarioRef"

    @builtins.property
    @jsii.member(jsii_name="billScenarioRef")
    def bill_scenario_ref(self) -> "BillScenarioReference":
        '''(experimental) A reference to a BillScenario resource.

        :stability: experimental
        '''
        return typing.cast("BillScenarioReference", jsii.get(self, "billScenarioRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBillScenarioRef).__jsii_proxy_class__ = lambda : _IBillScenarioRefProxy


__all__ = [
    "BillScenarioReference",
    "IBillScenarioRef",
]

publication.publish()

def _typecheckingstub__1a4b8207a20270e6b553edc4af87ceaf942f02e0451a503352b2dd42aa4f4365(
    *,
    bill_scenario_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBillScenarioRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])

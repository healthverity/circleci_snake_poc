# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class MSPPrincipal(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Classification(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> MSPPrincipal.Classification: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[MSPPrincipal.Classification]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, MSPPrincipal.Classification]]: ...
        ROLE = typing___cast(MSPPrincipal.Classification, 0)
        ORGANIZATION_UNIT = typing___cast(MSPPrincipal.Classification, 1)
        IDENTITY = typing___cast(MSPPrincipal.Classification, 2)
        ANONYMITY = typing___cast(MSPPrincipal.Classification, 3)
        COMBINED = typing___cast(MSPPrincipal.Classification, 4)
    ROLE = typing___cast(MSPPrincipal.Classification, 0)
    ORGANIZATION_UNIT = typing___cast(MSPPrincipal.Classification, 1)
    IDENTITY = typing___cast(MSPPrincipal.Classification, 2)
    ANONYMITY = typing___cast(MSPPrincipal.Classification, 3)
    COMBINED = typing___cast(MSPPrincipal.Classification, 4)

    principal_classification = ... # type: MSPPrincipal.Classification
    principal = ... # type: bytes

    def __init__(self,
        *,
        principal_classification : typing___Optional[MSPPrincipal.Classification] = None,
        principal : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MSPPrincipal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"principal",u"principal_classification"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"principal",b"principal",u"principal_classification",b"principal_classification"]) -> None: ...

class OrganizationUnit(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    msp_identifier = ... # type: typing___Text
    organizational_unit_identifier = ... # type: typing___Text
    certifiers_identifier = ... # type: bytes

    def __init__(self,
        *,
        msp_identifier : typing___Optional[typing___Text] = None,
        organizational_unit_identifier : typing___Optional[typing___Text] = None,
        certifiers_identifier : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> OrganizationUnit: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"certifiers_identifier",u"msp_identifier",u"organizational_unit_identifier"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"certifiers_identifier",b"certifiers_identifier",u"msp_identifier",b"msp_identifier",u"organizational_unit_identifier",b"organizational_unit_identifier"]) -> None: ...

class MSPRole(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MSPRoleType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> MSPRole.MSPRoleType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[MSPRole.MSPRoleType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, MSPRole.MSPRoleType]]: ...
        MEMBER = typing___cast(MSPRole.MSPRoleType, 0)
        ADMIN = typing___cast(MSPRole.MSPRoleType, 1)
        CLIENT = typing___cast(MSPRole.MSPRoleType, 2)
        PEER = typing___cast(MSPRole.MSPRoleType, 3)
    MEMBER = typing___cast(MSPRole.MSPRoleType, 0)
    ADMIN = typing___cast(MSPRole.MSPRoleType, 1)
    CLIENT = typing___cast(MSPRole.MSPRoleType, 2)
    PEER = typing___cast(MSPRole.MSPRoleType, 3)

    msp_identifier = ... # type: typing___Text
    role = ... # type: MSPRole.MSPRoleType

    def __init__(self,
        *,
        msp_identifier : typing___Optional[typing___Text] = None,
        role : typing___Optional[MSPRole.MSPRoleType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MSPRole: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"msp_identifier",u"role"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"msp_identifier",b"msp_identifier",u"role",b"role"]) -> None: ...

class MSPIdentityAnonymity(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MSPIdentityAnonymityType(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> MSPIdentityAnonymity.MSPIdentityAnonymityType: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[MSPIdentityAnonymity.MSPIdentityAnonymityType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, MSPIdentityAnonymity.MSPIdentityAnonymityType]]: ...
        NOMINAL = typing___cast(MSPIdentityAnonymity.MSPIdentityAnonymityType, 0)
        ANONYMOUS = typing___cast(MSPIdentityAnonymity.MSPIdentityAnonymityType, 1)
    NOMINAL = typing___cast(MSPIdentityAnonymity.MSPIdentityAnonymityType, 0)
    ANONYMOUS = typing___cast(MSPIdentityAnonymity.MSPIdentityAnonymityType, 1)

    anonymity_type = ... # type: MSPIdentityAnonymity.MSPIdentityAnonymityType

    def __init__(self,
        *,
        anonymity_type : typing___Optional[MSPIdentityAnonymity.MSPIdentityAnonymityType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MSPIdentityAnonymity: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"anonymity_type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"anonymity_type",b"anonymity_type"]) -> None: ...

class CombinedPrincipal(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def principals(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MSPPrincipal]: ...

    def __init__(self,
        *,
        principals : typing___Optional[typing___Iterable[MSPPrincipal]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CombinedPrincipal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"principals"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"principals",b"principals"]) -> None: ...

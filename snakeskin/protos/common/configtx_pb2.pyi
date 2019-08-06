# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from snakeskin.protos.common.common_pb2 import (
    Envelope as snakeskin___protos___common___common_pb2___Envelope,
)

from snakeskin.protos.common.policies_pb2 import (
    Policy as snakeskin___protos___common___policies_pb2___Policy,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ConfigEnvelope(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def config(self) -> Config: ...

    @property
    def last_update(self) -> snakeskin___protos___common___common_pb2___Envelope: ...

    def __init__(self,
        *,
        config : typing___Optional[Config] = None,
        last_update : typing___Optional[snakeskin___protos___common___common_pb2___Envelope] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigEnvelope: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"config",u"last_update"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",u"last_update"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"config",b"config",u"last_update",b"last_update"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"last_update",b"last_update"]) -> None: ...

class ConfigGroupSchema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class GroupsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ConfigGroupSchema: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ConfigGroupSchema] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigGroupSchema.GroupsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ValuesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ConfigValueSchema: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ConfigValueSchema] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigGroupSchema.ValuesEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PoliciesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ConfigPolicySchema: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ConfigPolicySchema] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigGroupSchema.PoliciesEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


    @property
    def groups(self) -> typing___MutableMapping[typing___Text, ConfigGroupSchema]: ...

    @property
    def values(self) -> typing___MutableMapping[typing___Text, ConfigValueSchema]: ...

    @property
    def policies(self) -> typing___MutableMapping[typing___Text, ConfigPolicySchema]: ...

    def __init__(self,
        *,
        groups : typing___Optional[typing___Mapping[typing___Text, ConfigGroupSchema]] = None,
        values : typing___Optional[typing___Mapping[typing___Text, ConfigValueSchema]] = None,
        policies : typing___Optional[typing___Mapping[typing___Text, ConfigPolicySchema]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigGroupSchema: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"groups",u"policies",u"values"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"groups",b"groups",u"policies",b"policies",u"values",b"values"]) -> None: ...

class ConfigValueSchema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigValueSchema: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ConfigPolicySchema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigPolicySchema: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class Config(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    sequence = ... # type: int

    @property
    def channel_group(self) -> ConfigGroup: ...

    def __init__(self,
        *,
        sequence : typing___Optional[int] = None,
        channel_group : typing___Optional[ConfigGroup] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Config: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"channel_group"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"channel_group",u"sequence"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"channel_group",b"channel_group"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"channel_group",b"channel_group",u"sequence",b"sequence"]) -> None: ...

class ConfigUpdateEnvelope(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    config_update = ... # type: bytes

    @property
    def signatures(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ConfigSignature]: ...

    def __init__(self,
        *,
        config_update : typing___Optional[bytes] = None,
        signatures : typing___Optional[typing___Iterable[ConfigSignature]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigUpdateEnvelope: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"config_update",u"signatures"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"config_update",b"config_update",u"signatures",b"signatures"]) -> None: ...

class ConfigUpdate(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class IsolatedDataEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: bytes

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[bytes] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigUpdate.IsolatedDataEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    channel_id = ... # type: typing___Text

    @property
    def read_set(self) -> ConfigGroup: ...

    @property
    def write_set(self) -> ConfigGroup: ...

    @property
    def isolated_data(self) -> typing___MutableMapping[typing___Text, bytes]: ...

    def __init__(self,
        *,
        channel_id : typing___Optional[typing___Text] = None,
        read_set : typing___Optional[ConfigGroup] = None,
        write_set : typing___Optional[ConfigGroup] = None,
        isolated_data : typing___Optional[typing___Mapping[typing___Text, bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigUpdate: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"read_set",u"write_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"channel_id",u"isolated_data",u"read_set",u"write_set"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"read_set",b"read_set",u"write_set",b"write_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"channel_id",b"channel_id",u"isolated_data",b"isolated_data",u"read_set",b"read_set",u"write_set",b"write_set"]) -> None: ...

class ConfigGroup(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class GroupsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ConfigGroup: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ConfigGroup] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigGroup.GroupsEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ValuesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ConfigValue: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ConfigValue] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigGroup.ValuesEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PoliciesEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> ConfigPolicy: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[ConfigPolicy] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ConfigGroup.PoliciesEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    version = ... # type: int
    mod_policy = ... # type: typing___Text

    @property
    def groups(self) -> typing___MutableMapping[typing___Text, ConfigGroup]: ...

    @property
    def values(self) -> typing___MutableMapping[typing___Text, ConfigValue]: ...

    @property
    def policies(self) -> typing___MutableMapping[typing___Text, ConfigPolicy]: ...

    def __init__(self,
        *,
        version : typing___Optional[int] = None,
        groups : typing___Optional[typing___Mapping[typing___Text, ConfigGroup]] = None,
        values : typing___Optional[typing___Mapping[typing___Text, ConfigValue]] = None,
        policies : typing___Optional[typing___Mapping[typing___Text, ConfigPolicy]] = None,
        mod_policy : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigGroup: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"groups",u"mod_policy",u"policies",u"values",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"groups",b"groups",u"mod_policy",b"mod_policy",u"policies",b"policies",u"values",b"values",u"version",b"version"]) -> None: ...

class ConfigValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version = ... # type: int
    value = ... # type: bytes
    mod_policy = ... # type: typing___Text

    def __init__(self,
        *,
        version : typing___Optional[int] = None,
        value : typing___Optional[bytes] = None,
        mod_policy : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"mod_policy",u"value",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"mod_policy",b"mod_policy",u"value",b"value",u"version",b"version"]) -> None: ...

class ConfigPolicy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version = ... # type: int
    mod_policy = ... # type: typing___Text

    @property
    def policy(self) -> snakeskin___protos___common___policies_pb2___Policy: ...

    def __init__(self,
        *,
        version : typing___Optional[int] = None,
        policy : typing___Optional[snakeskin___protos___common___policies_pb2___Policy] = None,
        mod_policy : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigPolicy: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"policy"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"mod_policy",u"policy",u"version"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"policy",b"policy"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"mod_policy",b"mod_policy",u"policy",b"policy",u"version",b"version"]) -> None: ...

class ConfigSignature(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    signature_header = ... # type: bytes
    signature = ... # type: bytes

    def __init__(self,
        *,
        signature_header : typing___Optional[bytes] = None,
        signature : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigSignature: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"signature",u"signature_header"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"signature",b"signature",u"signature_header",b"signature_header"]) -> None: ...

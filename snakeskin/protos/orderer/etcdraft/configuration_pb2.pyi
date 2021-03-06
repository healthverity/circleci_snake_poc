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


class Metadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def consenters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Consenter]: ...

    @property
    def options(self) -> Options: ...

    def __init__(self,
        *,
        consenters : typing___Optional[typing___Iterable[Consenter]] = None,
        options : typing___Optional[Options] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Metadata: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"options"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"consenters",u"options"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"options",b"options"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"consenters",b"consenters",u"options",b"options"]) -> None: ...

class Consenter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    host = ... # type: typing___Text
    port = ... # type: int
    client_tls_cert = ... # type: bytes
    server_tls_cert = ... # type: bytes

    def __init__(self,
        *,
        host : typing___Optional[typing___Text] = None,
        port : typing___Optional[int] = None,
        client_tls_cert : typing___Optional[bytes] = None,
        server_tls_cert : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Consenter: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"client_tls_cert",u"host",u"port",u"server_tls_cert"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"client_tls_cert",b"client_tls_cert",u"host",b"host",u"port",b"port",u"server_tls_cert",b"server_tls_cert"]) -> None: ...

class Options(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    tick_interval = ... # type: int
    election_tick = ... # type: int
    heartbeat_tick = ... # type: int
    max_inflight_msgs = ... # type: int
    max_size_per_msg = ... # type: int
    snapshot_interval = ... # type: int

    def __init__(self,
        *,
        tick_interval : typing___Optional[int] = None,
        election_tick : typing___Optional[int] = None,
        heartbeat_tick : typing___Optional[int] = None,
        max_inflight_msgs : typing___Optional[int] = None,
        max_size_per_msg : typing___Optional[int] = None,
        snapshot_interval : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Options: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"election_tick",u"heartbeat_tick",u"max_inflight_msgs",u"max_size_per_msg",u"snapshot_interval",u"tick_interval"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"election_tick",b"election_tick",u"heartbeat_tick",b"heartbeat_tick",u"max_inflight_msgs",b"max_inflight_msgs",u"max_size_per_msg",b"max_size_per_msg",u"snapshot_interval",b"snapshot_interval",u"tick_interval",b"tick_interval"]) -> None: ...

class RaftMetadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ConsentersEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: int

        @property
        def value(self) -> Consenter: ...

        def __init__(self,
            *,
            key : typing___Optional[int] = None,
            value : typing___Optional[Consenter] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> RaftMetadata.ConsentersEntry: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    next_consenter_id = ... # type: int
    conf_change_counts = ... # type: int
    raft_index = ... # type: int

    @property
    def consenters(self) -> typing___MutableMapping[int, Consenter]: ...

    def __init__(self,
        *,
        consenters : typing___Optional[typing___Mapping[int, Consenter]] = None,
        next_consenter_id : typing___Optional[int] = None,
        conf_change_counts : typing___Optional[int] = None,
        raft_index : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RaftMetadata: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"conf_change_counts",u"consenters",u"next_consenter_id",u"raft_index"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"conf_change_counts",b"conf_change_counts",u"consenters",b"consenters",u"next_consenter_id",b"next_consenter_id",u"raft_index",b"raft_index"]) -> None: ...

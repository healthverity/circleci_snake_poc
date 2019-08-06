# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class KVRWSet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def reads(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVRead]: ...

    @property
    def range_queries_info(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RangeQueryInfo]: ...

    @property
    def writes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVWrite]: ...

    @property
    def metadata_writes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVMetadataWrite]: ...

    def __init__(self,
        *,
        reads : typing___Optional[typing___Iterable[KVRead]] = None,
        range_queries_info : typing___Optional[typing___Iterable[RangeQueryInfo]] = None,
        writes : typing___Optional[typing___Iterable[KVWrite]] = None,
        metadata_writes : typing___Optional[typing___Iterable[KVMetadataWrite]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVRWSet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"metadata_writes",u"range_queries_info",u"reads",u"writes"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"metadata_writes",b"metadata_writes",u"range_queries_info",b"range_queries_info",u"reads",b"reads",u"writes",b"writes"]) -> None: ...

class HashedRWSet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def hashed_reads(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVReadHash]: ...

    @property
    def hashed_writes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVWriteHash]: ...

    @property
    def metadata_writes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVMetadataWriteHash]: ...

    def __init__(self,
        *,
        hashed_reads : typing___Optional[typing___Iterable[KVReadHash]] = None,
        hashed_writes : typing___Optional[typing___Iterable[KVWriteHash]] = None,
        metadata_writes : typing___Optional[typing___Iterable[KVMetadataWriteHash]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> HashedRWSet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hashed_reads",u"hashed_writes",u"metadata_writes"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hashed_reads",b"hashed_reads",u"hashed_writes",b"hashed_writes",u"metadata_writes",b"metadata_writes"]) -> None: ...

class KVRead(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key = ... # type: typing___Text

    @property
    def version(self) -> Version: ...

    def __init__(self,
        *,
        key : typing___Optional[typing___Text] = None,
        version : typing___Optional[Version] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVRead: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"version"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",u"version"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"version",b"version"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"version",b"version"]) -> None: ...

class KVWrite(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key = ... # type: typing___Text
    is_delete = ... # type: bool
    value = ... # type: bytes

    def __init__(self,
        *,
        key : typing___Optional[typing___Text] = None,
        is_delete : typing___Optional[bool] = None,
        value : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVWrite: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"is_delete",u"key",u"value"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"is_delete",b"is_delete",u"key",b"key",u"value",b"value"]) -> None: ...

class KVMetadataWrite(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key = ... # type: typing___Text

    @property
    def entries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVMetadataEntry]: ...

    def __init__(self,
        *,
        key : typing___Optional[typing___Text] = None,
        entries : typing___Optional[typing___Iterable[KVMetadataEntry]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVMetadataWrite: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"entries",u"key"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"entries",b"entries",u"key",b"key"]) -> None: ...

class KVReadHash(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key_hash = ... # type: bytes

    @property
    def version(self) -> Version: ...

    def __init__(self,
        *,
        key_hash : typing___Optional[bytes] = None,
        version : typing___Optional[Version] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVReadHash: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"version"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key_hash",u"version"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"version",b"version"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key_hash",b"key_hash",u"version",b"version"]) -> None: ...

class KVWriteHash(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key_hash = ... # type: bytes
    is_delete = ... # type: bool
    value_hash = ... # type: bytes

    def __init__(self,
        *,
        key_hash : typing___Optional[bytes] = None,
        is_delete : typing___Optional[bool] = None,
        value_hash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVWriteHash: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"is_delete",u"key_hash",u"value_hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"is_delete",b"is_delete",u"key_hash",b"key_hash",u"value_hash",b"value_hash"]) -> None: ...

class KVMetadataWriteHash(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key_hash = ... # type: bytes

    @property
    def entries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVMetadataEntry]: ...

    def __init__(self,
        *,
        key_hash : typing___Optional[bytes] = None,
        entries : typing___Optional[typing___Iterable[KVMetadataEntry]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVMetadataWriteHash: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"entries",u"key_hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"entries",b"entries",u"key_hash",b"key_hash"]) -> None: ...

class KVMetadataEntry(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    value = ... # type: bytes

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        value : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KVMetadataEntry: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"name",u"value"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"value",b"value"]) -> None: ...

class Version(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    block_num = ... # type: int
    tx_num = ... # type: int

    def __init__(self,
        *,
        block_num : typing___Optional[int] = None,
        tx_num : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Version: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"block_num",u"tx_num"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"block_num",b"block_num",u"tx_num",b"tx_num"]) -> None: ...

class RangeQueryInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start_key = ... # type: typing___Text
    end_key = ... # type: typing___Text
    itr_exhausted = ... # type: bool

    @property
    def raw_reads(self) -> QueryReads: ...

    @property
    def reads_merkle_hashes(self) -> QueryReadsMerkleSummary: ...

    def __init__(self,
        *,
        start_key : typing___Optional[typing___Text] = None,
        end_key : typing___Optional[typing___Text] = None,
        itr_exhausted : typing___Optional[bool] = None,
        raw_reads : typing___Optional[QueryReads] = None,
        reads_merkle_hashes : typing___Optional[QueryReadsMerkleSummary] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RangeQueryInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"raw_reads",u"reads_info",u"reads_merkle_hashes"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"end_key",u"itr_exhausted",u"raw_reads",u"reads_info",u"reads_merkle_hashes",u"start_key"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"raw_reads",b"raw_reads",u"reads_info",b"reads_info",u"reads_merkle_hashes",b"reads_merkle_hashes"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"end_key",b"end_key",u"itr_exhausted",b"itr_exhausted",u"raw_reads",b"raw_reads",u"reads_info",b"reads_info",u"reads_merkle_hashes",b"reads_merkle_hashes",u"start_key",b"start_key"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"reads_info",b"reads_info"]) -> typing_extensions___Literal["raw_reads","reads_merkle_hashes"]: ...

class QueryReads(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def kv_reads(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[KVRead]: ...

    def __init__(self,
        *,
        kv_reads : typing___Optional[typing___Iterable[KVRead]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> QueryReads: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"kv_reads"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"kv_reads",b"kv_reads"]) -> None: ...

class QueryReadsMerkleSummary(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    max_degree = ... # type: int
    max_level = ... # type: int
    max_level_hashes = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]

    def __init__(self,
        *,
        max_degree : typing___Optional[int] = None,
        max_level : typing___Optional[int] = None,
        max_level_hashes : typing___Optional[typing___Iterable[bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> QueryReadsMerkleSummary: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"max_degree",u"max_level",u"max_level_hashes"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"max_degree",b"max_degree",u"max_level",b"max_level",u"max_level_hashes",b"max_level_hashes"]) -> None: ...

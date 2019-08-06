# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snakeskin/protos/peer/configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='snakeskin/protos/peer/configuration.proto',
  package='protos',
  syntax='proto3',
  serialized_options=_b('\n\"org.hyperledger.fabric.protos.peerZ)github.com/hyperledger/fabric/protos/peer'),
  serialized_pb=_b('\n)snakeskin/protos/peer/configuration.proto\x12\x06protos\"7\n\x0b\x41nchorPeers\x12(\n\x0c\x61nchor_peers\x18\x01 \x03(\x0b\x32\x12.protos.AnchorPeer\"(\n\nAnchorPeer\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"!\n\x0b\x41PIResource\x12\x12\n\npolicy_ref\x18\x01 \x01(\t\"n\n\x04\x41\x43Ls\x12$\n\x04\x61\x63ls\x18\x01 \x03(\x0b\x32\x16.protos.ACLs.AclsEntry\x1a@\n\tAclsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.protos.APIResource:\x02\x38\x01\x42O\n\"org.hyperledger.fabric.protos.peerZ)github.com/hyperledger/fabric/protos/peerb\x06proto3')
)




_ANCHORPEERS = _descriptor.Descriptor(
  name='AnchorPeers',
  full_name='protos.AnchorPeers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_peers', full_name='protos.AnchorPeers.anchor_peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=108,
)


_ANCHORPEER = _descriptor.Descriptor(
  name='AnchorPeer',
  full_name='protos.AnchorPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='protos.AnchorPeer.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.AnchorPeer.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=150,
)


_APIRESOURCE = _descriptor.Descriptor(
  name='APIResource',
  full_name='protos.APIResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_ref', full_name='protos.APIResource.policy_ref', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=185,
)


_ACLS_ACLSENTRY = _descriptor.Descriptor(
  name='AclsEntry',
  full_name='protos.ACLs.AclsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.ACLs.AclsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.ACLs.AclsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=297,
)

_ACLS = _descriptor.Descriptor(
  name='ACLs',
  full_name='protos.ACLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acls', full_name='protos.ACLs.acls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACLS_ACLSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=297,
)

_ANCHORPEERS.fields_by_name['anchor_peers'].message_type = _ANCHORPEER
_ACLS_ACLSENTRY.fields_by_name['value'].message_type = _APIRESOURCE
_ACLS_ACLSENTRY.containing_type = _ACLS
_ACLS.fields_by_name['acls'].message_type = _ACLS_ACLSENTRY
DESCRIPTOR.message_types_by_name['AnchorPeers'] = _ANCHORPEERS
DESCRIPTOR.message_types_by_name['AnchorPeer'] = _ANCHORPEER
DESCRIPTOR.message_types_by_name['APIResource'] = _APIRESOURCE
DESCRIPTOR.message_types_by_name['ACLs'] = _ACLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnchorPeers = _reflection.GeneratedProtocolMessageType('AnchorPeers', (_message.Message,), {
  'DESCRIPTOR' : _ANCHORPEERS,
  '__module__' : 'snakeskin.protos.peer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:protos.AnchorPeers)
  })
_sym_db.RegisterMessage(AnchorPeers)

AnchorPeer = _reflection.GeneratedProtocolMessageType('AnchorPeer', (_message.Message,), {
  'DESCRIPTOR' : _ANCHORPEER,
  '__module__' : 'snakeskin.protos.peer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:protos.AnchorPeer)
  })
_sym_db.RegisterMessage(AnchorPeer)

APIResource = _reflection.GeneratedProtocolMessageType('APIResource', (_message.Message,), {
  'DESCRIPTOR' : _APIRESOURCE,
  '__module__' : 'snakeskin.protos.peer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:protos.APIResource)
  })
_sym_db.RegisterMessage(APIResource)

ACLs = _reflection.GeneratedProtocolMessageType('ACLs', (_message.Message,), {

  'AclsEntry' : _reflection.GeneratedProtocolMessageType('AclsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACLS_ACLSENTRY,
    '__module__' : 'snakeskin.protos.peer.configuration_pb2'
    # @@protoc_insertion_point(class_scope:protos.ACLs.AclsEntry)
    })
  ,
  'DESCRIPTOR' : _ACLS,
  '__module__' : 'snakeskin.protos.peer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:protos.ACLs)
  })
_sym_db.RegisterMessage(ACLs)
_sym_db.RegisterMessage(ACLs.AclsEntry)


DESCRIPTOR._options = None
_ACLS_ACLSENTRY._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snakeskin/protos/peer/signed_cc_dep_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from snakeskin.protos.peer import proposal_response_pb2 as snakeskin_dot_protos_dot_peer_dot_proposal__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='snakeskin/protos/peer/signed_cc_dep_spec.proto',
  package='protos',
  syntax='proto3',
  serialized_options=_b('\n\"org.hyperledger.fabric.protos.peerZ)github.com/hyperledger/fabric/protos/peer'),
  serialized_pb=_b('\n.snakeskin/protos/peer/signed_cc_dep_spec.proto\x12\x06protos\x1a-snakeskin/protos/peer/proposal_response.proto\"\x91\x01\n\x1dSignedChaincodeDeploymentSpec\x12!\n\x19\x63haincode_deployment_spec\x18\x01 \x01(\x0c\x12\x1c\n\x14instantiation_policy\x18\x02 \x01(\x0c\x12/\n\x12owner_endorsements\x18\x03 \x03(\x0b\x32\x13.protos.EndorsementBO\n\"org.hyperledger.fabric.protos.peerZ)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[snakeskin_dot_protos_dot_peer_dot_proposal__response__pb2.DESCRIPTOR,])




_SIGNEDCHAINCODEDEPLOYMENTSPEC = _descriptor.Descriptor(
  name='SignedChaincodeDeploymentSpec',
  full_name='protos.SignedChaincodeDeploymentSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_deployment_spec', full_name='protos.SignedChaincodeDeploymentSpec.chaincode_deployment_spec', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instantiation_policy', full_name='protos.SignedChaincodeDeploymentSpec.instantiation_policy', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner_endorsements', full_name='protos.SignedChaincodeDeploymentSpec.owner_endorsements', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=106,
  serialized_end=251,
)

_SIGNEDCHAINCODEDEPLOYMENTSPEC.fields_by_name['owner_endorsements'].message_type = snakeskin_dot_protos_dot_peer_dot_proposal__response__pb2._ENDORSEMENT
DESCRIPTOR.message_types_by_name['SignedChaincodeDeploymentSpec'] = _SIGNEDCHAINCODEDEPLOYMENTSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignedChaincodeDeploymentSpec = _reflection.GeneratedProtocolMessageType('SignedChaincodeDeploymentSpec', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDCHAINCODEDEPLOYMENTSPEC,
  '__module__' : 'snakeskin.protos.peer.signed_cc_dep_spec_pb2'
  # @@protoc_insertion_point(class_scope:protos.SignedChaincodeDeploymentSpec)
  })
_sym_db.RegisterMessage(SignedChaincodeDeploymentSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

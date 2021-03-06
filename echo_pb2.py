# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo.proto',
  package='tenori',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\necho.proto\x12\x06tenori\"\'\n\x0b\x45\x63hoRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0b\n\x03log\x18\x02 \x01(\x08\"\x19\n\tEchoReply\x12\x0c\n\x04resp\x18\x01 \x01(\t2C\n\x0b\x45\x63hoService\x12\x34\n\x04\x65\x63ho\x12\x13.tenori.EchoRequest\x1a\x11.tenori.EchoReply\"\x00(\x01\x30\x01\x62\x06proto3'
)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='tenori.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='tenori.EchoRequest.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='tenori.EchoRequest.log', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=22,
  serialized_end=61,
)


_ECHOREPLY = _descriptor.Descriptor(
  name='EchoReply',
  full_name='tenori.EchoReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='tenori.EchoReply.resp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=63,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoReply'] = _ECHOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:tenori.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoReply = _reflection.GeneratedProtocolMessageType('EchoReply', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREPLY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:tenori.EchoReply)
  })
_sym_db.RegisterMessage(EchoReply)



_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='tenori.EchoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=90,
  serialized_end=157,
  methods=[
  _descriptor.MethodDescriptor(
    name='echo',
    full_name='tenori.EchoService.echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHOREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHOSERVICE)

DESCRIPTOR.services_by_name['EchoService'] = _ECHOSERVICE

# @@protoc_insertion_point(module_scope)

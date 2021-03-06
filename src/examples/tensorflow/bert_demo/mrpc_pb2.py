# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mrpc.proto',
  package='mrpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nmrpc.proto\x12\x04mrpc\"*\n\x08TextPair\x12\x0e\n\x06text_a\x18\x01 \x01(\x0c\x12\x0e\n\x06text_b\x18\x02 \x01(\x0c\",\n\x05YesNo\x12\x0f\n\x07message\x18\x01 \x01(\x0c\x12\x12\n\nprediction\x18\x02 \x01(\x0c\x32\x33\n\x04mrpc\x12+\n\nparaphrase\x12\x0e.mrpc.TextPair\x1a\x0b.mrpc.YesNo\"\x00\x62\x06proto3')
)




_TEXTPAIR = _descriptor.Descriptor(
  name='TextPair',
  full_name='mrpc.TextPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_a', full_name='mrpc.TextPair.text_a', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_b', full_name='mrpc.TextPair.text_b', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=20,
  serialized_end=62,
)


_YESNO = _descriptor.Descriptor(
  name='YesNo',
  full_name='mrpc.YesNo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='mrpc.YesNo.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='mrpc.YesNo.prediction', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=64,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['TextPair'] = _TEXTPAIR
DESCRIPTOR.message_types_by_name['YesNo'] = _YESNO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextPair = _reflection.GeneratedProtocolMessageType('TextPair', (_message.Message,), {
  'DESCRIPTOR' : _TEXTPAIR,
  '__module__' : 'mrpc_pb2'
  # @@protoc_insertion_point(class_scope:mrpc.TextPair)
  })
_sym_db.RegisterMessage(TextPair)

YesNo = _reflection.GeneratedProtocolMessageType('YesNo', (_message.Message,), {
  'DESCRIPTOR' : _YESNO,
  '__module__' : 'mrpc_pb2'
  # @@protoc_insertion_point(class_scope:mrpc.YesNo)
  })
_sym_db.RegisterMessage(YesNo)



_MRPC = _descriptor.ServiceDescriptor(
  name='mrpc',
  full_name='mrpc.mrpc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=110,
  serialized_end=161,
  methods=[
  _descriptor.MethodDescriptor(
    name='paraphrase',
    full_name='mrpc.mrpc.paraphrase',
    index=0,
    containing_service=None,
    input_type=_TEXTPAIR,
    output_type=_YESNO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MRPC)

DESCRIPTOR.services_by_name['mrpc'] = _MRPC

# @@protoc_insertion_point(module_scope)

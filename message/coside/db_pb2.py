# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/coside/db.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from message.coside import coside_pb2 as message_dot_coside_dot_coside__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='message/coside/db.proto',
  package='backend.db',
  syntax='proto3',
  serialized_pb=_b('\n\x17message/coside/db.proto\x12\nbackend.db\x1a\x1bmessage/coside/coside.proto\"]\n\x0c\x44\x61taRequired\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tnode_name\x18\x02 \x01(\t\x12.\n\x05\x62lock\x18\x03 \x01(\x0e\x32\x1f.backend.coside.SimulationBlock\"e\n\x0cHeatPumpInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06t_lake\x18\x02 \x01(\x02\x12\r\n\x05t_set\x18\x03 \x01(\x02\x12\x12\n\nmflow_lake\x18\x04 \x01(\x02\x12\x16\n\x0emflow_lake_src\x18\x05 \x01(\x02\"z\n\tStoreData\x12\x15\n\rsimulation_id\x18\x01 \x01(\t\x12\x0f\n\x07node_id\x18\x02 \x01(\t\x12\x16\n\x0e\x61ttribute_name\x18\x03 \x01(\t\x12\x10\n\x08timestep\x18\x04 \x01(\x02\x12\r\n\x05value\x18\x05 \x01(\x02\x12\x0c\n\x04unit\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[message_dot_coside_dot_coside__pb2.DESCRIPTOR,])




_DATAREQUIRED = _descriptor.Descriptor(
  name='DataRequired',
  full_name='backend.db.DataRequired',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='backend.db.DataRequired.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='backend.db.DataRequired.node_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='backend.db.DataRequired.block', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=161,
)


_HEATPUMPINFO = _descriptor.Descriptor(
  name='HeatPumpInfo',
  full_name='backend.db.HeatPumpInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='backend.db.HeatPumpInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_lake', full_name='backend.db.HeatPumpInfo.t_lake', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_set', full_name='backend.db.HeatPumpInfo.t_set', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mflow_lake', full_name='backend.db.HeatPumpInfo.mflow_lake', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mflow_lake_src', full_name='backend.db.HeatPumpInfo.mflow_lake_src', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=264,
)


_STOREDATA = _descriptor.Descriptor(
  name='StoreData',
  full_name='backend.db.StoreData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulation_id', full_name='backend.db.StoreData.simulation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='backend.db.StoreData.node_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute_name', full_name='backend.db.StoreData.attribute_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestep', full_name='backend.db.StoreData.timestep', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='backend.db.StoreData.value', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='backend.db.StoreData.unit', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=388,
)

_DATAREQUIRED.fields_by_name['block'].enum_type = message_dot_coside_dot_coside__pb2._SIMULATIONBLOCK
DESCRIPTOR.message_types_by_name['DataRequired'] = _DATAREQUIRED
DESCRIPTOR.message_types_by_name['HeatPumpInfo'] = _HEATPUMPINFO
DESCRIPTOR.message_types_by_name['StoreData'] = _STOREDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataRequired = _reflection.GeneratedProtocolMessageType('DataRequired', (_message.Message,), dict(
  DESCRIPTOR = _DATAREQUIRED,
  __module__ = 'message.coside.db_pb2'
  # @@protoc_insertion_point(class_scope:backend.db.DataRequired)
  ))
_sym_db.RegisterMessage(DataRequired)

HeatPumpInfo = _reflection.GeneratedProtocolMessageType('HeatPumpInfo', (_message.Message,), dict(
  DESCRIPTOR = _HEATPUMPINFO,
  __module__ = 'message.coside.db_pb2'
  # @@protoc_insertion_point(class_scope:backend.db.HeatPumpInfo)
  ))
_sym_db.RegisterMessage(HeatPumpInfo)

StoreData = _reflection.GeneratedProtocolMessageType('StoreData', (_message.Message,), dict(
  DESCRIPTOR = _STOREDATA,
  __module__ = 'message.coside.db_pb2'
  # @@protoc_insertion_point(class_scope:backend.db.StoreData)
  ))
_sym_db.RegisterMessage(StoreData)


# @@protoc_insertion_point(module_scope)

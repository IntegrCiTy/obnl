# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message/coside/coside.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message/coside/coside.proto',
  package='backend.coside',
  syntax='proto3',
  serialized_pb=_b('\n\x1bmessage/coside/coside.proto\x12\x0e\x62\x61\x63kend.coside\"\xe9\x01\n\x0fSimulationModel\x12\x39\n\x10the_parent_block\x18\x01 \x01(\x0e\x32\x1f.backend.coside.SimulationBlock\x12\x45\n\x08the_type\x18\x02 \x01(\x0e\x32\x33.backend.coside.SimulationModel.SimulationModelType\x12\x13\n\x0bstored_data\x18\x03 \x03(\t\"?\n\x13SimulationModelType\x12\t\n\x05OTHER\x10\x00\x12\r\n\tSIMPLE_HP\x10\x01\x12\x0e\n\nCOMPLEX_HP\x10\x02\"n\n\x0eSimulationInit\x12-\n\x05nodes\x18\x01 \x03(\x0b\x32\x1e.backend.coside.NodeSimulation\x12-\n\x05links\x18\x02 \x03(\x0b\x32\x1e.backend.coside.LinkSimulation\"o\n\x0eNodeSimulation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x05\x62lock\x18\x02 \x01(\x0e\x32\x1f.backend.coside.SimulationBlock\x12\x0e\n\x06inputs\x18\x03 \x03(\t\x12\x0f\n\x07outputs\x18\x04 \x03(\t\"y\n\x0eLinkSimulation\x12\x32\n\x05input\x18\x01 \x01(\x0b\x32#.backend.coside.ConnectorSimulation\x12\x33\n\x06output\x18\x02 \x01(\x0b\x32#.backend.coside.ConnectorSimulation\"6\n\x13\x43onnectorSimulation\x12\x0c\n\x04node\x18\x01 \x01(\t\x12\x11\n\tattribute\x18\x02 \x01(\t\"Z\n\x08Schedule\x12\x17\n\x0fsimulation_name\x18\x01 \x01(\t\x12&\n\x08schedule\x18\x02 \x03(\x0b\x32\x14.backend.coside.Step\x12\r\n\x05steps\x18\x03 \x03(\x02\"\x1a\n\x04Step\x12\x12\n\nnode_names\x18\x01 \x03(\t\"\x11\n\x0fStartSimulation*@\n\x0fSimulationBlock\x12\t\n\x05OTHER\x10\x00\x12\r\n\tHEAT_PUMP\x10\x01\x12\x13\n\x0fTHERMAL_NETWORK\x10\x02\x62\x06proto3')
)

_SIMULATIONBLOCK = _descriptor.EnumDescriptor(
  name='SimulationBlock',
  full_name='backend.coside.SimulationBlock',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEAT_PUMP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THERMAL_NETWORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=826,
  serialized_end=890,
)
_sym_db.RegisterEnumDescriptor(_SIMULATIONBLOCK)

SimulationBlock = enum_type_wrapper.EnumTypeWrapper(_SIMULATIONBLOCK)
OTHER = 0
HEAT_PUMP = 1
THERMAL_NETWORK = 2


_SIMULATIONMODEL_SIMULATIONMODELTYPE = _descriptor.EnumDescriptor(
  name='SimulationModelType',
  full_name='backend.coside.SimulationModel.SimulationModelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_HP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLEX_HP', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=218,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_SIMULATIONMODEL_SIMULATIONMODELTYPE)


_SIMULATIONMODEL = _descriptor.Descriptor(
  name='SimulationModel',
  full_name='backend.coside.SimulationModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='the_parent_block', full_name='backend.coside.SimulationModel.the_parent_block', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='the_type', full_name='backend.coside.SimulationModel.the_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stored_data', full_name='backend.coside.SimulationModel.stored_data', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIMULATIONMODEL_SIMULATIONMODELTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=281,
)


_SIMULATIONINIT = _descriptor.Descriptor(
  name='SimulationInit',
  full_name='backend.coside.SimulationInit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='backend.coside.SimulationInit.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links', full_name='backend.coside.SimulationInit.links', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=283,
  serialized_end=393,
)


_NODESIMULATION = _descriptor.Descriptor(
  name='NodeSimulation',
  full_name='backend.coside.NodeSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='backend.coside.NodeSimulation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='backend.coside.NodeSimulation.block', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='backend.coside.NodeSimulation.inputs', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='backend.coside.NodeSimulation.outputs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=395,
  serialized_end=506,
)


_LINKSIMULATION = _descriptor.Descriptor(
  name='LinkSimulation',
  full_name='backend.coside.LinkSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='backend.coside.LinkSimulation.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='backend.coside.LinkSimulation.output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=508,
  serialized_end=629,
)


_CONNECTORSIMULATION = _descriptor.Descriptor(
  name='ConnectorSimulation',
  full_name='backend.coside.ConnectorSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='backend.coside.ConnectorSimulation.node', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='backend.coside.ConnectorSimulation.attribute', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=631,
  serialized_end=685,
)


_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='backend.coside.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simulation_name', full_name='backend.coside.Schedule.simulation_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='backend.coside.Schedule.schedule', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps', full_name='backend.coside.Schedule.steps', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=687,
  serialized_end=777,
)


_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='backend.coside.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_names', full_name='backend.coside.Step.node_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=779,
  serialized_end=805,
)


_STARTSIMULATION = _descriptor.Descriptor(
  name='StartSimulation',
  full_name='backend.coside.StartSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=807,
  serialized_end=824,
)

_SIMULATIONMODEL.fields_by_name['the_parent_block'].enum_type = _SIMULATIONBLOCK
_SIMULATIONMODEL.fields_by_name['the_type'].enum_type = _SIMULATIONMODEL_SIMULATIONMODELTYPE
_SIMULATIONMODEL_SIMULATIONMODELTYPE.containing_type = _SIMULATIONMODEL
_SIMULATIONINIT.fields_by_name['nodes'].message_type = _NODESIMULATION
_SIMULATIONINIT.fields_by_name['links'].message_type = _LINKSIMULATION
_NODESIMULATION.fields_by_name['block'].enum_type = _SIMULATIONBLOCK
_LINKSIMULATION.fields_by_name['input'].message_type = _CONNECTORSIMULATION
_LINKSIMULATION.fields_by_name['output'].message_type = _CONNECTORSIMULATION
_SCHEDULE.fields_by_name['schedule'].message_type = _STEP
DESCRIPTOR.message_types_by_name['SimulationModel'] = _SIMULATIONMODEL
DESCRIPTOR.message_types_by_name['SimulationInit'] = _SIMULATIONINIT
DESCRIPTOR.message_types_by_name['NodeSimulation'] = _NODESIMULATION
DESCRIPTOR.message_types_by_name['LinkSimulation'] = _LINKSIMULATION
DESCRIPTOR.message_types_by_name['ConnectorSimulation'] = _CONNECTORSIMULATION
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['Step'] = _STEP
DESCRIPTOR.message_types_by_name['StartSimulation'] = _STARTSIMULATION
DESCRIPTOR.enum_types_by_name['SimulationBlock'] = _SIMULATIONBLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimulationModel = _reflection.GeneratedProtocolMessageType('SimulationModel', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATIONMODEL,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.SimulationModel)
  ))
_sym_db.RegisterMessage(SimulationModel)

SimulationInit = _reflection.GeneratedProtocolMessageType('SimulationInit', (_message.Message,), dict(
  DESCRIPTOR = _SIMULATIONINIT,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.SimulationInit)
  ))
_sym_db.RegisterMessage(SimulationInit)

NodeSimulation = _reflection.GeneratedProtocolMessageType('NodeSimulation', (_message.Message,), dict(
  DESCRIPTOR = _NODESIMULATION,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.NodeSimulation)
  ))
_sym_db.RegisterMessage(NodeSimulation)

LinkSimulation = _reflection.GeneratedProtocolMessageType('LinkSimulation', (_message.Message,), dict(
  DESCRIPTOR = _LINKSIMULATION,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.LinkSimulation)
  ))
_sym_db.RegisterMessage(LinkSimulation)

ConnectorSimulation = _reflection.GeneratedProtocolMessageType('ConnectorSimulation', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTORSIMULATION,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.ConnectorSimulation)
  ))
_sym_db.RegisterMessage(ConnectorSimulation)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.Schedule)
  ))
_sym_db.RegisterMessage(Schedule)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), dict(
  DESCRIPTOR = _STEP,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.Step)
  ))
_sym_db.RegisterMessage(Step)

StartSimulation = _reflection.GeneratedProtocolMessageType('StartSimulation', (_message.Message,), dict(
  DESCRIPTOR = _STARTSIMULATION,
  __module__ = 'message.coside.coside_pb2'
  # @@protoc_insertion_point(class_scope:backend.coside.StartSimulation)
  ))
_sym_db.RegisterMessage(StartSimulation)


# @@protoc_insertion_point(module_scope)
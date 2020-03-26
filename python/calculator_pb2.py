# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10\x63\x61lculator.proto\"_\n\x0f\x42inaryOperation\x12\x15\n\rfirst_operand\x18\x01 \x01(\x02\x12\x16\n\x0esecond_operand\x18\x02 \x01(\x02\x12\x1d\n\toperation\x18\x03 \x01(\x0e\x32\n.Operation\"0\n\rComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02\"\x80\x01\n\x10\x43omplexOperation\x12%\n\rfirst_operand\x18\x01 \x01(\x0b\x32\x0e.ComplexNumber\x12&\n\x0esecond_operand\x18\x02 \x01(\x0b\x32\x0e.ComplexNumber\x12\x1d\n\toperation\x18\x03 \x01(\x0e\x32\n.Operation\"#\n\x11\x43\x61lculationResult\x12\x0e\n\x06result\x18\x01 \x01(\x02\"/\n\rComplexResult\x12\x1e\n\x06result\x18\x01 \x01(\x0b\x32\x0e.ComplexNumber*\"\n\tOperation\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\x0c\n\x08SUBTRACT\x10\x01\x32v\n\nCalculator\x12\x31\n\tCalculate\x12\x10.BinaryOperation\x1a\x12.CalculationResult\x12\x35\n\x10\x43\x61lculateComplex\x12\x11.ComplexOperation\x1a\x0e.ComplexResultb\x06proto3'
)

_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBTRACT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=384,
  serialized_end=418,
)
_sym_db.RegisterEnumDescriptor(_OPERATION)

Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
ADD = 0
SUBTRACT = 1



_BINARYOPERATION = _descriptor.Descriptor(
  name='BinaryOperation',
  full_name='BinaryOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_operand', full_name='BinaryOperation.first_operand', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_operand', full_name='BinaryOperation.second_operand', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='BinaryOperation.operation', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=20,
  serialized_end=115,
)


_COMPLEXNUMBER = _descriptor.Descriptor(
  name='ComplexNumber',
  full_name='ComplexNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='real', full_name='ComplexNumber.real', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imaginary', full_name='ComplexNumber.imaginary', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=117,
  serialized_end=165,
)


_COMPLEXOPERATION = _descriptor.Descriptor(
  name='ComplexOperation',
  full_name='ComplexOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_operand', full_name='ComplexOperation.first_operand', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_operand', full_name='ComplexOperation.second_operand', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='ComplexOperation.operation', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=168,
  serialized_end=296,
)


_CALCULATIONRESULT = _descriptor.Descriptor(
  name='CalculationResult',
  full_name='CalculationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CalculationResult.result', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=298,
  serialized_end=333,
)


_COMPLEXRESULT = _descriptor.Descriptor(
  name='ComplexResult',
  full_name='ComplexResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ComplexResult.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=382,
)

_BINARYOPERATION.fields_by_name['operation'].enum_type = _OPERATION
_COMPLEXOPERATION.fields_by_name['first_operand'].message_type = _COMPLEXNUMBER
_COMPLEXOPERATION.fields_by_name['second_operand'].message_type = _COMPLEXNUMBER
_COMPLEXOPERATION.fields_by_name['operation'].enum_type = _OPERATION
_COMPLEXRESULT.fields_by_name['result'].message_type = _COMPLEXNUMBER
DESCRIPTOR.message_types_by_name['BinaryOperation'] = _BINARYOPERATION
DESCRIPTOR.message_types_by_name['ComplexNumber'] = _COMPLEXNUMBER
DESCRIPTOR.message_types_by_name['ComplexOperation'] = _COMPLEXOPERATION
DESCRIPTOR.message_types_by_name['CalculationResult'] = _CALCULATIONRESULT
DESCRIPTOR.message_types_by_name['ComplexResult'] = _COMPLEXRESULT
DESCRIPTOR.enum_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BinaryOperation = _reflection.GeneratedProtocolMessageType('BinaryOperation', (_message.Message,), {
  'DESCRIPTOR' : _BINARYOPERATION,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:BinaryOperation)
  })
_sym_db.RegisterMessage(BinaryOperation)

ComplexNumber = _reflection.GeneratedProtocolMessageType('ComplexNumber', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXNUMBER,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ComplexNumber)
  })
_sym_db.RegisterMessage(ComplexNumber)

ComplexOperation = _reflection.GeneratedProtocolMessageType('ComplexOperation', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXOPERATION,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ComplexOperation)
  })
_sym_db.RegisterMessage(ComplexOperation)

CalculationResult = _reflection.GeneratedProtocolMessageType('CalculationResult', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATIONRESULT,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:CalculationResult)
  })
_sym_db.RegisterMessage(CalculationResult)

ComplexResult = _reflection.GeneratedProtocolMessageType('ComplexResult', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXRESULT,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:ComplexResult)
  })
_sym_db.RegisterMessage(ComplexResult)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=420,
  serialized_end=538,
  methods=[
  _descriptor.MethodDescriptor(
    name='Calculate',
    full_name='Calculator.Calculate',
    index=0,
    containing_service=None,
    input_type=_BINARYOPERATION,
    output_type=_CALCULATIONRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CalculateComplex',
    full_name='Calculator.CalculateComplex',
    index=1,
    containing_service=None,
    input_type=_COMPLEXOPERATION,
    output_type=_COMPLEXRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
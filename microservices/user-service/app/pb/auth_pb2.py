# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/auth.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpb/auth.proto\x12\x04\x61uth\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\'\n\x0eRefreshRequest\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\"\x1e\n\rVerifyRequest\x12\r\n\x05token\x18\x01 \x01(\t\"P\n\rTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\x03\"D\n\x0eVerifyResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t2\xb4\x01\n\x0b\x41uthService\x12\x30\n\x05Login\x12\x12.auth.LoginRequest\x1a\x13.auth.TokenResponse\x12\x39\n\x0cRefreshToken\x12\x14.auth.RefreshRequest\x1a\x13.auth.TokenResponse\x12\x38\n\x0bVerifyToken\x12\x13.auth.VerifyRequest\x1a\x14.auth.VerifyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pb.auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOGINREQUEST']._serialized_start=23
  _globals['_LOGINREQUEST']._serialized_end=73
  _globals['_REFRESHREQUEST']._serialized_start=75
  _globals['_REFRESHREQUEST']._serialized_end=114
  _globals['_VERIFYREQUEST']._serialized_start=116
  _globals['_VERIFYREQUEST']._serialized_end=146
  _globals['_TOKENRESPONSE']._serialized_start=148
  _globals['_TOKENRESPONSE']._serialized_end=228
  _globals['_VERIFYRESPONSE']._serialized_start=230
  _globals['_VERIFYRESPONSE']._serialized_end=298
  _globals['_AUTHSERVICE']._serialized_start=301
  _globals['_AUTHSERVICE']._serialized_end=481
# @@protoc_insertion_point(module_scope)
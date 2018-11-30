# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/matching_function.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/common/matching_function.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_pb=_b('\n<google/ads/googleads_v0/proto/common/matching_function.proto\x12\x1egoogle.ads.googleads.v0.common\x1a\x1egoogle/protobuf/wrappers.proto\"I\n\x10MatchingFunction\x12\x35\n\x0f\x66unction_string\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xcb\x01\n\"com.google.ads.googleads.v0.commonB\x15MatchingFunctionProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_MATCHINGFUNCTION = _descriptor.Descriptor(
  name='MatchingFunction',
  full_name='google.ads.googleads.v0.common.MatchingFunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_string', full_name='google.ads.googleads.v0.common.MatchingFunction.function_string', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=128,
  serialized_end=201,
)

_MATCHINGFUNCTION.fields_by_name['function_string'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['MatchingFunction'] = _MATCHINGFUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchingFunction = _reflection.GeneratedProtocolMessageType('MatchingFunction', (_message.Message,), dict(
  DESCRIPTOR = _MATCHINGFUNCTION,
  __module__ = 'google.ads.google_ads.v0.proto.common.matching_function_pb2'
  ,
  __doc__ = """Matching function associated with a CustomerFeed, CampaignFeed, or
  AdGroupFeed. The matching function is used to filter the set of feed
  items selected.
  
  
  Attributes:
      function_string:
          String representation of the Function.  Examples: 1)
          IDENTITY(true) or IDENTITY(false). All or none feed items
          serve. 2) EQUALS(CONTEXT.DEVICE,"Mobile") 3)
          IN(FEED\_ITEM\_ID,{1000001,1000002,1000003}) 4)
          CONTAINS\_ANY(FeedAttribute[12345678,0],{"Mars cruise","Venus
          cruise"}) 5) AND(IN(FEED\_ITEM\_ID,{10001,10002}),EQUALS(CONTE
          XT.DEVICE,"Mobile")) See https:
          //developers.google.com/adwords/api/docs/guides/feed-matching-
          functions  Note that because multiple strings may represent
          the same underlying function (whitespace and single versus
          double quotation marks, for example), the value returned may
          not be identical to the string sent in a mutate request.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.MatchingFunction)
  ))
_sym_db.RegisterMessage(MatchingFunction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.commonB\025MatchingFunctionProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common'))
# @@protoc_insertion_point(module_scope)
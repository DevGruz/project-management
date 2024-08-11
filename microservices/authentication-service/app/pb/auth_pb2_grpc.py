# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pb import auth_pb2 as pb_dot_auth__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pb/auth_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/auth.AuthService/Login',
                request_serializer=pb_dot_auth__pb2.LoginRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.TokenResponse.FromString,
                _registered_method=True)
        self.RefreshToken = channel.unary_unary(
                '/auth.AuthService/RefreshToken',
                request_serializer=pb_dot_auth__pb2.RefreshRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.TokenResponse.FromString,
                _registered_method=True)
        self.VerifyToken = channel.unary_unary(
                '/auth.AuthService/VerifyToken',
                request_serializer=pb_dot_auth__pb2.VerifyRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.VerifyResponse.FromString,
                _registered_method=True)


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=pb_dot_auth__pb2.LoginRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.TokenResponse.SerializeToString,
            ),
            'RefreshToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshToken,
                    request_deserializer=pb_dot_auth__pb2.RefreshRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.TokenResponse.SerializeToString,
            ),
            'VerifyToken': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyToken,
                    request_deserializer=pb_dot_auth__pb2.VerifyRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.VerifyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('auth.AuthService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/auth.AuthService/Login',
            pb_dot_auth__pb2.LoginRequest.SerializeToString,
            pb_dot_auth__pb2.TokenResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RefreshToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/auth.AuthService/RefreshToken',
            pb_dot_auth__pb2.RefreshRequest.SerializeToString,
            pb_dot_auth__pb2.TokenResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def VerifyToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/auth.AuthService/VerifyToken',
            pb_dot_auth__pb2.VerifyRequest.SerializeToString,
            pb_dot_auth__pb2.VerifyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

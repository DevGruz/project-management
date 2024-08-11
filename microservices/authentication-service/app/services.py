import logging

import grpc
import pb.auth_pb2 as auth_pb2
import pb.auth_pb2_grpc as auth_pb2_grpc
import pb.user_pb2 as user_pb2
import pb.user_pb2_grpc as user_pb2_grpc
from utils import encode_jwt, decode_jwt

logger = logging.getLogger(__name__)

class AuthServicer(auth_pb2_grpc.AuthServiceServicer):
    def __init__(self):
        self.user_service_channel = grpc.insecure_channel("user-service:50051")
        self.user_service_stub = user_pb2_grpc.UserStub(self.user_service_channel)

    async def Login(
        self,
        request: auth_pb2.LoginRequest,
        context: grpc.aio.ServicerContext,
    ) -> auth_pb2.TokenResponse:
        try:
            user_authentication_request = user_pb2.UserAuthenticationRequest(
                email=request.username, password=request.password
            )
            response = self.user_service_stub.UserAuthentication(
                user_authentication_request
            )
            jwt_payload = {
                "sub": response.id,
                "email": response.email,
            }
            access_token = encode_jwt(payload=jwt_payload)
            return auth_pb2.TokenResponse(access_token=access_token)
        except grpc.RpcError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f"Error calling other service: {e.details()}")
            return auth_pb2.TokenResponse()

    # def RefreshToken(self, request, context):
    #     access_token = refresh_access_token(request.refresh_token)
    #     new_refresh_token = generate_refresh_token_from_refresh_token(request.refresh_token)
    #     return auth_pb2.TokenResponse(access_token=access_token, refresh_token=new_refresh_token, expires_in=3600)

    async def VerifyToken(self, request, context):
        try:
            payload_jwt = decode_jwt(token=str(request.token))
            return auth_pb2.VerifyResponse(valid=True, user_id=payload_jwt.get("id"), user_email=payload_jwt.get("email"))
        except Exception as ex:
            logger.debug(type(ex))
            return auth_pb2.VerifyResponse(valid=False)

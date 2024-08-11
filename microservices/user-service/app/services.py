import grpc
import pb.user_pb2 as user_pb2
import pb.user_pb2_grpc as user_pb2_grpc
import pb.auth_pb2 as auth_pb2
import pb.auth_pb2_grpc as auth_pb2_grpc
from repositories import UserRepository
from schemas import UserCreateInDBSchema, AuthUserSchema, UserSchema
from exceptions import EmailAlreadyInUseError
from utils import hash_password, verify_password


class UserServicer(user_pb2_grpc.UserServicer):
    def __init__(self):
        self.auth_service_channel = grpc.insecure_channel("auth-service:50052")
        self.auth_service_stub = auth_pb2_grpc.AuthServiceStub(self.auth_service_channel)

    async def CreateUser(
        self,
        request: user_pb2.CreateUserRequest,
        context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserResponse:
        try:
            user_create_schema = UserCreateInDBSchema.model_validate(
                request, from_attributes=True
            )
            user_create_schema.hashed_password = hash_password(request.password)
            user_model = await UserRepository.add_one(user_create_schema)
            # user_schema = UserSchema.model_validate(user_model, from_attributes=True)
            return user_pb2.UserResponse(
                id=str(user_model.id),
                email=user_model.email,
                first_name=user_model.first_name,
                last_name=user_model.last_name,
                is_active=user_model.is_active,
            )
        except EmailAlreadyInUseError as ex:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(str(ex))
            return user_pb2.UserResponse()

    async def GetUserByEmail(
        self,
        request: user_pb2.GetUserByEmailRequest,
        context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserResponse:
        user = await UserRepository.find_one_or_none(email=request.email)

        if user is None:
            return user_pb2.UserResponse()

        return user_pb2.UserResponse(
            id=str(user.id),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

    async def UpdateUser(
        self,
        request: user_pb2.UpdateUserRequest,
        context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserResponse:
        user_schema = AuthUserSchema(email=request.email, password=request.password)
        user = await UserRepository.find_one_or_none(email=user_schema.email)

        if user is None or not verify_password(user.hashed_password, request.password):
            return user_pb2.UserResponse()

        return user_pb2.UserResponse(
            id=str(user.id),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

    async def GetUserById(
        self,
        request: user_pb2.UpdateUserRequest,
        context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserResponse:
        pass

    async def UserAuthentication(
        self,
        request: user_pb2.UserAuthenticationRequest,
        context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserResponse:
        user = await UserRepository.find_one_or_none(email=request.email)

        if user is None or not verify_password(user.hashed_password, request.password):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Email or password is incorrect")
            return user_pb2.UserResponse()

        return user_pb2.UserResponse(
            id=str(user.id),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
        )

    async def GetUserFromJWT(
        self,
        request: user_pb2.TokenRequest,
        context: grpc.aio.ServicerContext,
    ) -> user_pb2.UserResponse:
        try:
            print("access_token", request.access_token)
            verify_token_request = auth_pb2.VerifyRequest(
                token=request.access_token
            )
            verify_token_response = self.auth_service_stub.VerifyToken(
                verify_token_request
            )
            print("TOKEN", verify_token_response)
            # jwt_payload = {
            #     "sub": response.id,
            #     "email": response.email,
            # }
            # access_token = encode_jwt(payload=jwt_payload)

            user_request = user_pb2.GetUserByEmailRequest(
                email=verify_token_response.user_email
            )
            user = await self.GetUserByEmail(request=user_request, context=context)

            return user_pb2.UserResponse(
                id=str(user.id),
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )
        except grpc.RpcError as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(f"Error calling other service: {e.details()}")
            return auth_pb2.TokenResponse()

import uuid
from fastapi import FastAPI, HTTPException, Depends, HTTPException, status, Cookie, Response
from pydantic import BaseModel

import grpc
import app.pb.user_pb2 as user_pb2
import app.pb.user_pb2_grpc as user_pb2_grpc
import app.pb.auth_pb2 as auth_pb2
import app.pb.auth_pb2_grpc as auth_pb2_grpc

app = FastAPI()

USER_SERVICE_URL = "user-service:50051"
AUTH_SERVICE_URL = "auth-service:50052"


class Token(BaseModel):
    access_token: str
    token_type: str


class CreateUser(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class User(BaseModel):
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str


class AuthUser(BaseModel):
    email: str
    password: str


@app.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser):
    async with grpc.aio.insecure_channel(USER_SERVICE_URL) as channel:
        try:
            stub = user_pb2_grpc.UserStub(channel)
            response = await stub.CreateUser(
                user_pb2.CreateUserRequest(
                    email=user.email,
                    password=user.password,
                    first_name=user.first_name,
                    last_name=user.last_name,
                )
            )
            return User(
                id=response.id,
                email=response.email,
                first_name=response.first_name,
                last_name=response.last_name,
            )
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="A user with this email already exists",
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
                )


@app.post("/user/auth")
async def auth_user(auth_data: AuthUser):
    async with grpc.aio.insecure_channel(USER_SERVICE_URL) as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = await stub.UserAuthentication(
            user_pb2.UserAuthenticationRequest(
                email=auth_data.email, password=auth_data.password
            )
        )
    return User(
        id=response.id,
        email=response.email,
        first_name=response.first_name,
        last_name=response.last_name,
    )


@app.post("/user/auth-test")
async def auth_user_test(auth_data: AuthUser, response: Response):
    async with grpc.aio.insecure_channel(AUTH_SERVICE_URL) as channel:
        try:
            stub = auth_pb2_grpc.AuthServiceStub(channel)
            response_login = await stub.Login(
                auth_pb2.LoginRequest(
                    username=auth_data.email, password=auth_data.password
                )
            )
            response.set_cookie(key="access_token", value=response_login.access_token)
            return {
                "access_token": response_login.access_token,
                "token_type": "Bearer",
            }
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Email or password is incorrect",
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                )


@app.get("/users/me")
async def get_current_user(access_token: str | None = Cookie(default=None)):
    async with grpc.aio.insecure_channel(USER_SERVICE_URL) as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = await stub.GetUserFromJWT(
            user_pb2.TokenRequest(
                access_token=access_token, token_type="Bearer"
            )
        )
        print("RESPONSE", response)
    return User(
        id=response.id,
        email=response.email,
        first_name=response.first_name,
        last_name=response.last_name,
    )
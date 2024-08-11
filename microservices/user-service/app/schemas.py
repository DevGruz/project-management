from typing import Annotated
import uuid
from pydantic import BaseModel, EmailStr, field_validator

UuidToStr = Annotated[str, uuid.UUID]

class UserSchema(BaseModel):
    id: uuid.UUID
    email: EmailStr
    hashed_password: str
    first_name: str
    last_name: str
    is_active: bool = True
    
    # @model_validator('id', pre=True)
    # def convert_uuid_to_str(cls, value):
    #     if isinstance(value, UUID):
    #         return str(value)
    #     return value
    
    @field_validator("id", mode="before")
    @classmethod
    def convert_uuid_to_str(cls, value):
        if isinstance(value, uuid.UUID):
            return str(value)
        return value


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    
class UserCreateInDBSchema(BaseModel):
    email: EmailStr
    hashed_password: str | None = None
    first_name: str
    last_name: str


class UserUpdateSchema(BaseModel):
    email: EmailStr | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserDeleteSchema(BaseModel):
    id: UuidToStr

class AuthUserSchema(BaseModel):
    email: EmailStr
    password: str
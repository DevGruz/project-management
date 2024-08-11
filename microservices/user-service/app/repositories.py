import uuid
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

from core.db import async_session_maker
from models import User
from schemas import UserCreateInDBSchema, UserSchema
from exceptions import EmailAlreadyInUseError



class UserRepository:
    @classmethod
    async def add_one(cls, data: UserCreateInDBSchema) -> uuid.UUID:
        async with async_session_maker() as session:
            try:
                user_dict = data.model_dump()
                
                stmt = select(User).filter_by(email=data.email)
                result = await session.execute(stmt)
                existing_user = result.scalar_one_or_none()

                if existing_user:
                    raise EmailAlreadyInUseError(data.email)
                
                stmt = insert(User).values(**user_dict).returning(User)
                result = await session.execute(stmt)
                await session.commit()
                return result.scalar_one_or_none()
            except IntegrityError as e:
                raise e
            
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(User).filter_by(**filter_by)
            result = await session.execute(query)
            # task_models = result.scalars().all()
            user_model = result.scalar_one_or_none()
            # task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return UserSchema.model_validate(user_model, from_attributes=True)

    # @classmethod
    # async def find_all(cls) -> list[STask]:
    #     async with async_session_maker() as session:
    #         query = select(TaskOrm)
    #         result = await session.execute(query)
    #         task_models = result.scalars().all()
    #         task_schemas = [STask.model_validate(task_model) for task_model in task_models]
    #         return task_schemas
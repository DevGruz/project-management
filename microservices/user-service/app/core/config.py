from typing import Literal
from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict

class PostgresSettings(BaseSettings):
    HOST: str = Field(validation_alias="POSTGRES_HOST")
    PORT: int = Field(validation_alias="POSTGRES_PORT")
    USER: str = Field(validation_alias="POSTGRES_USER")
    PASSWORD: str = Field(validation_alias="POSTGRES_PASSWORD")
    NAME: str = Field(validation_alias="POSTGRES_NAME")
    
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    
    @property
    def URL(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: str
    
    DATABASE: PostgresSettings = PostgresSettings()
    
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    
settings = Settings()
from enum import StrEnum, auto

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    LOCAL = auto()


class Settings(BaseSettings):
    environment: Environment
    llm_model: str

    model_config = SettingsConfigDict(env_file=".env")

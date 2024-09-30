from enum import StrEnum, auto

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    LOCAL = auto()
    PRODUCTION = auto()


class Settings(BaseSettings):
    environment: Environment
    llm_model: str
    openai_api_key: str

    model_config = SettingsConfigDict(env_file=".env")

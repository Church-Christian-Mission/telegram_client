from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MOD: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: Literal["DEBUG", "INFO"]

    TG_API_ID: int
    TG_API_HASH: str
    TELEGRAM_PHONE_NUMBER: int
    TELEGRAM_USERNAME: str
    TELEGRAM_PASSWORD: str

    class Config:
        env_file = '.env'


settings = Settings()

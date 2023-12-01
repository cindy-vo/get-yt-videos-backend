from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = ""
    SERVICE_PORT: int = None

    class Config:
        env_file = ".env"
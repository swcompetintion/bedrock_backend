from pydantic import BaseSettings

class Settings(BaseSettings):
    base_api_url: str ="/api/v1"

    class Config:
        env_file =".env"

settings = Settings()


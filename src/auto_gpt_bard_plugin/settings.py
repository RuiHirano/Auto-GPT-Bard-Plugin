from pydantic import BaseSettings

class Settings(BaseSettings):
    BARD_SESSION_TOKEN: str

    class Config:
        case_sensitive = True

settings = Settings()
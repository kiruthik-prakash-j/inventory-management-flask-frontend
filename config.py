from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    API_URL: str
    AUTHORIZATION_URL: str
    USER_EMAIL: EmailStr
    USER_PASSWORD: str
    TOTAL_ROWS: int
    TOTAL_COLUMNS: int
    BASE_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()
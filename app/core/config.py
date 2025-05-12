import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Dev Stream API"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "devstreamsecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEFAULT_LANGUAGE: str = "en"
    SUPPORTED_LANGUAGES = ["en", "km", "vn"]
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://fastapi:password@localhost:5432/fastapi_db")

settings = Settings()

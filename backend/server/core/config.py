import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, \
    validator


# from dotenv import load_dotenv
# load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME = "operation_helper"
    BACKEND_CORS_ORIGINS = ["http://localhost", "http://localhost:4200",
                            "http://localhost:3000", "http://localhost:8080",
                            "http://39.97.239.252:9002",
                            "http://localhost.tiangolo.com"]

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI") or "postgresql://user:admin123@0.0.0.0:5432/app"

    # token
    ACCESS_TOKEN_EXPIRE_MINUTES = 480
    # import secrets; secrets.token_urlsafe(32)
    SECRET_KEY: str = "SbwsWYOR2l_dsrcKrPfPpvUbJbPNEDUUH6ki5Dh5Woc"
    SUPER_TOKEN: str = "test token"

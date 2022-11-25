import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, \
    validator


# from dotenv import load_dotenv
# load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    PROJECT_NAME = "operation_helper"
    BACKEND_CORS_ORIGINS = ["http://localhost:3000",
                            "http://139.196.213.108:5432",
                            "http://39.97.239.252:9002",
                            "http://localhost.tiangolo.com"]

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI") or "postgresql://user:admin123@0.0.0.0:9002/app"

    # token
    ACCESS_TOKEN_EXPIRE_MINUTES = 480
    # import secrets; secrets.token_urlsafe(32)
    SECRET_KEY: str = os.getenv("SECRET_KEY") or "SbwsWYOR2l_dsrcKrPfPpvUbJbPNEDUUH6ki5Dh5Woc"
    SUPER_TOKEN: str = os.getenv("SUPER_TOKEN") or "test token"

import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, \
    validator


# from dotenv import load_dotenv
#
# load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME = "operation_helper"
    BACKEND_CORS_ORIGINS = ["http://localhost", "http://localhost:4200",
                            "http://localhost:3000", "http://localhost:8080",
                            "http://39.97.239.252:9002",
                            "http://localhost.tiangolo.com"]

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI") or "postgresql://user:admin123@0.0.0.0:5432/app"

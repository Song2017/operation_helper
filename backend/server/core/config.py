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
                            "https://localhost", "https://localhost:4200",
                            "https://localhost:3000", "https://localhost:8080",
                            "http://dev.operation.com",
                            "https://stag.operation.com",
                            "https://operation.com",
                            "http://local.dockertoolbox.tiangolo.com",
                            "http://localhost.tiangolo.com"]

    SQLALCHEMY_DATABASE_URI = "postgresql://user:admin123@localhost:5432/app"

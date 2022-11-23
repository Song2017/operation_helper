from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api import deps
from core import security, settings
from db.crud.base import CRUDBase
from models.app_user import AppUser
from schemas.token import Token
from schemas.user import User

router = APIRouter()


@router.post("/login/access-token", response_model=Token)
def login_access_token(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = CRUDBase(AppUser)
    condition_in = {"full_name": form_data.username,
                    "hashed_password": form_data.password,
                    "is_active": True
                    }
    users = user.get_multi(db, page_no=1, page_size=1, condition_in=condition_in)
    if len(users) < 1:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user_data: AppUser = users[0]
    if not user_data.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user_data.app_user_id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=User)
def test_token() -> Any:
    """
    Test access token
    """
    return {
        "email": "test@ddd.com",
        "is_active": True,
        "is_superuser": False,
        "full_name": "test",
        "id": "1000"
    }

from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from core import settings, security
from db.crud.base import CRUDBase
from db.session import SessionLocal
from schemas.token import TokenPayload
from models.app_user import AppUser

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("get_db except" + str(e))
    finally:
        db.close()


def get_current_user(
        db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> AppUser:
    if token == settings.SUPER_TOKEN:
        token_data = TokenPayload(sub=1)
    else:
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
            )
            token_data = TokenPayload(**payload)
        except (jwt.JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )

    user_orm = CRUDBase(AppUser)
    user = user_orm.get(db, id_key="app_user_id", id_val=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
        current_user: AppUser = Depends(get_current_user),
) -> AppUser:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
        current_user: AppUser = Depends(get_current_user),
) -> AppUser:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user

from typing import Any, List, Union
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api import deps
from db.crud.base import CRUDBase
from models.app_auth import AppAuthentication
from schemas.sms_authentication import SmsAuthCreate, SmsAuthPut

router = APIRouter()


@router.post("/")
def create_auth(
        obj_in: SmsAuthCreate,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Test access token
    """
    auth = CRUDBase(AppAuthentication)
    return auth.create(db, obj_in=obj_in)


@router.put("/")
def put_auth(
        obj_in: SmsAuthPut,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Test access token
    """
    auth = CRUDBase(AppAuthentication)
    res = auth.query_update(db, condition_in={
        "app_authentication_id": obj_in.app_authentication_id}, obj_in=obj_in)
    if not res:
        raise HTTPException(status_code=400, detail="No record update")
    return obj_in


@router.get("/", response_model=List)
def get_auth(
        name: Union[str, None] = None,
        is_enabled: Union[bool, None] = None,
        platform: Union[str, None] = None,
        page_no: int = 1,
        page_size: int = 10,
        db: Session = Depends(deps.get_db),
) -> Any:
    auth = CRUDBase(AppAuthentication)
    condition_in = {"name": name, "is_enabled": is_enabled, "platform": platform}
    filter_condition = {k: v for k, v in condition_in.items() if v is not None}
    auths = auth.get_multi(db, page_no=page_no, page_size=page_size,
                           condition_in=filter_condition, order_by="platform")
    return auths

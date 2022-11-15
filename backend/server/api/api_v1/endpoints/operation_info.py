from typing import Any, List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api import deps
from db.crud.base import CRUDBase
from models.app_operation_info import AppOperationInfo
from schemas.operation_info import OperationInfoCreate, OperationInfo, OperationInfoPut

router = APIRouter()


@router.post("/")
def create_info(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: OperationInfoCreate,
) -> Any:
    auth = CRUDBase(AppOperationInfo)
    return auth.create(db, obj_in=obj_in)


@router.put("/")
def put_auth(
        obj_in: OperationInfoPut,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Test access token
    """
    auth = CRUDBase(AppOperationInfo)
    res = auth.query_update(db, condition_in={
        "app_operation_info_id": obj_in.app_operation_info_id}, obj_in=obj_in)
    if not res:
        raise HTTPException(status_code=400, detail="No record update")
    return obj_in


@router.get("/", response_model=List[OperationInfo])
def get_info(
        *,
        name: Union[str, None] = None,
        is_consumed: Union[bool, None] = None,
        page_no: int = 1,
        page_size: int = 10,
        db: Session = Depends(deps.get_db),
) -> Any:
    operation = CRUDBase(AppOperationInfo)
    condition_in = {"name": name, "is_consumed": is_consumed}
    filter_condition = {k: v for k, v in condition_in.items() if v is not None}
    info = operation.get_multi(db, page_no=page_no, page_size=page_size,
                               condition_in=filter_condition, order_by="name")
    return info

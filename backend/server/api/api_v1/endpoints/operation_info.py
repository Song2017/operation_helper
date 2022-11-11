from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import deps
from schemas.operation_info import OperationInfoCreate, OperationInfo

router = APIRouter()


@router.post("/", response_model=OperationInfo)
def create_info(
        *,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Test access token
    """
    
    return {
        "name": "name",
        "description": "True",
        "content": "",
    }

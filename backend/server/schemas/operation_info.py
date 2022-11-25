from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OperationInfoBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    content: str


class OperationInfoCreate(OperationInfoBase):
    ...


class OperationInfoPut(OperationInfoBase):
    app_operation_info_id: Optional[int]
    is_consumed: Optional[bool]
    content: Optional[str]


class OperationInfo(OperationInfoBase):
    """
    "create_by": null,
    "create_time": "2022-11-15T01:30:17.013000+00:00",
    "is_consumed": false,
    "description": null,
    "app_operation_info_id": 1,
    "modify_by": null,
    "modify_time": "2022-11-15T01:30:17.013000+00:00",
    "content": "test",
    "name": "test"
    """
    app_operation_info_id: Optional[int]
    is_consumed: Optional[bool]
    create_time: Optional[datetime]
    modify_time: Optional[datetime]
    create_by: Optional[str]
    modify_by: Optional[str]

    class Config:
        orm_mode = True

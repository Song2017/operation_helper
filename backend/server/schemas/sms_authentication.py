from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SmsAuthBase(BaseModel):
    type: Optional[str]
    platform: Optional[str]
    token: str


class SmsAuthCreate(SmsAuthBase):
    is_enabled: Optional[bool]


class SmsAuthPut(SmsAuthCreate):
    app_authentication_id: int


class SmsAuthOrm(SmsAuthBase):
    app_authentication_id: Optional[int]
    is_enabled: Optional[bool]
    create_time: Optional[datetime]
    modify_time: Optional[datetime]
    create_by: Optional[str]
    modify_by: Optional[str]

    class Config:
        orm_mode = True

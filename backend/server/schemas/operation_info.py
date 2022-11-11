from typing import Optional

from pydantic import BaseModel


class OperationInfoBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    content: str


class OperationInfoCreate(OperationInfoBase):
    ...


class OperationInfo(OperationInfoBase):
    id: Optional[str]

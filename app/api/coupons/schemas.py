from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class CouponsType(str, Enum):
    VALUE = "value"
    PERCENTAGE = "percentage"


class CouponsSchema(BaseModel):
    code: str
    expire_at: datetime
    limit: int
    type: CouponsType
    value: float


class ShowCouponsSchema(CouponsSchema):
    id: int

    class Config:
        orm_mode = True


""" --> retornando dois atributos para a função update """


class UpdateCoupons(BaseModel):
    expire_at: datetime
    limit: int

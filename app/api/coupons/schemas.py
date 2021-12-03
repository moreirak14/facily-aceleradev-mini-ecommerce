from datetime import datetime
from pydantic import BaseModel


class CouponsSchema(BaseModel):
    code: str
    expire_at: datetime
    limit: int
    type: str
    value: float


class ShowCouponsSchema(CouponsSchema):
    id: int

    class Config:
        orm_mode = True

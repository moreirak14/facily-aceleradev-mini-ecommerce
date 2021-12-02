from pydantic import BaseModel


class PaymentMethodsSchema(BaseModel):
    name: str
    enabled: bool


class ShowPaymentMethodsSchema(PaymentMethodsSchema):
    id: int
    
    class Config:
        orm_mode = True
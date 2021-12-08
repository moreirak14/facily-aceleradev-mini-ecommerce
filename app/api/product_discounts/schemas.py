from enum import Enum
from pydantic import BaseModel
from app.api.product.schemas import ShowProductSchema
from app.api.payment_methods.schemas import ShowPaymentMethodsSchema


class DiscountMode(str, Enum):
    VALUE = "value"
    PERCENTAGE = "percentage"


class ProductDiscountsSchema(BaseModel):
    mode: DiscountMode
    value: float
    product_id: int
    payment_methods_id: int


class ShowProductDiscountsSchema(ProductDiscountsSchema):
    id: int
    product = ShowProductSchema
    payment_methods = ShowPaymentMethodsSchema

    class Config:
        orm_mode = True

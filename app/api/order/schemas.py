from typing import List, Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class OrderStatus(str, Enum):
    ORDER_CANCELLED = "order_cancelled"
    ORDER_COMPLETED = "order_completed"
    ORDER_RECEIVED = "order_received"
    ORDER_PLACED = "order_placed"
    ORDER_PAID = "order_paid"
    ORDER_SHIPPED = "order_shipped"


class ProductSchema(BaseModel):
    id: int
    quantity: int


class OrderSchema(BaseModel):
    address_id: int
    payment_form_id: int
    coupon_code: Optional[str]
    product: List[ProductSchema]


class OrderStatusSchema(BaseModel):
    status: OrderStatus


class OrderSchema(BaseModel):
    number: str = ""
    status: str = ""
    customer_id: int = 0
    created_at: datetime = datetime.now()
    address_id: int = 0
    total_value: float = 0
    payment_form_id: int = 0
    total_discount: float = 0

    class Config:
        orm_mode = True


class OrderStatusSchema:
    def __init__(
        self, order_id: int, status: OrderStatus, created_at: datetime
    ) -> None:
        self.order_id = order_id
        self.status = status
        self.created_at = created_at


class OrderProductSchema:
    def __init__(self, order_id: int, product_id: int, quantity: int) -> None:
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

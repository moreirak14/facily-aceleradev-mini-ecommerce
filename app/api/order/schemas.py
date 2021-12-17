from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from app.api.product.schemas import ShowProductSchemas


class OrderProducts_sum_Schema(BaseModel):
    product_id: int
    quantity: int


class OrderSchema(BaseModel):
    number: str = None
    status = 'ORDER PLACED'
    #customer_id = Column(Integer, ForeignKey("customers.id"))
    customer_id: int = None
    created_at: datetime = None
    #address_id = Column(Integer, ForeignKey("addresses.id"))
    address_id: int = None
    value: float = None  # valor total
    payment_form_id: int = None
    total_discount: float = None


class creat_OrderProductSchema(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class creat_OrderSchema(BaseModel):
    customer_id: int
    address_id: int
    payment_form_id: int
    list_products: list[OrderProducts_sum_Schema]


class OrderStatus(str, Enum):
    ORDER_CANCELLED = 'order_cancelled'
    ORDER_COMPLETED = 'order_completed'
    ORDER_RECEIVED = 'order_received'
    ORDER_PLACED = 'order_placed'
    ORDER_PAID = 'order_paid'
    ORDER_SHIPPED = 'order_shipped'


class OrderStatusSchema:
    def __init__(self, order_id: int, status: OrderStatus, created_at: datetime):
        self.order_id = order_id
        self.status = status
        self.created_at = created_at

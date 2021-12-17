from fastapi import APIRouter, status, Depends
from app.api.order.schemas import OrderSchema, OrderStatus, creat_OrderSchema
from app.models.models import User
from app.services.auth_service import only_admin, only_customer, get_user
from app.services.order_service import OrderService

router = APIRouter(dependencies=[Depends(only_admin)])


@router.post('/')
def create(input_order_schema: creat_OrderSchema, service: OrderService = Depends()):
    return service.creat_order(input_order_schema)


@router.put('/{id}')
def update(id: int, order_status: OrderStatus, service: OrderService = Depends()):
    service.update(id, order_status)

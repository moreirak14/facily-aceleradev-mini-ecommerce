from fastapi import Depends
from app.models.models import Ordem_status, Order, OrderProducts
from app.repositories.order_repository import OrderRepository, Ordem_status_Repository, OrderProducts_Repository
from app.repositories.produc_repository import ProductRepository
from app.services.product_discount_service import ProducDiscountService
from app.services.address_service import AddressService
from app.api.order.schemas import OrderStatusSchema, OrderStatus, OrderProducts_sum_Schema, creat_OrderProductSchema, creat_OrderSchema
from datetime import datetime
#from fastapi.exceptions import HTTPException
#from app.common.exceptions import CouponCodeAlreadyExistsException
import random


class OrderSchema_Dto:
    def __init__(self, number, status, customer_id, created_at, address_id,
                 value, payment_form_id, total_discount):
        self.number = number
        self.status = status
        self.customer_id = customer_id
        self.created_at = created_at
        self.address_id = address_id
        self.value = value
        self.payment_form_id = payment_form_id
        self.total_discount = total_discount


class OrderService:
    def __init__(self, orderRepository: OrderRepository = Depends(),
                 ordem_status_Repository: Ordem_status_Repository = Depends(),
                 orderProducts_Repository: OrderProducts_Repository = Depends(),
                 productRepository: ProductRepository = Depends(),
                 producDiscountService: ProducDiscountService = Depends(),
                 addressService: AddressService = Depends()):
        self.orderRepository = orderRepository
        self.ordem_status_Repository = ordem_status_Repository
        self.orderProducts_Repository = orderProducts_Repository
        self.productRepository = productRepository
        self.producDiscountService = producDiscountService
        self.addressService = addressService

    def order_number(self):
        n_order = random.sample(range(10000000), k=1)
        return n_order[0]

    def criar_status(self, order_id, current_status: OrderStatus):
        orderStatus = OrderStatusSchema(order_id=order_id,
                                        status=current_status,
                                        created_at=datetime.now())
        self.ordem_status_Repository.create(
            Ordem_status(**orderStatus.__dict__))

    def update(self, id: int, order_status: OrderStatus):
        self.orderRepository.update(id, {'status': order_status})
        return self.criar_status(id, order_status)

    # O status inicial da ordem deverá ser ORDER PLACED
    def init_status_order(self, id_order):
        return self.criar_status(id_order, OrderStatus.ORDER_PLACED)

    # def next_status_order(self,id):
    #     pass

    # def get_listProductsOrder(self,order_id):
    #     return self.orderProducts_Repository.get_by_order_id(order_id)

    def generate_total_value(self, list_products):
        return sum(list(map(lambda x: x.quantity *
                            self.productRepository.get_by_id(x.product_id).price, list_products)))

    def generate_total_desconto(self, list_products, payment_form_id):
        return self.producDiscountService.get_productDiscounts(list_products, payment_form_id)

    def create_order_products(self, id, list_products: list[OrderProducts_sum_Schema]):
        return list(map(lambda x:
                        self.orderProducts_Repository.create(OrderProducts
                                                             (**creat_OrderProductSchema(
                                                                 order_id=id,
                                                                 product_id=x.product_id,
                                                                 quantity=x.quantity
                                                             ).dict())), list_products))

    def creat_order(self, input_order_schema: creat_OrderSchema):
        order_schema = OrderSchema_Dto(
            number=self.order_number(),
            status=OrderStatus.ORDER_PLACED,
            customer_id=3,
            created_at=datetime.now(),
            address_id=self.addressService.validate_address(
                3, input_order_schema.address_id),
            value=self.generate_total_value(input_order_schema.list_products),
            payment_form_id=input_order_schema.payment_form_id,
            total_discount=self.generate_total_desconto(input_order_schema.list_products,
                                                        input_order_schema.payment_form_id)
        )
        order = self.orderRepository.create(Order(**order_schema.__dict__))
        self.criar_status(order.id, OrderStatus.ORDER_PLACED)
        self.create_order_products(order.id, input_order_schema.list_products)

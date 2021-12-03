from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import PaymentDiscountRepository
from app.api.product_discounts.schemas import ProductDiscountsSchema
from app.models.models import PaymentMethod


class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: PaymentDiscountRepository = Depends()):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, discount: ProductDiscountsSchema):
        payment_method = self.payment_method_repository.get_by_id(discount.product_id)
        if payment_method.enabled():
            self.payment_method_repository.create(PaymentMethod(**payment_method.dict()))
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Item not allowed!!!")

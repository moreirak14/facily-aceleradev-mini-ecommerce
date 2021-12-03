from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import PaymentDiscountRepository
from app.api.product_discounts.schemas import ProductDiscountsSchema, DiscountMode
from app.models.models import PaymentDiscount


class ProductDiscountService:
    def __init__(self, payment_method_repository: PaymentMethodRepository = Depends(),
                 product_discount_repository: PaymentDiscountRepository = Depends(),):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository


    def create_discount(self, discount: ProductDiscountsSchema):
        payment_method = self.payment_method_repository.get_by_id(discount.payment_methods_id)
        mode_method = self.payment_method_repository.get_by_id(discount.mode)

        if payment_method.enabled:
            self.product_discount_repository.create(PaymentDiscount(**discount.dict()))
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                                detail=f"{payment_method.name} - item not allowed!!!")

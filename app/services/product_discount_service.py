from fastapi import Depends
from app.repositories.payment_method_repository import PaymentMethodRepository
from app.repositories.product_discount_repository import PaymentDiscountRepository
from app.api.product_discounts.schemas import ProductDiscountsSchema
from app.models.models import PaymentDiscount
from app.common.exceptions import (
    PaymentMethodsNotAvailableException,
    PaymentMethodDiscountAlreadyExistsException,
)


class ProductDiscountService:
    def __init__(
        self,
        payment_method_repository: PaymentMethodRepository = Depends(),
        product_discount_repository: PaymentDiscountRepository = Depends(),
    ):
        self.payment_method_repository = payment_method_repository
        self.product_discount_repository = product_discount_repository

    def create_discount(self, discount: ProductDiscountsSchema):
        """--> percorre o model de payment_method_repository(PaymentMethod) de cada id retornando
        o valor booleano de cada metodo de pagamento."""
        payment_method = self.payment_method_repository.get_by_id(
            discount.payment_methods_id
        )

        """ --> se o resultado booleano de payment_method não for enabled (1),
        retorna exception. """
        if not payment_method or not payment_method.enabled:
            raise PaymentMethodsNotAvailableException()

        """ --> percorre o model de product_discount_repository(PaymentDiscount) filtrando 
        product_id e payment_method_id. """
        mode_method = self.product_discount_repository.filter(
            {
                "product_id": discount.product_id,
                "payment_methods_id": discount.payment_methods_id,
            }
        )

        """ --> se já existir product_id e payment_method_id atribuido em algum
        metodo de desconto, retorna exception. """
        if mode_method:
            raise PaymentMethodDiscountAlreadyExistsException()

        return self.product_discount_repository.create(PaymentDiscount(**discount.dict()))

from fastapi import APIRouter, status, Depends, HTTPException
from .schemas import ProductDiscountsSchema
from app.repositories.product_discount_repository import PaymentDiscountRepository
from app.services.product_discount_service import ProductDiscountService
from app.common.exceptions import (
    PaymentMethodsNotAvailableException,
    PaymentMethodDiscountAlreadyExistsException,
)
from app.services.auth_service import only_admin


router = APIRouter(
    dependencies=[Depends(only_admin)]
)  # --> atribuindo autenticação para produtos


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    product_discounts: ProductDiscountsSchema,
    services: ProductDiscountService = Depends(),
):
    try:
        return services.create_discount(product_discounts)
    except PaymentMethodsNotAvailableException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)
    except PaymentMethodDiscountAlreadyExistsException as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/")
def index(repository: PaymentDiscountRepository = Depends()):
    return repository.get_all()


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete(id: int, repository: PaymentDiscountRepository = Depends()):
    repository.remove(id)

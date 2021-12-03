from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from .schemas import ProductDiscountsSchema, ShowProductDiscountsSchema
from app.models.models import PaymentDiscount
from app.repositories.product_discount_repository import PaymentDiscountRepository
from app.services.product_discount_service import ProductDiscountService


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discounts: ProductDiscountsSchema, 
           services: ProductDiscountService = Depends()):
    services.create_discount(product_discounts)


@router.get('/', response_model=List[ShowProductDiscountsSchema])
def index(repository: PaymentDiscountRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, product_discounts: ProductDiscountsSchema, 
           repository: PaymentDiscountRepository = Depends()):
    repository.update(id, product_discounts.dict())


@router.get('/{id}', response_model=ShowProductDiscountsSchema)
def show(id: int, repository: PaymentDiscountRepository = Depends()):
    return repository.get_by_id(id)

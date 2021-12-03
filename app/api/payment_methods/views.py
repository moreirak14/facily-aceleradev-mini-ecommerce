from typing import List
from fastapi import APIRouter, status
from app.models.models import PaymentMethod
from .schemas import PaymentMethodsSchema, ShowPaymentMethodsSchema
from fastapi.params import Depends
from app.repositories.payment_method_repository import PaymentMethodRepository


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodsSchema, 
           repository: PaymentMethodRepository = Depends()):
    repository.create(PaymentMethod(**payment_method.dict()))


@router.get('/', response_model=List[ShowPaymentMethodsSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, payment_method: PaymentMethodsSchema, 
           repository: PaymentMethodRepository = Depends()):
    repository.update(id, payment_method.dict())


@router.get('/{id}', response_model=ShowPaymentMethodsSchema)
def show(id: int, repository: PaymentMethodRepository = Depends()):
    return repository.get_by_id(id)

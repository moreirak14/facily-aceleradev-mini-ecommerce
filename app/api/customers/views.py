from typing import List
from fastapi import APIRouter, status
from app.repositories.customers_repository import CustomersRepository
from fastapi.params import Depends
from app.api.customers.schemas import CustomersSchema, ShowCustomersSchema
from app.models.models import Customer
from app.services.auth_service import only_admin


router = APIRouter(dependencies=[Depends(only_admin)]) # --> atribuindo autenticação para produtos


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(customers: CustomersSchema, 
           repository: CustomersRepository = Depends()):
    repository.create(Customer(**customers.dict()))


@router.get('/', response_model=List[ShowCustomersSchema])
def index(repository: CustomersRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, customers: CustomersSchema, 
           repository: CustomersRepository = Depends()):
    repository.update(id, customers.dict())


@router.get('/{id}', response_model=ShowCustomersSchema)
def show(id: int, repository: CustomersRepository = Depends()):
    return repository.get_by_id(id)

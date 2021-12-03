from typing import List
from fastapi import APIRouter, status
from .schemas import AddressesSchema, ShowAddressesSchema
from fastapi.params import Depends
from app.models.models import Address
from app.repositories.addresses_repository import AddressesRepository


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(address: AddressesSchema, repository: AddressesRepository = Depends()):
    repository.create(Address(**address.dict()))


@router.get('/', response_model=List[ShowAddressesSchema])
def index(repository: AddressesRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, address: AddressesSchema, repository: AddressesRepository = Depends()):
    repository.update(id, address.dict())


@router.get('/{id}', response_model=ShowAddressesSchema)
def show(id: int, repository: AddressesRepository = Depends()):
    return repository.get_by_id(id)

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from .schemas import AddressesSchema, ShowAddressesSchema
from app.models.models import Address
from app.repositories.addresses_repository import AddressesRepository
from app.services.addresses_service import AddressesService
from app.common.exceptions import CustomersInvalidNone


router = APIRouter()


@router.post("/", response_model=ShowAddressesSchema, status_code=status.HTTP_201_CREATED)
def create(address: AddressesSchema, services: AddressesService = Depends()):
    try:
        return services.create_address(address)
    except CustomersInvalidNone as msg:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=msg.message
        )


@router.get("/", response_model=List[ShowAddressesSchema])
def index(repository: AddressesRepository = Depends()):
    return repository.get_all()


@router.put("/{id}", response_model=ShowAddressesSchema, status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int, address: AddressesSchema, repository: AddressesRepository = Depends()
):
    return repository.update(id, address.dict())


@router.get("/{id}", response_model=ShowAddressesSchema)
def show(id: int, repository: AddressesRepository = Depends()):
    return repository.get_by_id(id)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def remove(id: int, repository: AddressesRepository = Depends()):
    return repository.remove(id)

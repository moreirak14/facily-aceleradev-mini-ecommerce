from typing import List
from fastapi import APIRouter, status, HTTPException
from app.repositories.customers_repository import CustomersRepository
from app.services.customer_service import CustomerService
from fastapi.params import Depends
from app.api.customers.schemas import (
    CustomersSchema,
    ShowCustomersSchema,
    UpdateCustomersSchema,
)
from app.common.exceptions import EmailAdminUserAuthentication


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(customers: CustomersSchema, services: CustomerService = Depends()):
    try:
        return services.create_customer(customers)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg.message)


@router.get("/", response_model=List[ShowCustomersSchema])
def index(repository: CustomersRepository = Depends()):
    return repository.get_all()


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    customers: UpdateCustomersSchema,
    services: CustomerService = Depends()):
    return services.update_customer(id, customers)


@router.get("/{id}", response_model=ShowCustomersSchema)
def show(id: int, repository: CustomersRepository = Depends()):
    return repository.get_by_id(id)

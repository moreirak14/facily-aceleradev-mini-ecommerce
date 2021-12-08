from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from app.repositories.cupons_repository import CouponsRepository
from app.api.coupons.schemas import CouponsSchema, ShowCouponsSchema, UpdateCoupons
from app.services.coupons_service import CouponsService
from app.common.exceptions import CouponsCodeAlreadyExistsException
from app.services.auth_service import only_admin


router = APIRouter(
    dependencies=[Depends(only_admin)]
)  # --> atribuindo autenticação para produtos


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(coupons: CouponsSchema, services: CouponsService = Depends()):
    try:
        services.create_coupons(coupons)
    except CouponsCodeAlreadyExistsException as msg:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=msg.message
        )


@router.get("/", response_model=List[ShowCouponsSchema])
def index(repository: CouponsRepository = Depends()):
    return repository.get_all()


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, coupons: UpdateCoupons, repository: CouponsRepository = Depends()):
    repository.update(id, coupons.dict())


@router.get("/{id}", response_model=ShowCouponsSchema)
def show(id: int, repository: CouponsRepository = Depends()):
    return repository.get_by_id(id)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def remove(id: int, repository: CouponsRepository = Depends()):
    repository.remove(id)

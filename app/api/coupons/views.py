from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from app.repositories.cupons_repository import CouponsRepository
from app.api.coupons.schemas import CouponsSchema, ShowCouponsSchema
from app.models.models import Coupons


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(coupons: CouponsSchema, 
           repository: CouponsRepository = Depends()):
    repository.create(Coupons(**coupons.dict()))


@router.get('/', response_model=List[ShowCouponsSchema])
def index(repository: CouponsRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, coupons: CouponsSchema, 
           repository: CouponsRepository = Depends()):
    repository.update(id, coupons.dict())


@router.get('/{id}', response_model=ShowCouponsSchema)
def show(id: int, repository: CouponsRepository = Depends()):
    return repository.get_by_id(id)

from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from .schemas import ProductSchema, ShowProductSchema
from app.models.models import Product
from app.repositories.product_repository import ProductRepository


router = APIRouter()

# --> estrutura padrão para todas as rotas que chamar a router
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository: ProductRepository = Depends()):
    repository.create(Product(**product.dict()))


@router.get('/', response_model=List[ShowProductSchema])
def index(repository: ProductRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, product: ProductSchema, 
           repository: ProductRepository = Depends()):
    repository.update(id, product.dict())


@router.get('/{id}', response_model=ShowProductSchema)
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id)

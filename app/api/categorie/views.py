from typing import List
from fastapi import APIRouter, status
from .schemas import CategorieSchema, ShowCategorieSchema
from fastapi.params import Depends
from app.models.models import Categorie
from app.repositories.categorie_repository import CategorieRepository
from app.services.auth_service import only_admin


router = APIRouter(dependencies=[Depends(only_admin)]) # --> atribuindo autenticação para produtos


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(categorie: CategorieSchema, repository: CategorieRepository = Depends()):
    repository.create(Categorie(**categorie.dict()))


@router.get('/', response_model=List[ShowCategorieSchema])
def index(repository: CategorieRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, categorie: CategorieSchema, repository: CategorieRepository = Depends()):
    repository.update(id, categorie.dict())


@router.get('/{id}', response_model=ShowCategorieSchema)
def show(id: int, repository: CategorieRepository = Depends()):
    return repository.get_by_id(id)

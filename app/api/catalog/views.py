from fastapi import APIRouter, Depends
from app.repositories.product_repository import ProductRepository
from .schemas import CatalogFilter, ShowProductSchema
from fastapi_pagination import Page


router = APIRouter()


@router.get("/", response_model=Page[ShowProductSchema])
def index(
    filter: CatalogFilter = Depends(), product_repository: ProductRepository = Depends()
):
    pass

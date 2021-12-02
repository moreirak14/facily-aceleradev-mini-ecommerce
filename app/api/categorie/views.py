from typing import List
from fastapi import APIRouter, status
from .schemas import CategorieSchema, ShowCategorieSchema
from sqlalchemy.orm import Session
from fastapi.params import Depends
from app.db.db import get_db
from app.models.models import Categorie


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(categorie: CategorieSchema, db: Session = Depends(get_db)):
    db.add(Categorie(**categorie.dict()))
    db.commit()


@router.get('/', response_model=List[ShowCategorieSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Categorie).all()


@router.put('/{id}')
def update(id: int, categorie: CategorieSchema, db: Session = Depends(get_db)):
    query = db.query(Categorie).filter_by(id=id)
    query.update(categorie.dict())
    db.commit()


@router.get('/{id}', response_model=ShowCategorieSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Categorie).filter_by(id=id).first()

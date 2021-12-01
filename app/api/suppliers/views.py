from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from app.models.models import Supplier
from .schemas import ShowSuppliersSchema, SuppliersSchema
from app.db.db import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SuppliersSchema, db: Session = Depends(get_db)):
    db.add(Supplier(**supplier.dict()))
    db.commit()


@router.get('/', response_model=List[ShowSuppliersSchema])
def index(db: Session = Depends(get_db)):
    return db.query(Supplier).all()


@router.put('/{id}')
def update(id: int, supplier: SuppliersSchema, db: Session = Depends(get_db)):
    query = db.query(Supplier).filter_by(id=id)
    query.update(supplier.dict())
    db.commit()


@router.get('/{id}', response_model=ShowSuppliersSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(Supplier).filter_by(id=id).first()

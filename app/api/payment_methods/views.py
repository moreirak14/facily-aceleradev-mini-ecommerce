from typing import List
from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from app.models.models import PaymentMethod, Product
from .schemas import PaymentMethodsSchema, ShowPaymentMethodsSchema
from fastapi.params import Depends
from app.db.db import get_db


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodsSchema, 
           db: Session = Depends(get_db)):
    db.add(PaymentMethod(**payment_method.dict()))
    db.commit()


@router.get('/', response_model=List[ShowPaymentMethodsSchema])
def index(db: Session = Depends(get_db)):
    return db.query(PaymentMethod).all()


@router.put('/{id}')
def update(id: int, payment_method: PaymentMethodsSchema, 
           db: Session = Depends(get_db)):
    query = db.query(PaymentMethod).filter_by(id=id)
    query.update(payment_method.dict())
    db.commit()


@router.get('/{id}', response_model=ShowPaymentMethodsSchema)
def show(id: int, db: Session = Depends(get_db)):
    return db.query(PaymentMethod).filter_by(id=id).first()

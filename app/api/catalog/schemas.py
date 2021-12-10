from typing import List
from fastapi import Query
from pydantic import BaseModel


class CatalogFilter:
    def __init__(
        self,
        description: str = Query(None),
        categorie_id: int = Query(None),
        supplier_id: int = Query(None),
        min_price: float = Query(None),
        max_price: float = Query(None),
    ):
        self.description = description
        self.categorie_id = categorie_id
        self.supplier_id = supplier_id
        self.min_price = min_price
        self.max_price = max_price


class ShowCategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ShowSupplierSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ShowPaymentMethodSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ShowDiscountSchema(BaseModel):
    mode: str
    value: float
    payment_methods: ShowPaymentMethodSchema

    class Config:
        orm_mode = True


class ShowProductSchema(BaseModel):
    id: int
    description: str
    price: float
    categorie: ShowCategorySchema
    supplier: ShowSupplierSchema
    discounts: List[ShowDiscountSchema]

    class Config:
        orm_mode = True

from app.api.catalog.schemas import CatalogFilter
from .base_repository import BaseRepository
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from app.db.db import get_db
from app.models.models import Categorie, Product, PaymentDiscount
from fastapi_pagination.ext.sqlalchemy import paginate


class ProductRepository(BaseRepository):  # --> pega o crud de base_repository
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Product)

    def get_for_catalog(self, filter: CatalogFilter):
        query = self.query()
        queryset = [Product.visible == True]
        if filter.categorie_id:
            queryset.append(Product.categorie_id == filter.categorie_id)
            query = query.join(Categorie)
        if filter.supplier_id:
            queryset.append(Product.supplier_id == filter.supplier_id)
        if filter.min_price:
            queryset.append(Product.price >= filter.min_price)
        if filter.max_price:
            queryset.append(Product.price <= filter.max_price)
        if filter.description:
            queryset.append(Product.description.like(f"%{filter.description}%"))

        query = query.filter(*queryset).options(
            joinedload(Product.categorie),
            joinedload(Product.supplier),
            joinedload(Product.discounts).subqueryload(PaymentDiscount.payment_methods),
        )
        return paginate(query)

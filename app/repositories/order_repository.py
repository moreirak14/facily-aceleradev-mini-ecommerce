from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.models import Ordem_status, Order, OrderProducts
from .base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Order)


class Ordem_status_Repository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, Ordem_status)


class OrderProducts_Repository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, OrderProducts)

    def get_by_order_id(self, order_id: int):
        return self.session.query(self.model).filter_by(order_id=order_id).all()

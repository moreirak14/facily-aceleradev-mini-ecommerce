from app.db.db import Session, get_db
from app.models.models import OrderStatus
from app.repositories.base_repository import BaseRepository
from fastapi import Depends


class OrderStatusRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(session, OrderStatus)

    def get_by_order_id(self, order_id: int):
        return self.session.query(self.model).fiter_by(order_id=order_id).first()

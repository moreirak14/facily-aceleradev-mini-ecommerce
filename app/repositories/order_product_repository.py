from app.db.db import Session, get_db
from app.models.models import OrderProducts
from app.repositories.base_repository import BaseRepository
from fastapi import Depends


class OrderProductRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)) -> None:
        super().__init__(session, OrderProducts)

    def get_by_order_id(self, order_id: int):
        return self.session.query(self.model).fiter_by(order_id=order_id).first()

    def get_by_product_id(self, product_id: int):
        return self.session.query(self.model).fiter_by(product_id=product_id).first()

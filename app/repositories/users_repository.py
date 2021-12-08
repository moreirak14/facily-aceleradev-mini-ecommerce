from .base_repository import BaseRepository
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.db import get_db
from app.models.models import User


class UsersRepository(BaseRepository):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(session, User)

    def find_by_email(self, email):
        return self.session.query(self.model).filter_by(email=email).first()

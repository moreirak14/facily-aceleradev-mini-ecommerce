from fastapi import APIRouter, Depends
from app.repositories.users_repository import UsersRepository
from .schemas import UsersSchema
from app.models.models import User
import bcrypt


router = APIRouter()


@router.post('/')
def create(user: UsersSchema, repository: UsersRepository = Depends()):
    user.password = bcrypt.hashpw(user.password.encode('utf8'), 
                    bcrypt.gensalt())
    repository.create(User(**user.dict()))

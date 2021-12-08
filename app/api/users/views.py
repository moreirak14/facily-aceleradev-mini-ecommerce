from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UsersSchema
from app.models.models import User
from app.services.users_admin_service import UsersAdminService
from app.common.exceptions import EmailAdminUserAuthentication
import bcrypt


router = APIRouter()


@router.post("/")
def create(user: UsersSchema, services: UsersAdminService = Depends()):
    user.password = bcrypt.hashpw(user.password.encode("utf8"), bcrypt.gensalt())
    try:
        services.create_user(user)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)

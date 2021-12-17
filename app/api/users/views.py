from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import UsersSchema
from app.services.users_admin_service import UsersAdminService
from app.common.exceptions import EmailAdminUserAuthentication


router = APIRouter()


@router.post("/")
def create(user: UsersSchema, services: UsersAdminService = Depends()):
    try:
        services.create_admin_user(user)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)

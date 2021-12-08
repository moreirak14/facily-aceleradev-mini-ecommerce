from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app.repositories.users_repository import UsersRepository
from .schemas import AdminUsersSchema, ShowAdminUsersSchema
from app.api.auth.schemas import ShowAdminUserAuthenticationSchema
from app.services.auth_service import only_admin
from app.services.users_admin_service import UsersAdminService
from app.common.exceptions import EmailAdminUserAuthentication
import bcrypt


router = APIRouter(
    dependencies=[Depends(only_admin)]
)  # --> atribuindo autenticação para produtos


@router.post("/")
def create(admin_user: AdminUsersSchema, services: UsersAdminService = Depends()):
    admin_user.password = bcrypt.hashpw(
        admin_user.password.encode("utf8"), bcrypt.gensalt()
    )
    try:
        services.create_user(admin_user)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/", response_model=List[ShowAdminUserAuthenticationSchema])
def index(repository: UsersRepository = Depends()):
    return repository.get_all()


@router.put("/{id}")
def update(
    id: int, admin_user: AdminUsersSchema, services: UsersAdminService = Depends()
):
    admin_user.password = bcrypt.hashpw(
        admin_user.password.encode("utf8"), bcrypt.gensalt()
    )
    try:
        services.update_admin_user(id, admin_user)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/{id}", response_model=ShowAdminUserAuthenticationSchema)
def show(id: int, repository: UsersRepository = Depends()):
    return repository.get_by_id(id)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def remove(id: int, repository: UsersRepository = Depends()):
    repository.remove(id)

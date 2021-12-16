from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_202_ACCEPTED
from app.repositories.users_repository import UsersRepository
from .schemas import AdminUsersSchema, ShowAdminUserSchema
from app.services.auth_service import only_admin
from app.services.users_admin_service import UsersAdminService
from app.common.exceptions import EmailAdminUserAuthentication
import bcrypt


router = APIRouter(
    dependencies=[Depends(only_admin)]
)  # --> atribuindo autenticação para produtos


@router.post("/", response_model=ShowAdminUserSchema)
def create(admin_user: AdminUsersSchema, services: UsersAdminService = Depends()):
    admin_user.password = bcrypt.hashpw(
        admin_user.password.encode("utf8"), bcrypt.gensalt()
    )
    try:
        return services.create_user(admin_user)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/", response_model=List[ShowAdminUserSchema])
def index(repository: UsersRepository = Depends()):
    return repository.get_all()


@router.put("/{id}", response_model=ShowAdminUserSchema)
def update(
    id: int, admin_user: AdminUsersSchema, services: UsersAdminService = Depends()
):
    admin_user.password = bcrypt.hashpw(
        admin_user.password.encode("utf8"), bcrypt.gensalt()
    )
    try:
        return services.update(id, admin_user)
    except EmailAdminUserAuthentication as msg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg.message)


@router.get("/{id}", response_model=ShowAdminUserSchema)
def show(id: int, repository: UsersRepository = Depends()):
    return repository.get_by_id(id)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def remove(id: int, repository: UsersRepository = Depends()):
    repository.remove(id)

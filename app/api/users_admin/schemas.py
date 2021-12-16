from pydantic import BaseModel


class AdminUsersSchema(BaseModel):
    display_name: str
    email: str
    role = "admin"
    password: str


class ShowAdminUserSchema(BaseModel):
    display_name: str
    email: str
    role = "admin"
    id: int

    class Config:
        orm_mode = True


class ShowAdminUsersSchema(AdminUsersSchema):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel


class AdminUsersSchema(BaseModel):
    display_name: str
    email: str
    role = "admin"
    password: str


class ShowAdminUserSchema(BaseModel):
    display_name: str
    email: str
    role: str
    id: int

    class Config:
        orm_mode = True

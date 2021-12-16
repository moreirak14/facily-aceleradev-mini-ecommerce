from pydantic import BaseModel


class UsersSchema(BaseModel):
    display_name: str
    email: str
    role = "customer"
    password: str

    class Config:
        orm_mode = True


class ShowAdminUserSchema(BaseModel):
    display_name: str
    email: str
    role = "customer"
    id: int

    class Config:
        orm_mode = True

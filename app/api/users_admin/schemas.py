from pydantic import BaseModel


class AdminUsersSchema(BaseModel):
    display_name: str
    email: str
    phone_number: str
    role = 'admin'
    password: str


class ShowAdminUsersSchema(AdminUsersSchema):
    id: int

    class Config:
        orm_mode = True

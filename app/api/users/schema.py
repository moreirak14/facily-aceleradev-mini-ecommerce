from pydantic import BaseModel


class UsersSchema(BaseModel):
    display_name: str
    email: str
    phone_number: str
    role: str
    password: str


class ShowUsersSchema(UsersSchema):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import date


class UserSchema(BaseModel):
    email: str
    password: str
    display_name: str


class CustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user: UserSchema


class UpdateUserSchema(UserSchema):
    id: int


class UpdateCustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    birth_date: date
    user: UpdateUserSchema

    class Config:
        orm_mode = True


class ShowCustomersSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True

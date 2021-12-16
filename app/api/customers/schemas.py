from pydantic import BaseModel
from datetime import date
from app.api.users.schemas import ShowAdminUserSchema


class CustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user_id: int


class UpdateCustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    birth_date: date

    class Config:
        orm_mode = True


class ShowCustomersSchema(CustomersSchema):
    user: ShowAdminUserSchema

    class Config:
        orm_mode = True

from pydantic import BaseModel
from datetime import date


class CustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date


class ShowCustomersSchema(CustomersSchema):
    id: int

    class Config:
        orm_mode = True

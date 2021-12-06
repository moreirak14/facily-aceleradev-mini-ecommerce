from pydantic import BaseModel
from app.api.customers.schemas import ShowCustomersSchema


class AddressesSchema(BaseModel):
    address: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: bool
    customer_id: int


class ShowAddressesSchema(AddressesSchema):
    id: int
    customer: ShowCustomersSchema

    class Config:
        orm_mode = True

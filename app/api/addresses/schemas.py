from pydantic import BaseModel


class AddressesSchema(BaseModel):
    address: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: bool


class ShowAddressesSchema(AddressesSchema):
    id: int

    class Config:
        orm_mode = True

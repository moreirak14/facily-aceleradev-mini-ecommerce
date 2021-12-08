from pydantic import BaseModel


class UsersSchema(BaseModel):
    display_name: str
    email: str
    phone_number: str
    role = "customer"
    password: str

    class Config:
        orm_mode = True

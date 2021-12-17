from pydantic import BaseModel


class UsersSchema(BaseModel):
    display_name: str
    email: str
    role: str
    password: str


class UsersSchemaCustomer(BaseModel):
    display_name: str
    email: str
    role:  str
    password: str

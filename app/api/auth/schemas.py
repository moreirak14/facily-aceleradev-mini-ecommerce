from pydantic import BaseModel


class ShowUserAuthenticationSchema(BaseModel):
    display_name: str
    email: str
    id: int

    class Config:
        orm_mode = True

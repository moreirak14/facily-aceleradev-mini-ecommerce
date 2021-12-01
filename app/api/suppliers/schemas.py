from pydantic import BaseModel


class SuppliersSchema(BaseModel):
    name: str


class ShowSuppliersSchema(SuppliersSchema):
    id: int

    class Config: # exibe um unico id
        orm_mode = True

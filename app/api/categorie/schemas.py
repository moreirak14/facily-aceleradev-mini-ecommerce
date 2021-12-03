from pydantic import BaseModel


class CategorieSchema(BaseModel):
    name: str


class ShowCategorieSchema(CategorieSchema):
    id: int

    class Config:
        orm_mode = True

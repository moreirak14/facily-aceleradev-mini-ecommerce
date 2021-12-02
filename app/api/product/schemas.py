from pydantic import BaseModel


class ProductSchema(BaseModel):
    description: str
    price: float
    technical_details: str
    image: str
    visible: bool
    categorie_id: int
    supplier_id: int


class ShowProductSchema(ProductSchema):
    id: int
    
    class Config:
        orm_mode = True

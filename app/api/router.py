from fastapi import APIRouter
from .product.views import router as product_router


router = APIRouter()

router.include_router(product_router, prefix='/product') # --> prefix adiciona o /product na rota @app.router('')

from fastapi import APIRouter
from .product.views import router as product_router
from .suppliers.views import router as supplier_router
from .categorie.views import router as categorie_router
from .payment_methods.views import router as payment_methods_router


router = APIRouter()


router.include_router(product_router, prefix='/product') # --> prefix adiciona o /product na rota @app.router('')
router.include_router(supplier_router, prefix='/supplier')
router.include_router(categorie_router, prefix='/categorie')
router.include_router(payment_methods_router, prefix='/payment_methods')

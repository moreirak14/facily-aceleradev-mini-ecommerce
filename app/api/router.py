from fastapi import APIRouter
from .product.views import router as product_router
from .suppliers.views import router as supplier_router
from .categorie.views import router as categorie_router
from .payment_methods.views import router as payment_methods_router
from .product_discounts.views import router as payment_discounts_router
from .coupons.views import router as coupons_router
from .addresses.views import router as addresses_router
from .customers.views import router as customers_router
from .auth.views import router as auth_router
from .users.views import router as users_router
from .users_admin.views import router as users_admin_router
from .catalog.views import router as catalog_router


router = APIRouter()


router.include_router(
    product_router, prefix="/products", tags=["products"]
)  # --> prefix adiciona o /product na rota @app.router('')
router.include_router(
    supplier_router, prefix="/suppliers", tags=["suppliers"]
)  # --> tags=[] quebra por nome as requisicoes na app
router.include_router(categorie_router, prefix="/categories", tags=["categories"])
router.include_router(
    payment_methods_router, prefix="/payment_methods", tags=["payment_methods"]
)
router.include_router(
    payment_discounts_router, prefix="/payment_discounts", tags=["payment_discounts"]
)
router.include_router(coupons_router, prefix="/coupons", tags=["coupons"])
router.include_router(addresses_router, prefix="/addresses", tags=["addresses"])
router.include_router(customers_router, prefix="/customers", tags=["customers"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(users_admin_router, prefix="/users_admin", tags=["users_admin"])
router.include_router(catalog_router, prefix="/catalog", tags=["catalog"])

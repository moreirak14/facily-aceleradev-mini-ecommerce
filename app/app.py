from fastapi import FastAPI
from app.api.router import router
from fastapi_pagination import add_pagination


app = FastAPI(title="E - COMMERCE")
app.include_router(router)
add_pagination(app)

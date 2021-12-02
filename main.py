from fastapi import FastAPI
from app.api.router import router
from app.models.models import Base
from app.db.db import engine


Base.metadata.create_all(engine) # --> criar as tabelas no DB


app = FastAPI(title="E - COMMERCE")


app.include_router(router)

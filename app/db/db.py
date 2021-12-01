from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent # --> caminho absoluto da arquivo DB
SQLALCHEMY_DATABASE_URL = f'sqlite:///{DB_PATH}/database.db'


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True) # --> echo retorna no terminal os valores da query
Session = sessionmaker(bind=engine)


Base = declarative_base()
metadata = Base.metadata


def get_db():
    db = Session()
    try:
        yield db # --> é a idea que pode retornar multiplos valores
    finally:
        db.close()
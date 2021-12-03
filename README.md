# facily-aceleradev-mini-ecommerce

venv
fastapi
sqlalchemy
alembic


# _____________________________________
command alembic:

# instalar o alembic
pip install alembic

# iniciar o alembic
alembic init alembic

# criar a migracao 
alembic revision --autogenerate -m <descricao da minha migration>

# rodar a migracao
alembic upgrade head

# desfazer a migracao
alembic downgrade <id da versao>

# adicionar a base em env.py e alembic.ini
from app.models.models import Base
target_metadata = Base.metadata
sqlalchemy.url = sqlite:////home/kaique/Projects/test/facily-aceleradev-mini-ecommerce/app/db/database.db

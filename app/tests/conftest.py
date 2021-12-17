from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import (
    Base, Categorie, Supplier, User, Coupons, Customer, Product, PaymentMethod)
from app.db.db import get_db
from fastapi.testclient import TestClient
from app.app import app
import pytest
import factory


@pytest.fixture()
def db_session():
    engine = create_engine('sqlite:///./test.db',
                           connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    db = Session()
    yield db
    db.close()


@pytest.fixture()
def override_get_db(db_session):
    def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    return client


""" @pytest.fixture()
def jwt_token():
    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjcxMTMwNDMyfQ.PdOs9oPPI-cQ8RMmYRh0qljiCk4yha9kqbt08sdtQeU' """


@pytest.fixture()
def payment_method_factory(db_session):
    class PaymentMethodFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = PaymentMethod
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')
        enabled = None

    return PaymentMethodFactory


@pytest.fixture()
def product_factory(db_session, category_factory, supplier_factory):
    class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Product
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        description = factory.Faker('word')
        price = factory.Faker('pyfloat')
        technical_details = factory.Faker('word')
        image = factory.Faker('word')
        visible = None
        categorie = factory.SubFactory(category_factory)
        supplier = factory.SubFactory(supplier_factory)

    return ProductFactory


@pytest.fixture()
def customer_factory(db_session):
    class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Customer
            sqlalchemy_session = db_session

        id = factory.Sequence(int)
        first_name = factory.Faker('first_name')
        last_name = factory.Faker('last_name')
        phone_number = factory.Faker('phone_number')
        genre = factory.Faker('word')
        document_id = factory.Faker('word')
        birth_date = factory.Faker('date_of_birth')
        user_id = factory.Faker('pyint')

    return CustomerFactory


@pytest.fixture()
def coupon_factory(db_session):
    class CouponFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Coupons
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        code = None
        expire_at = None
        limit = None
        type = None
        value = None

    return CouponFactory


@pytest.fixture()
def supplier_factory(db_session):
    class SupplierFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Supplier
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return SupplierFactory


@pytest.fixture()
def category_factory(db_session):
    class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = Categorie
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        name = factory.Faker('name')

    return CategoryFactory


@pytest.fixture()
def user_factory(db_session):
    class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = User
            sqlalchemy_session = db_session

        id = factory.Faker('pyint')
        display_name = factory.Faker('name')
        email = factory.Faker('email')
        role = None
        password = '$2b$12$rPq8ggNxK5FFJKCdmfcdoeXsL2zr1O9vHGRZI/0zGUSskM2XuZkJu'

    return UserFactory


@pytest.fixture()
def user_admin_token(user_factory):
    user_factory(role='admin')

    return 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjcxMTMwNDMyfQ.PdOs9oPPI-cQ8RMmYRh0qljiCk4yha9kqbt08sdtQeU'


@pytest.fixture()
def admin_auth_header(user_admin_token):
    return {'Authorization': f'Bearer {user_admin_token}'}

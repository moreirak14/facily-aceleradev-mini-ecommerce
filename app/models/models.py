from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Float, Integer, String
from app.db.db import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(Date)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customer)


class Coupons(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True)
    expire_at = Column(DateTime)
    limit = Column(Integer)
    type = Column(String(15))
    value = Column(Float(10, 2))


class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enabled = Column(Boolean, default=True)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Categorie(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2)) # --> 10 quantidades, 2 casas decimais
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    categorie_id = Column(Integer, ForeignKey('categories.id')) # --> relacionamento com categoria
    categorie = relationship(Categorie) # --> acesso a instancia Categorie via um atributo
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship(Supplier)


class PaymentDiscount(Base):
    __tablename__ = 'payment_discounts'

    id = Column(Integer, primary_key=True)
    mode = Column(String(45))
    value = Column(Float(10, 2))
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)
    payment_methods_id = Column(Integer, ForeignKey('payment_methods.id'))
    payment_methods = relationship(PaymentMethod)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    display_name = Column(String(100))
    email = Column(String(50))
    role = Column(String(10))
    password = Column(String(100))

"""Update all

Revision ID: f5eca38ebe0e
Revises: 
Create Date: 2021-12-07 19:10:37.250877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f5eca38ebe0e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "coupons",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=True),
        sa.Column("expire_at", sa.DateTime(), nullable=True),
        sa.Column("limit", sa.Integer(), nullable=True),
        sa.Column("type", sa.String(length=15), nullable=True),
        sa.Column("value", sa.Float(precision=10, asdecimal=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "payment_methods",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "suppliers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=45), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("display_name", sa.String(length=45), nullable=True),
        sa.Column("email", sa.String(length=45), nullable=True),
        sa.Column("phone_number", sa.String(length=12), nullable=True),
        sa.Column("role", sa.String(length=15), nullable=True),
        sa.Column("password", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=45), nullable=True),
        sa.Column("last_name", sa.String(length=45), nullable=True),
        sa.Column("phone_number", sa.String(length=15), nullable=True),
        sa.Column("genre", sa.String(length=45), nullable=True),
        sa.Column("document_id", sa.String(length=45), nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document_id"),
    )
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=150), nullable=True),
        sa.Column("price", sa.Float(precision=10, asdecimal=2), nullable=True),
        sa.Column("technical_details", sa.String(length=255), nullable=True),
        sa.Column("image", sa.String(length=255), nullable=True),
        sa.Column("visible", sa.Boolean(), nullable=True),
        sa.Column("categorie_id", sa.Integer(), nullable=True),
        sa.Column("supplier_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["categorie_id"],
            ["categories.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_id"],
            ["suppliers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("city", sa.String(length=45), nullable=True),
        sa.Column("state", sa.String(length=2), nullable=True),
        sa.Column("number", sa.String(length=10), nullable=True),
        sa.Column("zipcode", sa.String(length=6), nullable=True),
        sa.Column("neighbourhood", sa.String(length=45), nullable=True),
        sa.Column("primary", sa.Boolean(), nullable=True),
        sa.Column("customer_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["customer_id"],
            ["customers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "payment_discounts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("mode", sa.String(length=45), nullable=True),
        sa.Column("value", sa.Float(precision=10, asdecimal=2), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("payment_methods_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["payment_methods_id"],
            ["payment_methods.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("payment_discounts")
    op.drop_table("addresses")
    op.drop_table("products")
    op.drop_table("customers")
    op.drop_table("users")
    op.drop_table("suppliers")
    op.drop_table("payment_methods")
    op.drop_table("coupons")
    op.drop_table("categories")
    # ### end Alembic commands ###

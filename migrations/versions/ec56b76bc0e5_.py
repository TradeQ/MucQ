"""empty message

Revision ID: ec56b76bc0e5
Revises: ba0c1bd1c779
Create Date: 2022-07-24 23:35:44.331580

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'ec56b76bc0e5'
down_revision = 'ba0c1bd1c779'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('liked_products', sa.String(length=60), nullable=True))
    op.drop_column('user', 'liked_product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('liked_product', sqlite.JSON(), nullable=True))
    op.drop_column('user', 'liked_products')
    # ### end Alembic commands ###
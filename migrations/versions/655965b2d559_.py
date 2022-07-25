"""empty message

Revision ID: 655965b2d559
Revises: ec56b76bc0e5
Create Date: 2022-07-25 09:26:10.099977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '655965b2d559'
down_revision = 'ec56b76bc0e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'liked_products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('liked_products', sa.VARCHAR(length=60), nullable=True))
    # ### end Alembic commands ###
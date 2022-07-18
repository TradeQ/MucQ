"""empty message

Revision ID: 7a8eccc55391
Revises: eb3d293716e4
Create Date: 2022-07-18 23:02:26.107575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8eccc55391'
down_revision = 'eb3d293716e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('date_posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'date_posted')
    # ### end Alembic commands ###

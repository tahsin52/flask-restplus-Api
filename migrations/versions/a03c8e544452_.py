"""empty message

Revision ID: a03c8e544452
Revises: 21cf8a1df79d
Create Date: 2021-06-07 03:32:58.066148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03c8e544452'
down_revision = '21cf8a1df79d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'parent_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('parent_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###

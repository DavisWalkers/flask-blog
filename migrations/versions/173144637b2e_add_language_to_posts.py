"""add language to posts

Revision ID: 173144637b2e
Revises: d00e989ac35c
Create Date: 2020-09-26 15:00:17.655492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '173144637b2e'
down_revision = 'd00e989ac35c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###

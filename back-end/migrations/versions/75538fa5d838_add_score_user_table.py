"""add score user table

Revision ID: 75538fa5d838
Revises: a32945d954b9
Create Date: 2020-07-05 15:54:50.794353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75538fa5d838'
down_revision = 'a32945d954b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'score')
    # ### end Alembic commands ###

"""User Authentication

Revision ID: 413b16e6453e
Revises: 634a340a6416
Create Date: 2020-09-23 23:16:03.191923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413b16e6453e'
down_revision = '634a340a6416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###

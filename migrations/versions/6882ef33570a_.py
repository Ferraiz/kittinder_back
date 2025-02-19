"""empty message

Revision ID: 6882ef33570a
Revises: c5cd7a4bff20
Create Date: 2020-10-05 11:19:54.940814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6882ef33570a'
down_revision = 'c5cd7a4bff20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favourites_table', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favourites_table', sa.Column('image', sa.VARCHAR(length=120), nullable=True))
    # ### end Alembic commands ###

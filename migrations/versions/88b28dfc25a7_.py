"""empty message

Revision ID: 88b28dfc25a7
Revises: ef9667ff3016
Create Date: 2020-10-05 11:12:06.636859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88b28dfc25a7'
down_revision = 'ef9667ff3016'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favourites_table', sa.Column('image', sa.String(length=120), nullable=True))
    op.drop_column('favourites_table', 'photo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favourites_table', sa.Column('photo', sa.VARCHAR(length=120), nullable=True))
    op.drop_column('favourites_table', 'image')
    # ### end Alembic commands ###

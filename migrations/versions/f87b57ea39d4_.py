"""empty message

Revision ID: f87b57ea39d4
Revises: 
Create Date: 2021-03-17 09:08:32.064444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f87b57ea39d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('no_of_rooms', sa.String(length=11), nullable=True),
    sa.Column('no_of_bathrooms', sa.String(length=11), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('type_', sa.Enum('House', 'Apartment', name='PropertyType'), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('photo', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###

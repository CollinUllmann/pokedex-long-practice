"""empty message

Revision ID: b24c6e20917e
Revises: 
Create Date: 2024-02-14 19:47:21.657930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b24c6e20917e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('moves', sa.String(length=255), nullable=False),
    sa.Column('captured', sa.Boolean(), nullable=False),
    sa.Column('encounter_rate', sa.Integer(), nullable=True),
    sa.Column('catch_rate', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('number'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('number')
    )
    op.create_table('pokemon_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('happiness', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('pokemonId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemonId'], ['pokemon.number'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('pokemon_types')
    op.drop_table('pokemon')
    # ### end Alembic commands ###

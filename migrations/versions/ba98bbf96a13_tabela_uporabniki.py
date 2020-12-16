"""tabela uporabniki

Revision ID: ba98bbf96a13
Revises: 
Create Date: 2020-12-04 22:24:41.766059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba98bbf96a13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uporabniki',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uporabnisko_ime', sa.String(length=50), nullable=False),
    sa.Column('e_naslov', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_uporabniki_e_naslov'), 'uporabniki', ['e_naslov'], unique=True)
    op.create_index(op.f('ix_uporabniki_uporabnisko_ime'), 'uporabniki', ['uporabnisko_ime'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_uporabniki_uporabnisko_ime'), table_name='uporabniki')
    op.drop_index(op.f('ix_uporabniki_e_naslov'), table_name='uporabniki')
    op.drop_table('uporabniki')
    # ### end Alembic commands ###
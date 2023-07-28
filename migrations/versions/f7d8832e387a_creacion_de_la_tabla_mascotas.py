"""creacion de la tabla mascotas

Revision ID: f7d8832e387a
Revises: 8de103564ad6
Create Date: 2023-07-27 19:22:00.117579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7d8832e387a'
down_revision = '8de103564ad6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mascotas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('tipo', sa.Enum('Perro', 'Gato', 'Cuy', name='tipomascota'), nullable=False),
    sa.Column('sexo', sa.Enum('Macho', 'Hembra', 'Helicoptero', 'Otro', name='sexomascota'), nullable=True),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mascotas')
    # ### end Alembic commands ###

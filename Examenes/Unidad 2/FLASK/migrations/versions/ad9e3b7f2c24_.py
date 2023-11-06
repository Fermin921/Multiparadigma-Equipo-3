"""empty message

Revision ID: ad9e3b7f2c24
Revises: 
Create Date: 2023-11-06 10:48:56.364604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad9e3b7f2c24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aula',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_aula', sa.String(length=100), nullable=False),
    sa.Column('capacidad_maxima', sa.Integer(), nullable=True),
    sa.Column('edades_admitidas', sa.String(length=50), nullable=True),
    sa.Column('maestro_a_cargo', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comida',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_comida', sa.String(length=100), nullable=False),
    sa.Column('ingredientes', sa.String(length=200), nullable=True),
    sa.Column('restricciones_alimenticias', sa.String(length=100), nullable=True),
    sa.Column('fecha_introduccion', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('niño',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('genero', sa.String(length=20), nullable=True),
    sa.Column('tutor_principal', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personal_guarderia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('puesto', sa.String(length=50), nullable=True),
    sa.Column('fecha_contratacion', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tutor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('direccion', sa.String(length=200), nullable=True),
    sa.Column('numero_telefono', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tutor')
    op.drop_table('personal_guarderia')
    op.drop_table('niño')
    op.drop_table('comida')
    op.drop_table('aula')
    # ### end Alembic commands ###

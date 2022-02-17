"""Nova coluna Senha na tabela Usuario e relacionamentos entre usuario e produto

Revision ID: d5675b12e299
Revises: 47f76b2f88e7
Create Date: 2022-02-16 13:37:21.059342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5675b12e299'
down_revision = '47f76b2f88e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_usuario', 'usuario', ['usuario_id'], ['id'])

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('senha')

    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario', type_='foreignkey')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###

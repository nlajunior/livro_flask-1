"""empty message

Revision ID: 977e7a6a5814
Revises: e7567e687eb6
Create Date: 2019-03-01 09:18:54.015032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '977e7a6a5814'
down_revision = 'e7567e687eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('product', sa.Column('category', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'category', ['category'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'category')
    op.drop_table('category')
    # ### end Alembic commands ###

'''empty message

Revision ID: a683da0e8333
Revises: 
Create Date: 2018-01-16 14:28:28.408369

'''
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a683da0e8333'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=50), nullable=False),
    sa.Column('category_description', sa.String(length=256), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('category_id'),
    sa.UniqueConstraint('category_name')
    )
    op.create_table('recipies',
    sa.Column('recipie_id', sa.Integer(), nullable=False),
    sa.Column('recipie_name', sa.String(length=100), nullable=False),
    sa.Column('ingredients', sa.String(length=256), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.PrimaryKeyConstraint('recipie_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipies')
    op.drop_table('categories')
    op.drop_table('users')
    # ### end Alembic commands ###

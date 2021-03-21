"""empty message

Revision ID: c97a7c257f2d
Revises: 
Create Date: 2021-03-21 13:08:54.757038

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c97a7c257f2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.drop_table('fwbdzz')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fwbdzz',
    sa.Column('nid', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_bin', length=20), nullable=True),
    sa.Column('pwd', mysql.VARCHAR(collation='utf8mb4_bin', length=64), nullable=True),
    mysql_collate='utf8mb4_bin',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user')
    # ### end Alembic commands ###
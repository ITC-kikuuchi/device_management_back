"""empty message

Revision ID: a14b90aa8e7f
Revises: 42fd3605de24
Create Date: 2024-01-27 09:22:29.571922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a14b90aa8e7f'
down_revision: Union[str, None] = '42fd3605de24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_ios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label_name', sa.String(length=255), nullable=False),
    sa.Column('ios_name', sa.String(length=255), nullable=True),
    sa.Column('manufacturer', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('os', sa.String(length=255), nullable=True),
    sa.Column('carrier', sa.String(length=255), nullable=True),
    sa.Column('condition', sa.String(length=255), nullable=True),
    sa.Column('delivery_date', sa.Date(), nullable=True),
    sa.Column('disposal_date', sa.Date(), nullable=True),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.Column('delete_flag', sa.Boolean(), nullable=False, server_default="0"),
    sa.Column('create_id', sa.Integer(), nullable=True),
    sa.Column('update_id', sa.Integer(), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_ios')
    # ### end Alembic commands ###
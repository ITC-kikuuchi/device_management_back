"""empty message

Revision ID: 42fd3605de24
Revises: 
Create Date: 2024-01-16 11:09:50.818941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '42fd3605de24'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('m_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mail_address', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('user_name', sa.String(length=255), nullable=False),
    sa.Column('create_id', sa.Integer(), nullable=True),
    sa.Column('update_id', sa.Integer(), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mail_address')
    )
    op.create_table('t_pc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label_name', sa.String(length=255), nullable=False),
    sa.Column('pc_name', sa.String(length=255), nullable=True),
    sa.Column('user_name', sa.String(length=255), nullable=True),
    sa.Column('pc_user', sa.String(length=255), nullable=True),
    sa.Column('condition', sa.String(length=255), nullable=True),
    sa.Column('manufacturer', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('service_tag', sa.String(length=255), nullable=True),
    sa.Column('os', sa.String(length=255), nullable=True),
    sa.Column('bit', sa.Integer(), nullable=True),
    sa.Column('ie_version', sa.String(length=255), nullable=True),
    sa.Column('ip_address', sa.String(length=255), nullable=True),
    sa.Column('gx_wwp_license', sa.String(length=255), nullable=True),
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
    op.drop_table('t_pc')
    op.drop_table('m_user')
    # ### end Alembic commands ###

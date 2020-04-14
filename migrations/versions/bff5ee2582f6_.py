"""empty message

Revision ID: bff5ee2582f6
Revises: 0aa765eaf89a
Create Date: 2019-10-31 14:19:36.687588

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bff5ee2582f6'
down_revision = '0aa765eaf89a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TEST_TASK', sa.Column('end_time', sa.DateTime(), nullable=True))
    op.add_column('TEST_TASK', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.drop_column('TEST_TASK', 'time_stamp')
    op.add_column('TRAINING', sa.Column('end_time', sa.DateTime(), nullable=True))
    op.add_column('TRAINING', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.drop_column('TRAINING', 'time_stamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('TRAINING', sa.Column('time_stamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('TRAINING', 'start_time')
    op.drop_column('TRAINING', 'end_time')
    op.add_column('TEST_TASK', sa.Column('time_stamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('TEST_TASK', 'start_time')
    op.drop_column('TEST_TASK', 'end_time')
    # ### end Alembic commands ###

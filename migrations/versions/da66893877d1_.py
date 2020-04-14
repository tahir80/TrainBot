"""empty message

Revision ID: da66893877d1
Revises: 27ffaeaf0a7a
Create Date: 2020-04-08 08:50:42.114689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da66893877d1'
down_revision = '27ffaeaf0a7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('BONUS', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('TEST_TASK_BONUS', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('TRAINING_BONUS', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('TRAINING_BONUS', 'timestamp')
    op.drop_column('TEST_TASK_BONUS', 'timestamp')
    op.drop_column('BONUS', 'timestamp')
    # ### end Alembic commands ###
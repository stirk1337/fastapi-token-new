"""Fix date naming

Revision ID: a8a45a0ee338
Revises: b529e312fec0
Create Date: 2023-06-18 18:51:23.838640

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a8a45a0ee338'
down_revision = 'b529e312fec0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column(
        'date_of_next_increase', sa.Date(), nullable=False))
    op.drop_column('user', 'date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('date', sa.DATE(),
                  autoincrement=False, nullable=False))
    op.drop_column('user', 'date_of_next_increase')
    # ### end Alembic commands ###

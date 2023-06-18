"""Create Salary model

Revision ID: f82da5abebaa
Revises: fba32410b256
Create Date: 2023-06-18 16:08:46.036816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f82da5abebaa'
down_revision = 'fba32410b256'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_salary_email', table_name='salary')
    op.drop_column('salary', 'is_superuser')
    op.drop_column('salary', 'is_verified')
    op.drop_column('salary', 'email')
    op.drop_column('salary', 'hashed_password')
    op.drop_column('salary', 'is_active')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('salary', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('salary', sa.Column('hashed_password', sa.VARCHAR(length=1024), autoincrement=False, nullable=False))
    op.add_column('salary', sa.Column('email', sa.VARCHAR(length=320), autoincrement=False, nullable=False))
    op.add_column('salary', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('salary', sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.create_index('ix_salary_email', 'salary', ['email'], unique=False)
    # ### end Alembic commands ###

"""create tables

Revision ID: 852a1460c108
Revises: d9061947fd56
Create Date: 2023-10-28 07:42:34.130247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '852a1460c108'
down_revision: Union[str, None] = 'd9061947fd56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('medical_records', sa.Column('doctor_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'medical_records', 'doctors', ['doctor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'medical_records', type_='foreignkey')
    op.drop_column('medical_records', 'doctor_id')
    # ### end Alembic commands ###
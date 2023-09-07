"""review  table

Revision ID: ba34a680a9b8
Revises: a75f643ef184
Create Date: 2023-09-07 18:09:43.759690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba34a680a9b8'
down_revision: Union[str, None] = 'a75f643ef184'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('star_rating', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###

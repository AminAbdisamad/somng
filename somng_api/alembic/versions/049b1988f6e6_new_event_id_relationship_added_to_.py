"""new event_id relationship added to workshops table

Revision ID: 049b1988f6e6
Revises: 73bb77faa8d5
Create Date: 2021-07-13 10:44:23.707790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "049b1988f6e6"
down_revision = "73bb77faa8d5"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("workshops", sa.Column("event_id", sa.Integer))


def downgrade():
    pass

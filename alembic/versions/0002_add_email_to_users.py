"""add email column to users

Revision ID: 0002
Revises: 0001
Create Date: 2026-05-01 00:00:01.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0002"
down_revision: Union[str, None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("email", sa.String(length=255), nullable=True),
    )
    op.create_unique_constraint(
        "uq_users_email",
        "users",
        ["email"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_users_email", "users", type_="unique")
    op.drop_column("users", "email")

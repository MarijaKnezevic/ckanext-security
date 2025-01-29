"""Create security totp table

Revision ID: 5ad63b021ed4
Revises:
Create Date: 2025-01-24 18:36:01.318092
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        "user_security_totp",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.UnicodeText, nullable=False),
        sa.Column("secret", sa.String(255), nullable=False),
        sa.Column("last_successful_challenge", sa.DateTime),
    )
    # Create sequence and set default
    op.execute("CREATE SEQUENCE IF NOT EXISTS user_security_totp_id_seq")
    op.execute("ALTER TABLE user_security_totp ALTER COLUMN id SET DEFAULT nextval('user_security_totp_id_seq')")
    op.execute("ALTER SEQUENCE user_security_totp_id_seq OWNED BY user_security_totp.id")


def downgrade():
    op.execute("DROP SEQUENCE IF EXISTS user_security_totp_id_seq")
    op.drop_table("user_security_totp")

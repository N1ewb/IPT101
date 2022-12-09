"""empty message

Revision ID: 0b3ab66dbdd8
Revises: 00f3cdbb0b99
Create Date: 2022-12-07 12:17:43.069303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b3ab66dbdd8'
down_revision = '00f3cdbb0b99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('Num_of_posts', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('fb_link', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'user', ['fb_link'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'fb_link')
    op.drop_column('user', 'Num_of_posts')
    # ### end Alembic commands ###
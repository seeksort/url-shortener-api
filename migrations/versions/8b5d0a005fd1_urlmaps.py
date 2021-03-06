"""urlmaps

Revision ID: 8b5d0a005fd1
Revises: 
Create Date: 2018-03-11 11:07:43.201367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b5d0a005fd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(), nullable=True),
    sa.Column('url_no_protocol', sa.String(), nullable=True),
    sa.Column('short_url_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_url_id')
    )
    op.create_index(op.f('ix_url_map_original_url'), 'url_map', ['original_url'], unique=True)
    op.create_index(op.f('ix_url_map_url_no_protocol'), 'url_map', ['url_no_protocol'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_url_map_url_no_protocol'), table_name='url_map')
    op.drop_index(op.f('ix_url_map_original_url'), table_name='url_map')
    op.drop_table('url_map')
    # ### end Alembic commands ###

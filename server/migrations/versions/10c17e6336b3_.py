"""empty message

Revision ID: 10c17e6336b3
Revises: e0a6ab933f26
Create Date: 2024-05-23 11:14:38.117393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10c17e6336b3'
down_revision = 'e0a6ab933f26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('item_img', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('page_views', sa.Integer(), nullable=True),
    sa.Column('inventory', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('products_table')
    with op.batch_alter_table('orders_table', schema=None) as batch_op:
        batch_op.drop_constraint('fk_orders_table_item_id_products_table', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_orders_table_item_id_items_table'), 'items_table', ['item_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders_table', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_orders_table_item_id_items_table'), type_='foreignkey')
        batch_op.create_foreign_key('fk_orders_table_item_id_products_table', 'products_table', ['item_id'], ['id'])

    op.create_table('products_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('category', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('page_views', sa.INTEGER(), nullable=True),
    sa.Column('inventory', sa.INTEGER(), nullable=False),
    sa.Column('item_name', sa.VARCHAR(), nullable=False),
    sa.Column('item_img', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('items_table')
    # ### end Alembic commands ###

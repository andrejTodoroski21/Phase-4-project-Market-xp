from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# write your models here!

class User (db.Model, SerializerMixin):
    __tablename__  = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    # is_seller = db.Column(db.Boolean, nullable=False)
    # cc_numbers = db.Column(db.Integer, unique=True) 
    # cc_pin = db.Column(db.Integer, unique=True) 
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    # address = db.Column(db.String, nullable=False)
    _hashed_password = db.Column(db.String)
    # email = db.Column(db.String, nullable=False)

    orders = db.relationship('Order', back_populates='user')
    items = db.relationship('Item', secondary='orders_table', back_populates='users')

    purchased_items = association_proxy('orders', 'item')
    serialize_rules = ('-orders.user', '-items.users',)


class Item(db.Model, SerializerMixin):
    __tablename__ = 'items_table'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    item_img = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    # is_sold_out = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    price = db.Column(db.Integer, nullable=False)
    # page_views = db.Column(db.Integer, server_default=None) V2
    inventory = db.Column(db.Integer, nullable=False)

    orders = db.relationship('Order', back_populates='item')
    users = db.relationship('User', secondary='orders_table', back_populates='items')

    buyers = association_proxy('orders', 'user')
    serialize_rules = ('-orders.item', '-users.items',)


class Item(db.Model, SerializerMixin):
    __tablename__ = 'orders_table'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items_table.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    price_sold = db.Column(db.Integer )
    quantity = dbColumn(db.Integer)
    sold_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", back_populates="orders")
    item = db.relationship("Item", back_populates="orders")
    serialize_rules = ('-user.orders', '-item.orders',)

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments_table'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    serialize_rules = ('-user.comments',)






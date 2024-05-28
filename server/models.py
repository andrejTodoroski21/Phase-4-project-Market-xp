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

    carts = db.relationship('Cart', back_populates='user')
    items = db.relationship('Item', secondary='carts_table', back_populates='users')

    purchased_items = association_proxy('carts', 'item')
    serialize_rules = ('-carts.user', '-items.users',)


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

    carts = db.relationship('Cart', back_populates='item')
    users = db.relationship('User', secondary='carts_table', back_populates='items')

    buyers = association_proxy('carts', 'user')
    serialize_rules = ('-carts.item', '-users.items',)


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts_table'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items_table.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    price_sold = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    sold_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", back_populates="carts")
    item = db.relationship("Item", back_populates="carts")
    serialize_rules = ('-user.carts', '-item.carts',)

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments_table'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    serialize_rules = ('-user.comments',)






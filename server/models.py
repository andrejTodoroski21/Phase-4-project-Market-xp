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
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    _hashed_password = db.Column(db.String)

    carts = db.relationship('Cart', back_populates='user', cascade='all, delete-orphan')
    items = db.relationship('Item', back_populates='seller', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')

    purchased_items = association_proxy('carts', 'item')
    serialize_rules = ('-carts.user', '-items.seller', '-comments.user')


class Item(db.Model, SerializerMixin):
    __tablename__ = 'items_table'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String, nullable=False)
    item_img = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    price = db.Column(db.Integer, nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    # page_views = db.Column(db.Integer, server_default=None) V2
    seller_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))

    seller = db.relationship('User', back_populates='items')
    comments = db.relationship('Comment', back_populates='item', cascade='all, delete-orphan')
    carts = db.relationship('Cart', back_populates='items', cascade='all, delete-orphan')

    buyers = association_proxy('cart', 'user')
    serialize_rules = ('-seller', '-comments', '-carts')


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts_table'
    # cart is a joiner table between users and items
    id = db.Column(db.Integer, primary_key=True)
    price_sold = db.Column(db.Integer)
    # this is a forgeign key to the items table
    item_id = db.Column(db.Integer, db.ForeignKey('items_table.id'))
    # this is a forgeign key to the user table
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    sold_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship("User", back_populates="carts")
    items = db.relationship("Item", back_populates="carts")

    serialize_rules = ('-user.carts', '-items.carts')


class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments_table'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items_table.id'), nullable=False)

    user = db.relationship('User', back_populates='comments')
    item = db.relationship('Item', back_populates='comments')

    serialize_rules = ('-user.comments', '-item.comments')
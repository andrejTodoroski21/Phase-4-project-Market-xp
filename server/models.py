from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users_table'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    _hashed_password = db.Column(db.String)

    # there is a many to many relationship between users and items with cart being the join table.
    # ther is also a many to one relationship between users and comments.
    # the cascade is used to delete everthing 
    purchased_items = db.relationship('Cart', back_populates='user', cascade='all, delete-orphan')
    # means that if an Item object is disassociated from its parent (e.g., the seller is deleted or the relationship is broken),
    # it will be automatically deleted from the database.
    items = db.relationship('Item', foreign_keys='Item.seller_id', back_populates='seller', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')

    serialize_rules = ('-purchased_items.user', '-items.seller', '-comments.user')

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
    seller_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    buyer_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))

    seller = db.relationship('User', foreign_keys=[seller_id], back_populates='items')
    buyer = db.relationship('User', foreign_keys=[buyer_id])
    comments = db.relationship('Comment', back_populates='item', cascade='all, delete-orphan')
    purchases = db.relationship('Cart', back_populates='item', cascade='all, delete-orphan')

    serialize_rules = ('-seller', '-comments', '-purchases')

class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts_table'

    id = db.Column(db.Integer, primary_key=True)
    price_sold = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items_table.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users_table.id'))
    sold_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', back_populates='purchased_items')
    item = db.relationship('Item', back_populates='purchases')

    serialize_rules = ('-user.purchased_items', '-item.purchases')

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
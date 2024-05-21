#!/usr/bin/env python3

from app import app
from models import db, Product, User, Order
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Order.query.delete()
        User.query.delete()
        Product.query.delete()

        print("creating Orders...")


        print("creating Users")


        print("creating Products")
        nintendo_64 = Product(product_name = "N64", )
        id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    product_img = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    # is_sold_out = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    price = db.Column(db.Integer, nullable=False)
    page_views = db.Column(db.Integer)
    inventory = db.Column(db.Integer, nullable=False)

        print("Seeding complete!")

#!/usr/bin/env python3

from app import app
from models import db, Item, User, Order
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Order.query.delete()
        User.query.delete()
        Item.query.delete()

        print("creating Orders...")
        nintendo_64 = Order(price_sold= 120)
        nintendo_3ds = Order(price_sold=80) 
        eevee_plushie = Order(price_sold = 30)
        cd_player = Order(price_sold=70)
        carhartt_jacket = Order(price_sold=110)
        orders = [nintendo_3ds, nintendo_64, eevee_plushie, cd_player, carhartt_jacket]

        print("creating Users")
        andrej = User(is_seller=False, first_name="Andrej", last_name="Todoroski", username = "Monke", address="123 blvd")
        dan = User(is_seller=True, first_name="Dan", last_name="Castanheira", username = "Dannycast", address="broad st")
        will = User(is_seller=False, first_name="Will", last_name="Metzler", username = "Willymet", address="23 blanch ct")
        users = [will, dan, andrej]

        print("creating Products")
        nintendo_64 = Item(item_name = "N64", item_img = "https://i5.walmartimages.com/seo/Restored-Nintendo-64-N64-System-Video-Game-Console-Refurbished_4d39d2ad-33a4-46df-95d8-c68110826631_2.ed4f595c99d114de02b77d9fdf70d57f.jpeg", category = "console", price = 120, inventory = 2)
        nintendo_3ds = Item(item_name = "3ds", item_img = "https://cdn.mos.cms.futurecdn.net/madpibo7RKfTtQ3mnaVdPT.jpg", category = "console", price = 80, inventory = 1)
        eevee_plushie = Item(item_name = "Eevee plushie", item_img = "https://m.media-amazon.com/images/I/71ktlCcangL.jpg", category = "doll", price = 30, inventory = 3)
        cd_player= Item(item_name = "Sony Walkman", item_img = "https://i.ebayimg.com/images/g/xcAAAOSwr5tg6PCD/s-l1200.webp", category = "", price = 70, inventory = 5)
        carhartt_jacket = Item(item_name = "Carhartt Jacket", item_img = "https://i.ebayimg.com/images/g/BcUAAOSw2tBj6rHq/s-l1200.webp", category = "", price = 110, inventory = 8)
        items = [nintendo_3ds, nintendo_64, eevee_plushie, cd_player, carhartt_jacket]
        db.session.add_all(orders)
        db.session.add_all(users)
        db.session.add_all(items)
        db.session.commit()

        print("Seeding complete!")

#!/usr/bin/env python3

from app import app
from models import db, Item, User, Item
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Item.query.delete()
        User.query.delete()
        Item.query.delete()

        print("creating Orders...")
        nintendo_64 = Item(price_sold= 120)
        nintendo_3ds = Item(price_sold=80) 
        eevee_plushie = Item(price_sold = 30)
        cd_player = Item(price_sold=70)
        carhartt_jacket = Item(price_sold=110)
        items = [nintendo_3ds, nintendo_64, eevee_plushie, cd_player, carhartt_jacket]

        print("creating Users")
        andrej = User(first_name="Andrej", last_name="Todoroski", username = "Monke")
        dan = User(first_name="Dan", last_name="Castanheira", username = "Dannycast")
        will = User(first_name="Will", last_name="Metzler", username = "Willymet")
        users = [will, dan, andrej]

        print("creating Items")
        nintendo_64 = Item(item_name = "N64", item_img = "https://i5.walmartimages.com/seo/Restored-Nintendo-64-N64-System-Video-Game-Console-Refurbished_4d39d2ad-33a4-46df-95d8-c68110826631_2.ed4f595c99d114de02b77d9fdf70d57f.jpeg", category = "console", description ="a super old ancient console where you can play some of the oldest games ever made", price = 120, inventory = 2)
        nintendo_3ds = Item(item_name = "3ds", item_img = "https://cdn.mos.cms.futurecdn.net/madpibo7RKfTtQ3mnaVdPT.jpg", category = "console", description = "a fun console to play on that has a 3d setting",price = 80, inventory = 1)
        eevee_plushie = Item(item_name = "Eevee plushie", item_img = "https://m.media-amazon.com/images/I/71ktlCcangL.jpg", category = "doll", description = "a perfect little pokemon toy for a loved one",price = 30, inventory = 3)
        cd_player= Item(item_name = "Sony Walkman", item_img = "https://i.ebayimg.com/images/g/xcAAAOSwr5tg6PCD/s-l1200.webp", category = "electronics",description = "classic walkman player if youre looking to collect a relic", price = 70, inventory = 5)
        carhartt_jacket = Item(item_name = "Carhartt Jacket", item_img = "https://i.ebayimg.com/images/g/BcUAAOSw2tBj6rHq/s-l1200.webp", category = "clothing", description = "a popular reliable jacket looks better the more worn out it is",price = 110, inventory = 8)
        items = [nintendo_3ds, nintendo_64, eevee_plushie, cd_player, carhartt_jacket]
        db.session.add_all(carts)
        db.session.add_all(users)
        db.session.add_all(items)
        db.session.commit()

        print("Seeding complete!")

#!/usr/bin/env python3
import os
from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt


from models import db, User, Item, Comment, Cart

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

db.init_app(app)

# this route is used to get the users from the database
@app.get('/api/users')
def index():
    return [u.to_dict() for u in User.query.all()], 200

@app.get('/api/users/<int:id>')
def users_by_id(id):
    user = User.query.where(User.id == id).first()
    if user:
        return user.to_dict(), 200
    else:
        return {'error': 'Not found'}, 404

# we are creating a new user by creating a post request requiring a username, first name, last name, and a password.
@app.post('/api/users')
def create_user():
    try:
        new_user = User(username=request.json['username'], first_name=request.json['first_name'], last_name=request.json['last_name'])
        # using the bcrypt library to hash the password
        new_user._hashed_password = bcrypt.generate_password_hash(request.json['_hashed_password']).decode('utf-8')
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id  # Store the user ID in the session
        return new_user.to_dict(), 201
    except Exception as e:
        return { 'error': str(e) }, 406

# SEE WHICH USER IS LOGGED IN
@app.get('/api/get-session')
def get_session():
    user_id = session.get('user_id')  # Retrieve the user ID from the session
    if user_id:
        user = User.query.get(user_id)
        if user:
            return user.to_dict(), 200
    return {}, 204

# LOGIN AND LOGOUT
# to login we are creating a post request that requires a username and a password.
@app.post('/api/login')
def login():
    username = request.json.get('user')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    # in the if statment we are checking to see it the username is in the database and we are hashing the password the user input and 
    # comparing it to the password in the database.
    if user and bcrypt.check_password_hash(user._hashed_password, password):
        session['user_id'] = user.id  # Store the user ID in the session
        return user.to_dict(), 201
    else:
        return {'error': 'Username or password was invalid'}, 401

# to logout we are creating a delete request by doing session.pop to remove the user id from the session.
@app.delete('/api/logout')
def logout():
    session.pop('user_id')  # Remove the user ID from the session on logout
    return {}, 204

# GET LISTINGS
# we are creating a get request to get the items from the database.
@app.get('/api/items')
def get_items():
    return [i.to_dict() for i in Item.query.all()], 200

# POST LISTINGS
# we are using a post request to create a new item in the database.
@app.post('/api/items')
def post_items():
    try:
        data = request.json
        # (**data) unpacks the data dictionary into the new_listing variable.
        new_listing = Item(**data)
        db.session.add(new_listing)
        db.session.commit()
        return jsonify( new_listing.to_dict() ), 201
    except Exception as e:
        return jsonify( {'error': str(e)} ), 406

# GET COMMENTS
# here we are creating a get request to get the comments from the database.
@app.get('/api/comments')
def get_comments():
    return [c.to_dict() for c in Comment.query.all()], 200

# in this get request we are gettting the comments by the item_id from the database.
@app.get('/api/items/<int:item_id>/comments')
def get_comments_by_item_id(item_id):
    item = Item.query.get(item_id)
    if item:
        comments = Comment.query.filter_by(item_id=item_id).all()
        return [comment.to_dict() for comment in comments], 200
    else:
        return {'error': 'Item not found'}, 404

# POST COMMENTS
# this post request checks for the current user that is logged in and if the user is authorized to post a comment.
@app.post('/api/comments')
def post_comments():
    try:
        data = request.json
        new_comment = Comment(**data)
        new_comment.user_id = session.get('user_id')
        db.session.add(new_comment)
        db.session.commit()
        return jsonify( new_comment.to_dict() ), 201
    except Exception as e:
        return jsonify( {'error': str(e)} ), 406

# users can delete their own comments
@app.delete('/api/comments/<int:id>')
def delete_comments(id):
    try:
        comment = Comment.query.get(id)
        if comment:
            if comment.user_id == session.get('user_id'):
                db.session.delete(comment)
                db.session.commit()
                return {}, 204
            else:
                return {'error': 'You are not authorized to delete this comment'}, 403
        else:
            return {'error': 'Comment not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 406

# getting the items 
@app.get('/api/cart')
def get_cart():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'User not logged in'}), 401

        cart_items = Cart.query.filter_by(user_id=user_id).all()
        return jsonify([ci.to_dict() for ci in cart_items]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 406

# checks if the inventory is greater than 0 and if it is it adds it to the order history
@app.post('/api/items/<int:id>/buy')
def buy_now(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if item.inventory <=0:
        return jsonify({'error': 'Item out of stock'}), 400

    item.inventory -= 1
    purchase = Cart(
        price_sold=item.price,
        item_id=item.id,
        user_id=session.get('user_id'),
        sold_at=db.func.now()
        )
    db.session.add(purchase)
    db.session.commit()

    return jsonify({'message': 'Item purchased successfully'}), 200    
    if item.inventory <= 0:
        return jsonify({'error': 'Item out of stock'}), 400

    # Update inventory
    item.inventory -= 1

    # Create a new purchase record
    purchase = Cart(
        price_sold=item.price,
        item_id=item.id,
        user_id=current_user.id,
        sold_at=db.func.now()
    )
    db.session.add(purchase)
    db.session.commit()

    return jsonify({'message': 'Item purchased successfully'}), 200
    

@app.get('/api/profile')
def get_purchased_items():
    purchased_items = Cart.query.filter_by(user_id=current_user.id).all()
    return jsonify([purchase.item.to_dict() for purchase in purchased_items])


if __name__ == '__main__':
    app.run(port=5555, debug=True)

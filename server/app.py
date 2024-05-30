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

# USER SIGNUP 
@app.post('/api/users')
def create_user():
    try:
        new_user = User(username=request.json['username'], first_name=request.json['first_name'], last_name=request.json['last_name'])
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
@app.post('/api/login')
def login():
    username = request.json.get('user')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user._hashed_password, password):
        session['user_id'] = user.id  # Store the user ID in the session
        return user.to_dict(), 201
    else:
        return {'error': 'Username or password was invalid'}, 401

@app.delete('/api/logout')
def logout():
    session.pop('user_id')  # Remove the user ID from the session on logout
    return {}, 204

# GET LISTINGS
@app.get('/api/items')
def get_items():
    return [i.to_dict() for i in Item.query.all()], 200

# POST LISTINGS
@app.post('/api/items')
def post_items():
    try:
        data = request.json
        new_listing = Item(**data)
        db.session.add(new_listing)
        db.session.commit()
        return jsonify( new_listing.to_dict() ), 201
    except Exception as e:
        return jsonify( {'error': str(e)} ), 406

@app.patch('/api/items/<int:id>')
def patch_items(id):
        items = db.session.query(Item.id == id).first()
        if items:
            items.item_name = request.json.get('title')
            items.description = request.json.get('description')
            items.price = request.json.get('price')
        else:
            return {'error': 'Not found'}, 404


# DELETE AND PATCH
@app.delete('/api/items/<int:id>')
def delete_items(id):
    try:
        user = User.query.where(User.id == session.get('user_id')).first()
        item = Item.query.where(Item.id == id).first()
        if item.seller_id == user.id:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message':'your item has been deleted'}), 204
        else:
            return {'error': 'you are not authorized'}, 404
    except Exception as e:
        return jsonify( {'error': str(e)} ), 406

# GET COMMENTS
@app.get('/api/comments')
def get_comments():
    return [c.to_dict() for c in Comment.query.all()], 200

@app.get('/api/items/<int:item_id>/comments')
def get_comments_by_item_id(item_id):
    item = Item.query.get(item_id)
    if item:
        comments = Comment.query.filter_by(item_id=item_id).all()
        return [comment.to_dict() for comment in comments], 200
    else:
        return {'error': 'Item not found'}, 404

# POST COMMENTS
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

@app.post('/api/cart')
def add_to_cart():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'User not logged in'}), 401
        
        data = request.json
        item_id = data['item_id']
        quantity = data.get('quantity', 1)

        cart_item = Cart.query.filter_by(user_id=user_id, item_id=item_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = Cart(user_id=user_id, item_id=item_id, quantity=quantity)
            db.session.add(cart_item)
        
        db.session.commit()
        return jsonify(cart_item.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 406

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

@app.delete('/api/cart/<int:item_id>')
def remove_from_cart(item_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'User not logged in'}), 401

        cart_item = Cart.query.filter_by(user_id=user_id, item_id=item_id).first()
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return {}, 204
        else:
            return jsonify({'error': 'Item not found in cart'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 406

@app.post('/api/items/<int:id>/buy')
# @login_required
def buy_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
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

#!/usr/bin/env python3
import os
from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt


from models import db, User, Item, Order, Comment

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
        # first_name = User(first_name = request.json['first_name'])
        # last_name = User(last_name = request.json['last_name'])
        new_user = User(username=request.json['username'], first_name = request.json['first_name'], last_name = request.json['last_name'])
        new_user._hashed_password = bcrypt.generate_password_hash(request.json['_hashed_password']).decode('utf-8')
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        return new_user.to_dict(), 201
    except Exception as e:
        return { 'error': str(e) }, 406
# SEE WHICH USER IS LOGGED IN
@app.get('/api/get-session')
def get_session():
    user = User.query.where(User.id == session.get('user_id')).first()
    if user:
        return user.to_dict(), 200
    else:
        return {}, 204

# LOGIN AND LOGOUT
@app.post('/api/login')
def login():
    user = User.query.where(User.username == request.json.get('user')).first()
    if user and bcrypt.check_password_hash(user._hashed_password, request.json.get('password')):
        session['user_id'] = user.id
        return user.to_dict(), 201
    else:
        return {'error': 'username or password was not invalid'}, 401

@app.delete('/api/logout')
def logout():
    session.pop('user_id')
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


# DELETE AND PATCH

# GET COMMENTS
@app.get('/api/comments')
def get_comments():
    return [c.to_dict() for c in Comment.query.all()], 200

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


# PATCH AND DELETE COMMENTS
@app.patch('/api/comments/<int:id>')
def patch_comments(id):
    try:
        comment = Comment.query.where(Comment.id == id).first()
        if comment:
            comment.comment = request.json.get('comment')
            db.session.commit()
            return comment.to_dict(), 200
        else:
            return {'error': 'Not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 406

@app.delete('/api/comments/<int:id>')
def delete_comments(id):
    try:
        comment = Comment.query.where(Comment.id == id).first()
        if comment:
            db.session.delete(comment)
            db.session.commit()
            return {}, 204
        else:
            return {'error': 'Not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 406

# write your routes here! 
# all routes should start with '/api' to account for the proxy


if __name__ == '__main__':
    app.run(port=5555, debug=True)

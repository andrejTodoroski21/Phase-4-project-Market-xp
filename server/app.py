#!/usr/bin/env python3
import os
from flask import Flask, request
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
        new_user = User(username=request.json['username'])
        new_user._hashed_password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
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

# LOGIN AND LOGOUT
@app.post('/api/login')
def login():
    User.query.where(User.username == request.json.get('username')).first()
    if user and bcrypt.check_password_hash(user._hashed_password, request.json('password')):
        session['user_id'] = user.id
        return user.to_dict(), 201
    else:
        return {'error': 'username or password was not invalid'}, 401



@app.delete('/api/logout')
def logout():
    session.pop('user_id')
    return {}, 204


# write your routes here! 
# all routes should start with '/api' to account for the proxy


if __name__ == '__main__':
    app.run(port=5555, debug=True)

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from models import User
from extensions import db
import os

auth_bp = Blueprint('auth', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            ah = request.headers['Authorization']
            if ah.startswith('Token '):
                token = ah.split(" ")[1]
        if not token:
            return jsonify({'message': 'token missing'}), 401
        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            cu = User.query.filter_by(id=data['user_id']).first()
            
        except jwt.InvalidTokenError:
            return jsonify({'message': 'token invalid'}), 401
        return f(cu, *args, **kwargs)
    return decorated

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing required fields'}), 400
    hashed_password = generate_password_hash(data['password'])
    new_us = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )
    db.session.add(new_us)
    db.session.commit()
    
    return jsonify({'message': 'created user '}), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'username and password missing'}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, os.getenv('SECRET_KEY'))
        
        return jsonify({'token': token})
    return jsonify({'message': 'password invalid'}), 401
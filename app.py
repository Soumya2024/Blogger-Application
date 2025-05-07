from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
from extensions import db, migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)

from models import User, Post, Comment

@app.before_request
def create_tables():
    if not os.path.exists('database.db'):
        db.create_all()

from auth import auth_bp
from blog import blog_bp
from comment import comment_bp

app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(comment_bp)
        
        
if __name__ == '__main__':
    app.run(debug=True)
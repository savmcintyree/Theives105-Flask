from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# create Models based off our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='Author', lazy=True)

db = SQLAlchemy()

# create Models based off of our ERD
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    img_url = db.Column(db.String)
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import relationship
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fio = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    date_of_birth = db.Column(db.String(140))
    last_seen = db.Column(
        db.DateTime, server_default=func.utcnow(), default=datetime.utcnow
    )
    phone_number = db.Column(db.String(128))
    position = db.Column(db.String(128))
    passwords = db.relationship("UserPasswords", backref="user_pswd", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"

    def __repr__(self):
        return f"<User {self.username}>"


class UserPasswords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_ais = db.Column(db.String(128))
    password_pvd = db.Column(db.String(128))
    password_enter = db.Column(db.String(128))
    password_mail = db.Column(db.String(128))
    password_home = db.Column(db.String(128))
    password_delo = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Toner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    printers_name = db.Column(db.String(20), index=True, unique=True)
    printers_toner = db.Column(db.String(20), index=True, unique=True)
    created_at = db.Column(
        db.DateTime, server_default=func.utcnow(), default=datetime.utcnow, index=True
    )

    def __repr__(self):
        return f"<Toner {self.printers_name}>"


class PhoneBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(120))
    position = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    organization = db.Column(db.String(120))

    def __repr__(self):
        return f'<Contact {self.fio}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


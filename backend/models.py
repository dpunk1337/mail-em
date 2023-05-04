from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from backend import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(32), unique=True, nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_email_verified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return (self.password == password)


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(64), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.TIMESTAMP, default=datetime.utcnow)


class UserMailMap(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mail_id = db.Column(db.Integer, db.ForeignKey('mail.id'), nullable=False)
    status = db.Column(db.String(16), nullable=False)
    scheduled_date = db.Column(db.DATE)

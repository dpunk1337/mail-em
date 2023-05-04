from datetime import datetime, time
from typing import List
from sqlalchemy import and_, not_

from backend.models import User, Mail, UserMailMap
from backend.database import db


class UserDao:
    @staticmethod
    def add_user(email: str, first_name: str, last_name: str, password: str, is_admin: bool=False, is_email_verified: bool=False):
        new_user = User(email=email, first_name=first_name, last_name=last_name, password=password, is_admin=is_admin, is_email_verified=is_email_verified)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get_users_not_admin(id_to_exclude: int) -> List[User]:
        return User.query.filter(and_(User.is_admin == False, not_(User.id == id_to_exclude))).all()

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()


class MailDao:
    @staticmethod
    def add_mail(subject: str, message: str):
        today=datetime.today()
        new_mail = Mail(subject=subject, message=message, created_on=today)
        db.session.add(new_mail)
        db.session.commit()
        return new_mail

class UserMailMapDao:
    @staticmethod
    def add_user_mail_map(sender_id: int, receiver_id: int, mail_id: int, status: str, scheduled_date: datetime):
        new_map = UserMailMap(sender_id=sender_id, receiver_id=receiver_id, mail_id=mail_id, status=status, scheduled_date=scheduled_date)
        db.session.add(new_map)
        db.session.commit()

    @staticmethod
    def get_mails_sent_on_date_with_status(scheduled_date: datetime, status: str) -> int:
        return UserMailMap.query.filter(
            and_(UserMailMap.status == status, UserMailMap.scheduled_date == scheduled_date)).count()
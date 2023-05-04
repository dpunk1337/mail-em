from datetime import datetime, time
from flask import Flask
from flask_mail import Mail as Mailer, Message
from apscheduler.schedulers.blocking import BlockingScheduler
from backend.models import User, Mail, UserMailMap
from config import Config
from backend.database import db
import pytz

scheduler = BlockingScheduler(timezone=pytz.timezone('Asia/Kolkata'))
app = Flask(__name__)
app.config.from_object(Config)
mail = Mailer(app)
db.init_app(app)


@scheduler.scheduled_job('cron', hour=8, minute=0, second=0)
def send_scheduled_mails():
    with app.app_context():
        today = datetime.today().date()
        user_mail_maps = UserMailMap.query.filter_by(status='SCHEDULED', scheduled_date=today).all()
        for user_mail_map in user_mail_maps:
            sender = User.query.get(user_mail_map.sender_id)
            receiver = User.query.get(user_mail_map.receiver_id)
            mail_data = Mail.query.get(user_mail_map.mail_id)
            msg = Message(mail_data.subject, recipients=[receiver.email], body=mail_data.message)
            msg.sender = sender.email
            mail.send(msg)
            user_mail_map.status = 'SENT'
            db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    scheduler.start()
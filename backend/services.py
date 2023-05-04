from backend.daos import UserDao, MailDao, UserMailMapDao
from datetime import datetime, timedelta


class UserService:

    @staticmethod
    def add_user(user):
        return UserDao.add_user(user['email'], user['first_name'], user['last_name'], user['password'], user['is_admin'])

    @staticmethod
    def get_user_by_email(email):
        return UserDao.get_user_by_email(email)

    @staticmethod
    def check_if_email_taken(email):
        existing_user = UserService.get_user_by_email(email)
        return False if existing_user is None else True

    @staticmethod
    def check_if_user_exists(user):
        return UserService.check_if_email_taken(user.email)

    @staticmethod
    def check_password(user, password):
        return user.check_password(password)

    @staticmethod
    def get_all_other_normal_users(user):
        UserDao.get_users_not_admin(user.id)


class MailService:

    @staticmethod
    def schedule_mail(user, mail, receiver):
        mail = MailDao.add_mail(mail['subject'], mail['message'])
        UserMailMapDao.add_user_mail_map(user.id, receiver.id, mail.id, 'SCHEDULED', (datetime.today()+timedelta(days=1)).date())

    @staticmethod
    def get_number_of_scheduled_mails():
        return UserMailMapDao.get_mails_sent_on_date_with_status(datetime.today().date(),'SCHEDULED')

    @staticmethod
    def get_number_of_sent_mails():
        return UserMailMapDao.get_mails_sent_on_date_with_status(datetime.today().date(),'SENT')

    @staticmethod
    def get_number_of_opened_mails():
        return UserMailMapDao.get_mails_sent_on_date_with_status(datetime.today().date(),'OPENED')
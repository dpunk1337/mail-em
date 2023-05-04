from flask import Flask
from flask_login import LoginManager
from config import Config, TestConfig
from backend.database import db
from backend.models import *
from flask_mail import Mail as MailService

login_manager = LoginManager()
mail_service = MailService()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    login_manager.login_view = 'authentication.login'

    db.init_app(app)
    login_manager.init_app(app)
    mail_service.init_app(app)

    from backend import main_view
    from backend.controllers import authentication_controller, user_controller, analytics_controller, mail_controller
    app.register_blueprint(main_view.bp)
    app.register_blueprint(authentication_controller.bp)
    app.register_blueprint(user_controller.bp)
    app.register_blueprint(analytics_controller.bp)
    app.register_blueprint(mail_controller.bp)

    with app.app_context():
        db.create_all()
        create_admin_user()

    return app

def create_test_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    login_manager.login_view = 'authentication.login'

    db.init_app(app)
    login_manager.init_app(app)

    from backend.controllers import authentication_controller
    app.register_blueprint(authentication_controller.bp)

    return app


def create_admin_user():
    admin_user_details = {'first_name': 'admin', 'last_name': 'admin', 'email': 'admin@admin.admin', 'password': 'admin', 'is_admin': 1}
    existing_admin_user = db.session.query(User).filter(
        (User.email == admin_user_details['email'])).first()
    if not existing_admin_user:
        admin_user = User(first_name=admin_user_details['first_name'],
                          last_name=admin_user_details['last_name'],
                          email=admin_user_details['email'],
                          password=admin_user_details['password'],
                          is_admin=admin_user_details['is_admin'])
        db.session.add(admin_user)
        db.session.commit()
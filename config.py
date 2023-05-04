class Config:
    SECRET_KEY = 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    DEBUG = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '465'
    MAIL_USERNAME = 'company.email.id'
    MAIL_PASSWORD = 'company.email.password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class TestConfig:
    SECRET_KEY = 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    TESTING = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '465'
    MAIL_USERNAME = 'company.email.id'
    MAIL_PASSWORD = 'company.email.password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
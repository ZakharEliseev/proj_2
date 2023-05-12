import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
salt = secrets.token_hex(16)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECURITY_PASSWORD_SALT = salt
    # SECURITY_REGISTERABLE = True
    # SECURITY_SEND_REGISTER_EMAIL = False
    # SECURITY_RECOVERABLE = True
    # SECURITY_CHANGEABLE = True
    # SECURITY_EMAIL_SENDER = 'zelibelmfc@mail.ru'
    # SECURITY_EMAIL_SUBJECT_REGISTER= 'Сайт МФЦ'
    # SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = 'Сброс пароля от сайта МФЦ'
    # MAIL_SERVER = 'smtp.mail.ru'
    # MAIL_PORT = 587
    # MAIL_USERNAME = 'zelibelmfc@mail.ru'
    # MAIL_PASSWORD = 'u1fuschn'
    # MAIL_DEFAULT_SENDER = 'zelibelmfc@mail.ru'

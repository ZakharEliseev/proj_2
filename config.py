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
    # время жизни сессии в секундах (в данном случае 12 часов)
    PERMANENT_SESSION_LIFETIME = 12 * 60 * 60
    # обновление времени сессии при каждом запросе
    SESSION_REFRESH_EACH_REQUEST = True

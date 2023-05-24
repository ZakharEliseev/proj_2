from app import db, app
from app.models import User


def main():
    with app.app_context():
        u = User(username='test', email='test@example.com', password_hash='test')
        db.session.add(u)
        db.session.commit()


if __name__ == '__main__':
    main()


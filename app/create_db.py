# from pandas import pandas as pd

# from app import db, app
# from app.models import User
#
#
# def main():
#     with app.app_context():
#         u = User(username='test', email='test@example.com', password_hash='test')
#         db.session.add(u)
#         db.session.commit()
#
#
# if __name__ == '__main__':
#     main()
#
# df = pd.read_excel(open('csv/example.xlsx', 'rb'), sheet_name=1)
#
# print(df)
n = int(input())
res = 123 * n

print(res)
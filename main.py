from os import getenv

from app.sql.flask.flask import FlaskApp


db_uri = 'postgresql://postgres:tunaxx@localhost:5432/UserData'

def main():
    app = FlaskApp(db_uri)
    app.set_user({'login': '12', 'password': '123'})
    print(app.get_user({'login': '12'}))


if __name__ == '__main__':
    print('Hello, Duck!')
    main()

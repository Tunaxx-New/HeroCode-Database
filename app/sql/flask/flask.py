from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from app import App
from app.models import User


class FlaskApp(App):
    """
    FlaskApp - Data app based on Flask SQL Alchemy library
    """

    def __init__(self):
        super().__init__('FlaskSQLAlchemy')
        self.socketio = SocketIO(self.app)
        self.socketio.run(self.app, host=self.data['host'], port=self.data['port'], debug=self.data['debug'],
                          allow_unsafe_werkzeug=True)

    def initialize(self):
        """
        Initialize database flask app with properties
        Creates All database models in python class view
        """

        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.uri
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)

        self.User = type("User", (self.db.Model, ), {
            '__tablename__': 'users',
            User.id: self.db.Column(self.db.Integer, primary_key=True),
            User.login: self.db.Column(self.db.String(128), unique=True, nullable=False),
            User.password: self.db.Column(self.db.String(128), unique=False, nullable=False)
        })

        @self.app.route('/')
        def main():
            self.set_user({'login': '12', 'password': '12'})
            return str(self.get_user({'login': '12'}))

    def get_user(self, filter_by: dict) -> dict:
        """
        Find the user in user table

        :param: filter: dict - search filter ({COLUMN_NAME: FIND_VALUE})

        :return: dict -> user columns and their values
        """
        key = list(filter_by.keys())[0]
        value = list(filter_by.values())[0]
        user = self.User.query.filter(self.User.__dict__[key] == value).first()
        return user.__dict__ if user is not None else user

    def set_user(self, data: dict):
        """
        Register the new user in users table

        :param: filter: dict - user data [login, password]
        """
        if self.db.session.query(self.User.id).filter_by(login=data['login']).first() is None:
            user = self.User(login=data['login'], password=data['password'])
            self.db.session.add(user)
            self.db.session.commit()

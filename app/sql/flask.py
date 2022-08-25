from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from app import App
from duck_override import gaggle
from duck_override import quack


class FlaskApp(App):
    """
    FlaskApp - Data app based on Flask SQL Alchemy library
    """

    def __init__(self, uri: str):
        """
        Initialize the flask app and creates flask_sqlalchemy database

        :param uri: str
        """
        super().__init__()
        try:
            self.app = Flask(__name__)
            self.app.config['SQLALCHEMY_DATABASE_URI'] = uri
            self.db = SQLAlchemy(self.app)
        except Exception as e:
            gaggle(str(e))
        else:
            quack("Flask app with alchemy is set!")

from app.sql.flask.flask import FlaskApp
from util.load_env import load_env
from duck_override import quack


def main():
    load_env()
    FlaskApp()
    # Code after is working only when server closes!


if __name__ == '__main__':
    quack('Hello, Duck!')
    main()

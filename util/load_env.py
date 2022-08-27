import os
from dotenv import load_dotenv
from duck_override import purr


def load_env() -> bool:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        return True
    load_dotenv()
    purr('.env file not found! Make sure that you loaded useful environment variables!')
    return False

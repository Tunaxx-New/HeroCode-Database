from abc import ABC
from abc import abstractmethod
from os import getenv

from duck_override import gaggle
from duck_override import quack


class App(ABC):
    """
    App - base class for creating database app.
    Contains standard database variables and methods

    Main realization is IO to/from Host the structured data
    """

    @abstractmethod
    def get_user(self,  filter_by: dict) -> dict:
        pass

    @abstractmethod
    def set_user(self, data: dict):
        pass

    @abstractmethod
    def initialize(self):
        pass

    def __init__(self, name: str):
        """
        Initialize database app with catching exceptions
        Fill uri field with environment variables

        :param: uri: str - uri to database
        :param: name: str - name of database type
        """

        db_data = {
            'type': getenv('DATABASE_TYPE'),
            'user': getenv('DATABASE_USER'),
            'password': getenv('DATABASE_PASSWORD'),
            'host': getenv('DATABASE_HOST'),
            'port': getenv('DATABASE_PORT'),
            'name': getenv('DATABASE_NAME')
        }
        self.db_data_safe = {
            'type': db_data['type'],
            'host': db_data['host'],
            'port': db_data['port']
        }
        self.data = {
            'host': getenv('HOST'),
            'port': getenv('PORT'),
            'debug': getenv('DEBUG')
        }

        if None in db_data:
            gaggle('There is no database connection info in environment variables!\n'
                   'Please create env.vars such a'
                   '\'DATABASE_\' + [\'TYPE\', \'USER\', \'PASSWORD\', \'HOST\', \'PORT\', \'NAME\']')
            self.uri = None
        else:
            self.uri = db_data['type'] + '://' + db_data['user'] + ':' + db_data['password'] + \
                       '@' + db_data['host'] + ':' + db_data['port'] + '/' + db_data['name']
        self.app = None
        self.db = None

        # Models
        self.User = None

        try:
            self.initialize()
        except Exception as e:
            gaggle(str(e))
        else:
            quack("%s app with alchemy is set on %s!"
                  % (name,
                     self.db_data_safe['type'] + '://' + self.db_data_safe['host'] + ':' + self.db_data_safe['port']))

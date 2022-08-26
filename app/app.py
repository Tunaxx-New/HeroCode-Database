from abc import ABC
from abc import abstractmethod

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

    def __init__(self, uri: str, name: str):
        """
        Initialize database app with catching exceptions

        :param: uri: str - uri to database
        :param: name: str - name of database type
        """
        self.uri = uri
        self.app = None
        self.db = None

        # Models
        self.User = None

        try:
            self.initialize()
        except Exception as e:
            gaggle(str(e))
        else:
            quack("%s app with alchemy is set on %s!" % (name, self.uri))

from abc import ABC


class App(ABC):
    """
    App - base class for creating database app.
    Contains standard database variables and methods

    Main realization is IO to/from Host the structured data
    """

    def __init__(self):
        """
        Create standard database fields
        """
        self.app = None
        self.db = None
        self.uri = None

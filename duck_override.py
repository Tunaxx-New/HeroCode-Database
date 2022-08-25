def dive():
    """
    Your duck is dive or fly away, say goodbye!
    """
    print('Bye, quack!')
    quit()


def quack(message: str):
    """
    Standard message from duck.

    :param message: str
    """
    print('quack: ' + message)


def purr(message: str):
    """
    Warning, purr is not good sign. Duck does not trust you...

    :param message: str
    """
    print('purr!: ' + message)


def gaggle(message: str):
    """
    Error, important message from duck, or quack for help!!!

    :param message: str
    """
    print('gaggle!!!: ' + message)

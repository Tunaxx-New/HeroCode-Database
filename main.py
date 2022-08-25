from os import getenv


from duck_override import dive


def main():
    host = getenv('HOST')
    port = getenv('PORT')
    debug = getenv('DEBUG')

    if None in [host, port, debug]:
        print('One of (Host, Port, Debug) value is not set!')
        dive()


if __name__ == '__main__':
    print('Hello, Duck!')
    main()

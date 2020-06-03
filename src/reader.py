import os


def get_values():
    try:
        APP_SETTINGS = os.getenv('username')
        print('Application settings is {}'.format(APP_SETTINGS))
    except KeyError as ex:
        print('Key error: {}'.format(ex))


get_values()

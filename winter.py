import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def load():
    config_exists_check()

    if 'WINTER' not in config:
        setup()


def setup():
    api = input("Write your OWM API key > ")
    city = input("What is your city? > ")
    config['WINTER'] = {'api': api,
                        'city': city
                        }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def config_exists_check():
    try:
        file = open("config.ini")
    except FileNotFoundError:
        file = open("config.ini", "w")
    file.close()
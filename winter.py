import configparser

config = configparser.ConfigParser()

def setup():
    lang = input("> ")
    config['WINTER'] = {'lang': lang}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def load():
    if 'winter' not in config:
        setup()


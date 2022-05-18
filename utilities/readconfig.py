import configparser

config = configparser.RawConfigParser()
config.read(r'.\configs\config.ini')

class ReadConfig:
    @staticmethod
    def get_app_url():
        return config.get('common info', 'url')

    @staticmethod
    def get_valid_username():
        return config.get('common info', 'valid_username')

    @staticmethod
    def get_valid_password():
        return config.get('common info', 'valid_password')

    @staticmethod
    def get_firstname():
        return config.get('common info', 'firstname')
    
    @staticmethod
    def get_lastname():
        return config.get('common info', 'lastname')

    @staticmethod
    def get_zipcode():
        return config.get('common info', 'zipcode')
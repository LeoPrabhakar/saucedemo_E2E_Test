import configparser

config = configparser.RawConfigParser()
config.read("Saucedemo_new_E2E_test\\configurations\\config.ini")


class Read_Config_File:
    @staticmethod
    def get_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_product_link_text():
        product_name = config.get('common info', 'product_name')
        return product_name

    @staticmethod
    def get_first_name():
        first_name = config.get('common info', 'first_name')
        return first_name

    @staticmethod
    def get_last_name():
        last_name = config.get('common info', 'last_name')
        return last_name

    @staticmethod
    def get_pin_code():
        pin_code = config.get('common info', 'pin_code')
        return pin_code

    @staticmethod
    def get_products():
        products = [config['products'][key] for key in config['products'].keys()]
        return products
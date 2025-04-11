import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\routb\PycharmProjects\noop_commerce\Configurations\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        URL = config.get('common info', 'baseURL')
        return URL

    @staticmethod
    def getUseremail():
        mailid = config.get('common info', 'useremail')
        return mailid

    @staticmethod
    def getPassword():
        Password = config.get('common info', 'password')
        return Password

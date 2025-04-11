import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log",
                            format='%(asctime)s: %(message)s',
                            datefmt='%m%d%y %I:%M:%S %p',
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

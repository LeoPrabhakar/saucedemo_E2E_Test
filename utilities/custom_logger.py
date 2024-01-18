import logging


class Log_Gen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="Saucedemo_new_E2E_test/logs/automation.log",
                            format="%(asctime)s - %(levelname)s - %(message)s",
                            datefmt="%m%d%Y %I:%M:%S %p"
                            )
                            # level= logging.DEBUG)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

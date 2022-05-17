import logging
import sys


class LoggingMeta(type):
    def __init__(cls, *args, **kwargs):
        stdout_handler = (logging.StreamHandler(sys.stdout),)
        cls._logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO, handlers=stdout_handler,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        super().__init__(*args, **kwargs)

    @property
    def logger(cls) -> logging.Logger:
        return cls._logger


class Logging(metaclass=LoggingMeta):

    @staticmethod
    def info(message):
        Logging._log(message, level=logging.INFO)

    @staticmethod
    def debug(message):
        Logging._log(message, level=logging.DEBUG)

    @staticmethod
    def error(message):
        Logging._log(message, level=logging.ERROR)
        
    @staticmethod
    def _log(message: str, level: int = logging.INFO):
        Logging.logger.log(level, message)

import logging
import sys


class LoggingMeta(type):
    def __init__(cls, *args, **kwargs):
        stdout_handler = (logging.StreamHandler(sys.stdout),)
        cls.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.INFO, handlers=stdout_handler,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        super().__init__(*args, **kwargs)


class Logging(metaclass=LoggingMeta):
    pass

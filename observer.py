import logging
import os
from pathlib import Path
from time import time, sleep
from typing import Type

from log import Logging
from worker import SPICEWorker


class DirUpdatesObserver(Logging):

    def __init__(self, worker_class: Type[SPICEWorker], dir: Path, suffix: str):
        self._worker_class = worker_class
        if not suffix.startswith('.'):
            self.logger.log(logging.ERROR, 'Suffix must starts with "."')
            raise ValueError
        if not dir.exists():
            self.logger.log(logging.ERROR, 'The directory %s does not exists' % dir)
            raise ValueError
        self._dir = dir

    def get_dir_updates(self):
        max_time = time()
        while True:
            for file in self._dir.iterdir():
                if not file.suffix == '.vv':
                    continue
                file_mtime = os.path.getmtime(file.absolute())
                if file_mtime > max_time:
                    max_time = file_mtime
                    yield file.absolute()
            sleep(1)

    def listen(self):
        self.logger.log(logging.INFO, 'Listening %s directory has been started' % self._dir)
        try:
            for filename in self.get_dir_updates():
                worker = self._worker_class(filename=filename)
                worker.start()
        except (Exception, KeyboardInterrupt) as e:
            self.logger.log(logging.ERROR, 'Listening %s has been raised with exception: %s' % (self._dir, e))
        finally:
            self.logger.log(logging.INFO, 'Listening %s directory has been stopped' % self._dir)

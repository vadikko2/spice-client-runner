import logging
from threading import Thread
import subprocess
from pathlib import Path

from log import Logging


class SPICEWorker(Thread, Logging):
    COMMAND = ['remote-viewer', ]

    def __init__(self, filename: Path):
        super().__init__()
        self._filename = filename
        self._cmd = SPICEWorker.COMMAND + [str(self._filename), ]

    def __repr__(self):
        return '%s (%s)' % (self.name, self.cmd)

    @property
    def cmd(self):
        return ' '.join(map(str, self._cmd))

    def run(self) -> None:
        try:
            self.info('%s started' % self)
            process = subprocess.Popen(self._cmd)
            process.communicate()
            # keep checking stdout/stderr until the child exits
            while process.poll() is None:
                self.check_io(process)

            return process.returncode
        finally:
            self.info('%s stopped' % self)

    @staticmethod
    def check_io(process):
        while True:
            output = process.stdout.readline().decode()
            if output:
                SPICEWorker.info(output)
            else:
                break

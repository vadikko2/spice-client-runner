from pathlib import Path

from observer import DirUpdatesObserver
from worker import SPICEWorker
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Set params:'
    )
    parser.add_argument(
        '-d', '--dir', type=str,
        help='Working directory. By default "~/Downloads"',
        default=Path.home() / Path('Downloads')
    )
    parser.add_argument(
        '-s', '--suffix', type=str,
        help='SPICE file suffix. By default ".vv"',
        default='.vv'
    )
    args = parser.parse_args()
    dir_ = Path(args.dir)
    suffix = args.suffix
    observer = DirUpdatesObserver(worker_class=SPICEWorker, dir=dir_, suffix=suffix)
    observer.listen()

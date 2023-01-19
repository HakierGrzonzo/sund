import logging
from argparse import ArgumentParser

from .client import run_app
from .deamon import run_deamon

logging.basicConfig(level=logging.INFO)


def main():
    parser = ArgumentParser("sund")
    parser.add_argument(
        "-d", "--deamon", action="store_true", help="Start sund deamon"
    )
    args = parser.parse_args()
    if args.deamon:
        run_deamon()
    else:
        run_app()


if __name__ == "__main__":
    main()

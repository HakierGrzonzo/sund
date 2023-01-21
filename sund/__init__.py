import asyncio
import logging
from argparse import ArgumentParser

from .client import run_app
from .deamon import run_deamon

logging.basicConfig(level=logging.INFO)


def main():
    parser = ArgumentParser("sund")
    subparsers = parser.add_subparsers(
        help="Mode of operation", required=True, dest="mode"
    )
    deamon_parser = subparsers.add_parser("deamon")
    deamon_parser.add_argument("--bias", type=int, default=10, dest="bias")

    client_parser = subparsers.add_parser("client")
    client_commands = client_parser.add_subparsers(
        help="Command to execute", required=True, dest="command"
    )
    client_commands.add_parser("get_bias")
    client_commands.add_parser("get_brightness")
    set_bias = client_commands.add_parser("set_bias")
    set_bias.add_argument("value", type=int)
    args = parser.parse_args()
    if args.mode == "deamon":
        run_deamon(args.bias)
    else:
        asyncio.run(run_app(args))


if __name__ == "__main__":
    main()

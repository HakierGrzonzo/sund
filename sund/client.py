from socpi import Client

from .app import app

client = Client(app)


async def run_app(args):
    command = args.command
    if command == "get_bias":
        print(await client.get_bias())
    elif command == "set_bias":
        print(await client.set_bias(args.value))
    elif command == "get_brightness":
        print(await client.get_desired_brightness())

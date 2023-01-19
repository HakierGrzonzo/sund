import asyncio

from socpi import Client

from .app import app

client = Client(app)


def run_app():
    print(asyncio.run(client.get_desired_brightness()))

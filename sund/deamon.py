import asyncio
from datetime import timedelta

from sund.utils import run_every

from .app import app, store


async def set_brightness():
    async for _ in run_every(timedelta(seconds=15)):
        print("hewwo", store.bias)


async def deamon_runner():
    await asyncio.gather(set_brightness(), app.run())


def run_deamon():
    asyncio.run(deamon_runner())

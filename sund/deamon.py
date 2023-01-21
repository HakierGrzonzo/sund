import asyncio
import logging
from datetime import timedelta

from sund.utils import calculate_brightness, run_every, set_brightness

from .app import app, store

logger = logging.getLogger(__name__)


async def update_brightness():
    async for _ in run_every(timedelta(seconds=15)):
        current_brightness = calculate_brightness() + store.bias
        if current_brightness != store.last_brightness:
            await set_brightness(current_brightness)
            store.last_brightness = current_brightness


async def deamon_runner():
    await asyncio.gather(update_brightness(), app.run())


def run_deamon(initial_bias: int):
    store.bias = initial_bias
    asyncio.run(deamon_runner())

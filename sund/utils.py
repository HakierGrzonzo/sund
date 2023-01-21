import asyncio
import logging
import math
from datetime import datetime, timedelta

from suntime import Sun

logger = logging.getLogger(__name__)

LATITUDE = 50.32
LONGITUDE = 18.83


async def run_every(value: timedelta):
    seconds = value.total_seconds()
    while True:
        yield
        await asyncio.sleep(seconds)


async def set_brightness(value: int):
    logger.info(f"Setting brightness to {value}")
    proc = await asyncio.create_subprocess_shell(f"brightness.sh {value}")
    await proc.wait()
    if ret := proc.returncode:
        logger.error(
            f"Failed to set the brightness, command exited with code {ret}"
        )


def get_brightness(sunrise: float, sunset: float, aggressiveness: float):
    def transform(time: float, sun_time: float):
        return aggressiveness * (time - sun_time)

    return (
        lambda time: (
            math.atan(transform(time, sunrise))
            - math.atan(transform(time, sunset))
        )
        / math.pi
    )


def calculate_brightness():
    sun = Sun(LATITUDE, LONGITUDE)
    sunrise = sun.get_sunrise_time()
    sunset = sun.get_sunset_time()

    now = datetime.utcnow().astimezone()
    start_of_today = now.replace(second=0, minute=0, hour=0, microsecond=0)

    sunrise_seconds = (sunrise - start_of_today).total_seconds()
    sunset_seconds = (sunset - start_of_today).total_seconds()
    now_seconds = (now - start_of_today).total_seconds()

    brightness_function = get_brightness(sunrise_seconds, sunset_seconds, 2)
    return round(brightness_function(now_seconds) / 3 * 100)

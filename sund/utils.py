import asyncio
from datetime import datetime, timedelta

from suntime import Sun

LATITUDE = 50.32
LONGITUDE = 18.83


async def run_every(value: timedelta):
    seconds = value.total_seconds()
    while True:
        yield
        await asyncio.sleep(seconds)


def calculate_brightness():
    sun = Sun(LATITUDE, LONGITUDE)
    now = datetime.now()
    if (
        sun.get_local_sunrise_time().timestamp()
        < now.timestamp()
        < sun.get_sunset_time().timestamp()
    ):
        return "day"
    return "night"

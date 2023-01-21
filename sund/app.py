from dataclasses import dataclass
from os import getuid
from typing import Optional

from socpi import App

from sund.utils import calculate_brightness, set_brightness

app = App(f"/run/user/{getuid()}/sund")


@dataclass
class Store:
    """Stores the state of the application."""

    bias: int
    last_brightness: Optional[int]


store = Store(bias=0, last_brightness=None)


@app.register
async def set_bias(value: int):
    """Sets the `bias` in the state."""
    store.bias = value
    brightness = calculate_brightness() + store.bias
    await set_brightness(brightness)
    store.last_brightness = brightness
    return store.bias


@app.register
def get_bias():
    """Returns the current bias."""
    return store.bias


@app.register
def get_desired_brightness():
    """Returns the desired brightness."""
    return store.last_brightness

from dataclasses import dataclass
from os import getuid

from socpi import App

from sund.utils import calculate_brightness

app = App(f"/run/user/{getuid()}/sund")


@dataclass
class Store:
    """Stores the state of the application."""

    bias: int


store = Store(bias=0)


@app.register
def set_bias(value: int):
    """Sets the `bias` in the state."""
    store.bias = value
    return store.bias


@app.register
def modify_bias(value: int):
    """Adds the `value` to the bias and returns the new bias."""
    store.bias += value
    return store.bias


@app.register
def get_bias():
    """Returns the current bias."""
    return store.bias


@app.register
def get_desired_brightness():
    """Returns the desired brightness."""
    return calculate_brightness()

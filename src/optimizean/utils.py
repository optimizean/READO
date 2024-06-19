# src/optimizean/utils.py

from typing import Optional

import os
import time
import subprocess
from rich.console import Console

from optimizean.config import Parameters


# Exception
class BadRequestError(Exception):
    pass


# clear terminal
def clear_screen(delay: float = 0.3):
    current_os = os.name
    time.sleep(delay)
    if current_os == "nt":  # for Windows
        subprocess.call("cls", shell=True)
    else:  # Unix System
        subprocess.call("clear", shell=True)


# Load a whole configuration data from pypi,
# customized data from src/optimizean/config.py
def load_config():
    return Parameters()


# manual function
def custom_color():
    # color
    config = load_config()
    color_main = config.style.main
    color_sub = config.style.sub
    color_emp = config.style.emp
    return color_main, color_sub, color_emp


# (rich) effect
def typing_effect(console: Console, chars: str, delay: float = 0.01):
    for char in chars:
        console.print(char, end="", style=None)
        time.sleep(delay)
    print()


# -- Later Priority -- #
# Set the constant value of dependency: including 'rich' or not (default=True)
def output(console: Console, text: str, RICH: bool = True, color: Optional[str] = None):
    if RICH:
        if color:
            return console.log(f"[{color}]text[/]")  # colorize
        return console.log(text)  # default color
    return print(text)  # print

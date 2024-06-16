# src/optimizean/utils.py

from typing import Optional

import os
import sys
import toml
import time
import subprocess

from rich.console import Console


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


# read toml file
def load_config(PATH: str = "./pyproject.toml") -> dict:
    with open(PATH, "r") as f:
        return toml.load(f)


# write toml file
def write_config(TEXT: str, PATH: str = "./pyproject.toml") -> None:
    with open(PATH, "w") as f:
        toml.dump(TEXT, f)
        return f


# (rich) effect
def typing_effect(console: Console, chars: str, delay: float = 0.01):

    # color
    color_main = load_config()["color"]["main"]
    color_sub = load_config()["color"]["sub"]
    color_emp = load_config()["color"]["emp"]

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

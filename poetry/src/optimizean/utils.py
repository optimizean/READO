# src/optimizean/utils.py

from typing import Optional

import os
import sys

# import re
import toml  # import tomlib    # python v3.11

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


# -- legacy -- #
# read toml file - toml
def load_config(PATH: str = "./pyproject.toml") -> dict:
    with open(PATH, "r") as f:
        config = toml.load(f)
    return config


# read toml file - tomlib
# def load_config(PATH: str = "../pyproject.toml") -> dict:
#     with open(PATH, "rb") as f:       # not 'r', open in 'rb' type
#         config = tomllib.load(f)
#     return config


# -- unused -- #
# write toml file
# def write_config(TEXT: str, PATH: str = "../pyproject.toml") -> None:
#     with open(PATH, "w") as f:
#         toml.dump(TEXT, f)
#         return f


# manual function
def custom_color():
    # color
    config = load_config()
    color_main = config["custom"]["color"]["main"]
    color_sub = config["custom"]["color"]["sub"]
    color_emp = config["custom"]["color"]["emp"]
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

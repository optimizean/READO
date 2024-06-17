# src/optimizean/utils.py

from typing import Optional

import os
import sys
import re
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
# read toml file
# def load_config(PATH: str = "../pyproject.toml") -> dict:
#     with open(PATH, "r") as f:
#         return toml.load(f)

# -- unused -- #
# # write toml file
# def write_config(TEXT: str, PATH: str = "../pyproject.toml") -> None:
#     with open(PATH, "w") as f:
#         toml.dump(TEXT, f)
#         return f


# read toml file
# -- Parse Value in `toml` -- #
def str_parser(value):
    if value.startswith(("'", '"')) and value.endswith(("'", '"')):
        return value.strip("'\"")
    raise ValueError(f"Not A Valid Value: {value} ({type(value)})")


def num_parser(value):
    if re.match(r"^\d+$", value):
        return int(value)
    elif re.match(r"^\d+\.\d+$", value):
        return float(value)
    raise ValueError(f"Not A Valid Value: {value} ({type(value)})")


def list_parser(value):
    if value.startswith("[") and value.endswith("]"):
        items = value.strip("[],").split(",")
        return [str_parser(item.strip()) for item in items]
    raise ValueError(f"Not A Valid Value: {value} ({type(value)})")


def dict_parser(value):
    if value.startswith("{") and value.endswith("}"):
        items = re.findall(r'(\w+)\s*=\s*"([^"]+)"', value)
        return {key: val for key, val in items}
    raise ValueError(f"Not A Valid Value: {value} ({type(value)})")


def set_nested_dict(d, keys, value):
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


def load_config(PATH: str = "pyproject.toml") -> dict:
    """
    Read `pyproject.toml` File without other packages
    """
    with open(PATH, "r") as file:
        lines = file.readlines()

    metadata = {}
    current_section = []

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        # Parse Section header
        section_match = re.match(r"\[(.+)\]", line)
        if section_match:
            current_section = section_match.group(1).split(".")
            set_nested_dict(metadata, current_section, {})
            continue

        # Parse Key:Value
        if current_section:
            match_str = re.match(r"(\w+)\s*=\s*(.+)", line)
            if match_str:
                key, value = match_str.groups()
                if value.startswith("[") and value.endswith("]"):
                    value = list_parser(value.strip())
                elif value.startswith("{") and value.endswith("}"):
                    value = dict_parser(value.strip())
                else:
                    value = str_parser(value.strip())
                set_nested_dict(metadata, current_section + [key], value)

    return metadata


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

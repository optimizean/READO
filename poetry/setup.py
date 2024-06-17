# -- setup.py -- #

from setuptools import setup, find_packages

import toml
import time
from rich.console import Console

from src.optimizean.installation import install_dependencies
from src.optimizean.userid import sum_downloads_in_180
from src.optimizean.utils import (
    clear_screen,
    load_config,
    typing_effect,
)  # write_config
from src.optimizean.dependency import ask_requirements, set_requirements
from src.optimizean.localization import greetings, get_location, get_local_greeting
from src.optimizean.contents import contents, readme


# -- unused -- #
# def set_dependencies(console: Console, requirements: list):
#     # Var
#     choice = ask_requirements(console)
#     requires = set_requirements(choice, requirements)
#     # Load a TOML file
#     config = load_config()
#     # Modify values in the config
#     if requires:
#         for requirement in requirements:
#             config["tool"]["poetry"]["dependencies"].update({requirement: "*"})
#     write_config(config)
#     return config


def load_userid() -> int:
    return sum_downloads_in_180()


def installation_process(console: Console) -> bool:
    return install_dependencies(console)


def veritifying_process(console: Console, user_id):
    typing_effect(console, "Verifying user credentials...")
    typing_effect(console, "Authentication successful. ")
    time.sleep(0.5)
    print()
    typing_effect(console, f"Welcome, User no.{user_id}")
    return f"Welcome, User no.{user_id}"


def local_greeting():
    greeting = greetings()
    _, country_code = get_location()
    local_greeting = get_local_greeting(greeting, country_code)

    return local_greeting


def clear(function, *args, PAUSE=0.2):
    print()
    output = function(*args)
    time.sleep(PAUSE)
    clear_screen()
    return output


def main():

    # --- Load toml metadata --- #
    requirements = ["rich", "requests"]
    console = Console()
    clear_screen()

    # 1. Set Dependencies & Installation Process
    # config: dict = clear(set_dependencies, console, requirements)
    # installation_ok: bool = clear(installation_process, console, PAUSE=1)
    user_id: int = load_userid()
    authorized_message: str = clear(veritifying_process, console, user_id, PAUSE=1.5)

    # 2. The main contents
    local_greeting_message: str = local_greeting()
    main_contents: str = contents(console, local_greeting_message)
    code: str = readme(console)


if __name__ == "__main__":
    main()

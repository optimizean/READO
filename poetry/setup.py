# -- setup.py -- #

from setuptools import setup, find_packages

import toml
import time
from rich.console import Console

from src.optimizean.installation import install_dependencies
from src.optimizean.userid import sum_downloads_in_180
from src.optimizean.utils import clear_screen, load_config, write_config, typing_effect
from src.optimizean.dependency import ask_requirements, set_requirements


def set_dependencies(console: Console, requirements: list):

    # Var
    choice = ask_requirements(console)
    requires = set_requirements(choice, requirements)

    # Load a TOML file
    config = load_config()

    # Modify values in the config
    if requires:
        for requirement in requirements:
            config["tool"]["poetry"]["dependencies"].update({requirement: "*"})

    write_config(config)

    return config


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


def process(function, *args, PAUSE=0.2):
    output = function(*args)
    time.sleep(PAUSE)
    clear_screen()
    return output


def main():

    # --- Load toml metadata --- #
    requirements = ["rich", "requests"]
    console = Console()
    clear_screen()

    # 1. Set Dependencies
    config: dict = process(set_dependencies, console, requirements)
    installation_ok: bool = process(installation_process, console, PAUSE=0.6)
    user_id: int = load_userid()
    welcoming_message: str = process(veritifying_process, console, user_id, PAUSE=2)

    # 2. Installation Process


if __name__ == "__main__":
    main()

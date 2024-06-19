# -- setup.py -- #

import time
from rich.console import Console

# from optimizean.installation import install_dependencies
from optimizean.userid import sum_downloads_in_180
from optimizean.utils import clear_screen, typing_effect

from optimizean.localization import get_local_greeting
from optimizean.display import display_rich_contents


def load_userid() -> int:
    return sum_downloads_in_180()


# def installation_process(console: Console) -> bool:
#     return install_dependencies(console)


def veritifying_process(console: Console, user_id):
    typing_effect(console, "Verifying user credentials...")
    typing_effect(console, "Authentication successful. ")
    time.sleep(0.5)
    print()
    typing_effect(console, f"Welcome, User no.{user_id}")
    return f"Welcome, User no.{user_id}"


def clear(function, *args, PAUSE=0.2) -> float:
    function(*args)
    time.sleep(PAUSE)
    clear_screen()
    return PAUSE


def main():

    # --- Load toml metadata --- #
    console = Console()
    clear_screen()

    # 1. Set Dependencies & Installation Process
    user_id: int = load_userid()
    clear(veritifying_process, console, user_id, PAUSE=1.3)

    # 2. The main contents
    # manually change local settings
    customize_location: bool = True
    display_rich_contents(customize_location=customize_location)


if __name__ == "__main__":
    main()

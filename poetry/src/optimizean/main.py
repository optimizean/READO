# -- setup.py -- #

import time
from rich.console import Console

from optimizean.installation import install_dependencies
from optimizean.userid import sum_downloads_in_180
from optimizean.utils import clear_screen, typing_effect

from optimizean.localization import get_local_greeting
from optimizean.contents import display_contents, display_process


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
    local_greeting_message: str = get_local_greeting(
        localtime="morning", country_code="US"
    )
    display_contents(console, local_greeting_message)
    display_process(console)


if __name__ == "__main__":
    main()

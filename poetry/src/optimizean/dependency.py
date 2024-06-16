# poetry/src/optimizean/installation.py

import sys
from typing import List, Union

from rich.console import Console
from rich.prompt import Prompt

from src.optimizean.utils import load_config


def ask_requirements(console: Console) -> str:

    # color
    color_main = load_config()["color"]["main"]
    color_sub = load_config()["color"]["sub"]

    # Permission Message
    console.print(
        f"[{color_main}]Following libraries are needed for awesome experience.[/]"
    )
    console.print(
        f"[{color_main}]These are going to be uninstalled when it is dones[/]"
    )
    console.print(
        f"  - [{color_sub}]rich[/]        : for colorful text in your terminal"
    )
    console.print(f"  - [{color_sub}]requests[/]    : to check your visitor number\n")

    # Proceeding
    console.print(f"[{color_main}]Proceed?[/]")
    options = ["Yes, Proceed. ", "No, Abort."]
    for i, option in enumerate(options, 1):
        console.print(f"  > {i}. {option}")

    # Get User Input
    console.print()
    while True:
        choice = Prompt.ask(
            f"[{color_main}]Enter the number of your choice[/]",
            choices=["1", "2"],
            default="1",
        )
        if choice == "1":
            return choice
        sys.exit()


def set_requirements(choice: str, requirements: list) -> Union[List[str], None]:

    if choice == "1":
        return requirements

    elif choice == "2":
        return None


def main():
    requirements = ["rich", "requests"]
    console = Console()

    choice = ask_requirements(console)
    requires = set_requirements(choice, requirements)
    return requires


if __name__ == "__main__":
    main()

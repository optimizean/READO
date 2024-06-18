# src/optimizean/display.py
import sys

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.align import Align
from rich.layout import Layout

from optimizean.utils import custom_color
from optimizean.contents import contents

color_main, color_sub, color_emp = custom_color()  # color


def rich_introduce(content: str) -> Text:
    return Text(content)


def rich_contact(contents: dict) -> Table:
    # Contact
    contact = Table(
        title=f"\n{contents.get("title")}\n",
        expand=False,
        style=None,
        show_header=False,
        show_edge=False,
    )
    contact.add_column("Method", justify="right")
    contact.add_column("Contact", justify="left")
    contact.add_row("Email", contents.get("email"))
    contact.add_row("Github", contents.get("github"))
    contact.add_row("Blog", contents.get("blog"))

    return contact


def rich_code(console: Console, content: str) -> Panel:
    code = content
    syntax = Syntax(code, "python", theme="github-dark", line_numbers=True)
    panel = Panel(syntax, expand=True)
    console.print(panel)
    return panel


def rich_farewell(console: Console, content: str) -> str:
    return Text(content)


def rich_proceed(content: str) -> str:
    query = content
    choice = Prompt.ask(
        query,
        choices=["y", "n"],
        default="y",
    )
    return choice


def display_contents(
    console: Console, contents: dict, local_greeting_message: str
) -> Panel:

    # Contents
    introduce: Text = contents.get(introduce(local_greeting_message))
    contact: Table = rich_contact(contents.get("contact"))

    # Style
    grid = Table.grid(expand=True)
    grid.add_row(introduce)
    grid.add_row(contact)
    panel = Panel(Align.center(grid, vertical="middle"), padding=2)

    console.print(panel)

    return panel


def display_process(console: Console, contents: dict) -> None:

    while True:
        choice = contents.get("proceed")
        if choice == "y":
            rich_code(console, contents.get("code"))

        rich_farewell(console, contents.get("farewell"))
        sys.exit()


def display_rich_contents(customize_location:bool) -> True:
    console = Console
    contents_dict: dict = contents(customize_location)

    display_process(console, contents_dict)

    return True


if __name__ == "__main__":
    console = Console
    display_rich_contents(customize_location=False)

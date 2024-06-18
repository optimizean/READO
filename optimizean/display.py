# src/optimizean/display.py
import sys

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.align import Align

from optimizean.utils import custom_color
from optimizean.contents import contents

color_main, color_sub, color_emp = custom_color()  # color


# -- Make Contents Rich -- #


def rich_introduce(content: str) -> Text:
    content = Text.from_markup(content)
    return content


def rich_contact(contents: dict) -> Table:
    # Contact
    contact = Table(
        title=f"\n{contents.get('title')}\n",
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


def rich_code(content: str) -> Panel:
    code = content
    syntax = Syntax(code, "python", theme="github-dark", line_numbers=True)
    panel = Panel(syntax, expand=True)
    return panel


def rich_farewell(content: str) -> Text:
    return Text(content)


def rich_proceed(content: str) -> str:
    query = content
    choice = Prompt.ask(
        query,
        choices=["y", "n"],
        default="y",
    )
    return choice


# -- Displaying Module -- #


def display_contents(console: Console, introduce: Text, contact: Table) -> Panel:

    # Style
    grid = Table.grid(expand=True)
    grid.add_row(introduce)
    grid.add_row(contact)
    panel = Panel(Align.center(grid, vertical="middle"), padding=2)

    console.print(panel)

    return panel


def display_rich_contents(customize_location: bool) -> None:
    console = Console()
    contents_dict: dict = contents(customize_location)

    introduce_text: Text = rich_introduce(content=contents_dict.get("introduce"))
    contact_table: Table = rich_contact(contents=contents_dict.get("contact"))
    display_contents(console, introduce_text, contact_table)

    while True:
        choice = rich_proceed(contents_dict.get("proceed"))
        if choice == "y":
            console.print(rich_code(contents_dict.get("code")))

        console.print(rich_farewell(contents_dict.get("farewell")))
        sys.exit()


if __name__ == "__main__":
    console = Console
    display_rich_contents(customize_location=False)

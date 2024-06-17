# src/optimizean/contents.py
import sys

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.align import Align
from rich.layout import Layout

from optimizean.utils import load_config, clear_screen

# color
color_main = load_config()["color"]["main"]
color_sub = load_config()["color"]["sub"]
color_emp = load_config()["color"]["emp"]


def contents_introduce(local_greeting_message: str) -> Text:
    return f"""{local_greeting_message}, Human and Non-Human Visitor! 🤖
This is a proactive Log Keeper and [{color_sub}]Computer Vision engineer, An[/]
Believing greatest asset for developers is the trust and teamworks.
As a [{color_sub}]research-oriented engineer[/], I strive to overcome challenges 
utilize existing technologies and innovative ideas.

Always open to new collaborations!\n"""


def contents_contact(title: str = "\nContact me 💻\n") -> Table:
    f"""
    e.g.,   Contact me 💻

    [{color_main}]Email[/]   | email@gmail.com
    [{color_main}]Github[/]  | github.com/username
    [{color_main}]Blog[/]    | https://blog-address.com
    """
    # Contact
    contact = Table(
        title=title,
        expand=False,
        style=None,
        show_header=False,
        show_edge=False,
    )
    contact.add_column("Method", justify="right")
    contact.add_column("Contact", justify="left")
    contact.add_row("Email", "https://github.com/optimizean")
    contact.add_row("Github", "https://optimizean.github.io/an/")
    contact.add_row("Blog", "optimize.an@gmail.com")

    return contact


def code_contents(console: Console) -> Panel:
    code = """

    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    from an import Educator, Engineer, Researcher, Vision

    class AN(nn.Module):
        def __init__(self):
            super(AN, self).__init__()

            # Role
            self.educator   = Educator(driven = "sharing knowledge")
            self.engineer   = Engineer(driven = "contributing to open-source project")
            self.researcher = Researcher(driven = "engaging with in-depth experience")

            # Currently Focus on
            self.document_understanding = Vision(especially = "table_comprehension")
            self.semantic_segmentation  = Vision(especially = "building previous SOTA for joy")

            self.classifier = nn.Linear(365, 2)

            
        def forward(self, an):
        
            # Tech Stack
            educating   = self.educator(an, volunteering = ["Git", "GitHub/Actions", "Django"])
            engineering = self.engineer(an, prefer = ["PyTorch", "Huggingface", "Wandb"])
            researching = self.researcher(an, experienced = ["LaTeX", "Linux", "Misc."])
            
            inputs = torch.cat((educating, engineering, researching), 1)

            # at This Moment
            novice  = self.document_understanding(inputs)
            interme = self.semantic_segmentation(inputs)

            output = self.classifier((novice, interm))

            return output

            
    hello_world = AN()    

    """

    syntax = Syntax(code, "python", theme="github-dark", line_numbers=True)
    # panel = Panel.fit(syntax)
    panel = Panel(syntax, expand=True)
    console.print(panel)
    return panel


def contents_farewell(console: Console) -> str:
    farewell = f"""
    Thank you for taking time!
    Feel free to contact me. 👋 

    >  https://github.com/optimizean
    >  optimize.an@gmail.com
    
    """
    console.print(farewell)
    return farewell


def display_contents(console: Console, local_greeting_message: str) -> Panel:
    introduce: str = contents_introduce(local_greeting_message)
    contact: Table = contents_contact()

    grid = Table.grid(expand=True)
    grid.add_row(introduce)
    grid.add_row(contact)

    panel = Panel(Align.center(grid, vertical="middle"), padding=2)
    console.print(panel)

    return panel


def display_process(console: Console) -> None:

    color_main = load_config()["color"]["main"]
    color_sub = load_config()["color"]["sub"]
    color_emp = load_config()["color"]["emp"]

    while True:
        choice = Prompt.ask(
            f"[{color_emp}]🔒 New Feature is Released! Why don't you try? [/]",
            choices=["y", "n"],
            default="y",
        )
        if choice == "y":
            code_contents(console)

        contents_farewell(console)

        sys.exit()

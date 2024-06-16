import sys

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.syntax import Syntax

from src.optimizean.utils import load_config, clear_screen

# color
color_main = load_config()["color"]["main"]
color_sub = load_config()["color"]["sub"]
color_emp = load_config()["color"]["emp"]


def contents(console: Console, local_greeting_message: str):
    body = f"""
    {local_greeting_message}, Human and Non-Human Visitor! 🤖   

    This is a self-taught Computer Vision engineer AN.  
    Have a huge interest in what AI can do in a positive way.   
    Looking for oppurtunities to collaborate with various individuals  
    
    Contact me 💻

    Email   : optimize.an@gmail.com
    Github  : https://github.com/optimizean
    Blog    : https://optimizean.github.io/an/
    """

    panel = Panel.fit(Text(body), title="", border_style=color_emp)

    console.print()
    console.print(panel)
    console.print()
    return body


def code_contents(console: Console):
    clear_screen()

    code = """

    
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    from an import Educator, Engineer, Researcher, Vision

    class AN(nn.Module):
        def __init__(self):
            super(AN, self).__init__()

            # Role
            self.educator   = Educator(driven   =   "sharing knowledge")
            self.engineer   = Engineer(driven   =   "contributing to open-source project")
            self.researcher = Researcher(driven =   "engaging with in-depth experience")

            # Currently Focus on
            self.document_understanding = Vision(especially = "table_comprehension")
            self.semantic_segmentation  = Vision(especially = "building previous SOTA for joy")

            self.classifier = nn.Linear(365, 2)

            
        def forward(self, an):
        
            # Tech Stack
            educating   = self.educator  (an, volunteering  =   ["Git", "GitHub/Actions", "Django"])
            engineering = self.engineer  (an, prefer        =   ["PyTorch", "Huggingface", "Wandb"])
            researching = self.researcher(an, experienced   =   ["LaTeX", "Linux", "Misc."])
            
            inputs = torch.cat((educating, engineering, researching), 1)

            # at This Moment
            doc_exp = self.document_understanding(inputs)
            seg_exp = self.semantic_segmentation(inputs)

            output = self.classifier((doc_exp, seg_exp))
            return output

            
    hello_world = AN()    

    
    """

    syntax = Syntax(code, "python", theme="github-dark", line_numbers=True)

    console.print()
    console.print(syntax)
    console.print()
    return code


def readme(console: Console) -> None:

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

        console.print()
        console.print("  Thank you for taking time!")
        console.print("  Feel free to contact me. 👋 ")
        console.print()
        console.print("  >  https://github.com/optimizean", style=color_emp)
        console.print("  >  optimize.an@gmail.com", style=color_emp)
        console.print()

        sys.exit()

# src/optimizean/content.py

"""
Only the Content will be placed here
"""

from optimizean.config import Parameters
from optimizean.utils import custom_color
from optimizean.localization import local_greeting

# config = Parameters()
color_main, color_sub, color_emp = custom_color()  # color


def introduce(local_greeting_message: str = "Welcome") -> str:
    return f"""{local_greeting_message}, Human and Non-Human Visitor! 🤖
This is a proactive Log Keeper and [{color_sub}]Computer Vision engineer, An.[/]
Believing greatest asset for developers is the trust and teamworks.
As a [{color_sub}]research-oriented engineer[/], I strive to overcome challenges 
utilize existing technologies and innovative ideas.

Always open to new collaborations!"""


def contact(config: dict) -> dict:
    contact = dict()
    contact["title"] = "Contact me 💻"
    contact["email"] = config.author.email
    contact["github"] = config.author.github
    contact["blog"] = config.author.blog
    return contact


def code() -> str:
    return """
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


def farewell(config: dict) -> str:
    return f"""
Thank you for having your time!
Feel free to contact me 👋 

>  Github:  {config.author.github}
>  Email:   {config.author.email}
"""


def proceed() -> str:
    return f"""
[{color_sub}]🔒 New Feature is Released! Why don't you try? [/]
It won't install any other package.
"""


def contents(customize_location: bool) -> dict:
    config = Parameters()
    contents_dict = dict()
    greeting = local_greeting(customize_location)  # optimizean/localization

    # combine
    contents_dict["introduce"] = introduce(greeting)
    contents_dict["contact"] = contact(config)  # title, email, github, blog
    contents_dict["code"] = code()
    contents_dict["farewell"] = farewell(config)
    contents_dict["proceed"] = proceed()
    return contents_dict


if __name__ == "__main__":
    print(contents())

# src/optimizean/installation.py

import subprocess
from rich.console import Console
from src.optimizean.utils import clear_screen, load_config


def is_poetry_installed():
    try:
        subprocess.run(
            ["poetry", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def install_dependencies(console: Console):

    status = False

    # color
    color_main = load_config()["color"]["main"]
    color_sub = load_config()["color"]["sub"]
    color_emp = load_config()["color"]["emp"]

    if is_poetry_installed():
        console.print(
            f"[bold {color_sub}]Poetry is installed, installing dependencies with Poetry...[/]"
        )

        try:
            subprocess.run(["poetry", "install"], check=True)
            console.print()
            console.print(f"> Dependencies installed successfully with Poetry!")
            status = True
        except subprocess.CalledProcessError as e:
            console.print(
                f"[bold {color_emp}]An error occurred while installing dependencies with Poetry: {e}[/]"
            )
    else:
        console.print(
            f"[bold {color_sub}]Poetry is not installed, installing dependencies with pip...[/]"
        )

        # Load the updated config to get the dependencies
        config = load_config()

        # Extract the list of dependencies
        dependencies = config["tool"]["poetry"]["dependencies"]

        # Install each dependency using pip
        for package, version in dependencies.items():
            console.print(f"Installing {package}...")
            try:
                subprocess.run(["pip", "install", f"{package}"])
                status = True
            except:
                status = False

        return status

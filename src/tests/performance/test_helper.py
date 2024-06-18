import os
import re
from time import time
from pathlib import Path
from contextlib import contextmanager


def get_project_root(is_str=False) -> Path:
    if is_str:
        return str(Path(__file__).resolve().parent.parent.parent)
    return Path(Path(__file__).resolve().parent.parent.parent)


@contextmanager
def timer(task):
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"- {task} tooked {elapsed_time:.6f} sec")
    return elapsed_time


def clean_text(text: str) -> str:
    """
    Clean text by Removing special-characters, number, spaces and convert text lowercase
        (e.g. clean dataset name; NTU-RGB+D to nturgbd)

    Args:
        text (str): Raw text to clean

    Returns:
        str: cleaned text
    """
    return re.sub(r"[^A-Za-z\s]", "", text).lower()


# -- TEST -- #
def test_helpers():
    assert get_project_root(is_str=True)
    assert timer(get_project_root(is_str=True))
    assert clean_text(get_project_root(is_str=True))


if __name__ == "__main__":
    test_helpers()

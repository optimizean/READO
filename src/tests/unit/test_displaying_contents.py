# tests/unit/test_displaying_contents.py

# Testing tool
import pytest
from optimizean.config import Parameters
from src.optimizean.localization import local_greeting

# Testing target
from src.optimizean.contents import introduce, contact, code, farewell, proceed


# -- Utils -- #
def istype(value, expected_type: str) -> bool:
    return type(value).__name__ == expected_type


# -- Fixtures -- #
@pytest.fixture
def config():
    return Parameters()


@pytest.fixture
def greeting():
    return local_greeting(customize_location=True)


# --- TESTS --- #


def test_introduce(greeting):
    assert istype(introduce(greeting), "str")


def test_contact(config):
    assert istype(contact(config), "dict")


def test_code():
    assert istype(code(), "str")


def test_farewell(config):
    assert istype(farewell(config), "str")


def test_proceed():
    assert istype(proceed(), "str")


def test_contents():
    config = Parameters()
    greeting = local_greeting(customize_location=True)
    assert istype(introduce(greeting), "str")
    assert istype(contact(config), "dict")
    assert istype(code(), "str")
    assert istype(farewell(config), "str")
    assert istype(proceed(), "str")

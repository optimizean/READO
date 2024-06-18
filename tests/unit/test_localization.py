# optimizean.tests/unit/test_localization.py

""" Basic Utils """
import pytest
from optimizean.config import Parameters
from optimizean.localization import get_localtime, get_location, greetings


@pytest.fixture
def config():
    return Parameters()


@pytest.fixture
def greetings_dict():
    return greetings()


""" Test """

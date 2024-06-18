# # tests/unit/test_displaying_contents.py

# """ Modules """
# # Tools
# import pytest
# from pytest_mock import mocker  # poetry add --dev pytest-mock
# from optimizean.config import Parameters
# from optimizean.localization import local_greeting


# # Target
# from optimizean.contents import contents
# from optimizean.display import (
#     rich_introduce,
#     rich_contact,
#     rich_code,
#     rich_farewell,
#     rich_proceed,
# )
# from optimizean.display import display_contents, display_rich_contents


# """ Utils """
# # Fixture


# @pytest.fixture
# def config():
#     return Parameters()


# """ TEST """

# raise AssertionError("\n\nIncomplete Work\n\n")

# """

# # tests/unit/test_display.py

# import pytest
# from rich.console import Console
# from rich.text import Text
# from rich.table import Table
# from rich.panel import Panel
# from rich.prompt import Prompt
# from pytest_mock import mocker

# from optimizean.display import (
#     rich_introduce,
#     rich_contact,
#     rich_code,
#     rich_farewell,
#     rich_proceed,
#     display_contents,
#     display_rich_contents,
# )
# from optimizean.contents import contents

# # Mock custom_color function to return static values
# @pytest.fixture(autouse=True)
# def mock_custom_color(mocker):
#     mocker.patch("optimizean.utils.custom_color", return_value=("red", "blue", "green"))

# @pytest.fixture
# def mock_contents(mocker):
#     contents_mock = {
#         "introduce": "Welcome, Human and Non-Human Visitor!",
#         "contact": {"title": "Contact me 💻", "email": "test@example.com", "github": "github", "blog": "blog"},
#         "code": "print('Hello, World!')",
#         "farewell": "Thank you for having your time!",
#         "proceed": "Proceed with the new feature?",
#     }
#     mocker.patch("optimizean.contents.contents", return_value=contents_mock)
#     return contents_mock

# def test_rich_introduce():
#     content = "This is a [bold red]test[/]."
#     result = rich_introduce(content)
#     assert isinstance(result, Text)
#     assert "test" in result.plain

# def test_rich_contact(mock_contents):
#     content_dict = mock_contents["contact"]
#     result = rich_contact(content_dict)
#     assert isinstance(result, Table)
#     assert len(result.columns) == 2

# def test_rich_code():
#     content = "print('Hello, World!')"
#     result = rich_code(content)
#     assert isinstance(result, Panel)

# def test_rich_farewell():
#     content = "Goodbye!"
#     result = rich_farewell(content)
#     assert isinstance(result, Text)

# def test_rich_proceed(mocker):
#     mocker.patch('rich.prompt.Prompt.ask', return_value='y')
#     content = "Proceed?"
#     result = rich_proceed(content)
#     assert result == 'y'

# def test_display_contents(mocker, mock_contents):
#     mock_console = mocker.Mock(spec=Console)
#     introduce_text = rich_introduce(mock_contents["introduce"])
#     contact_table = rich_contact(mock_contents["contact"])
#     result = display_contents(mock_console, introduce_text, contact_table)
#     assert isinstance(result, Panel)

# def test_display_rich_contents(mocker, mock_contents):
#     mock_console = mocker.Mock(spec=Console)
#     mocker.patch('rich.console.Console', return_value=mock_console)
#     mocker.patch('optimizean.display.rich_proceed', return_value='n')

#     display_rich_contents(False)
#     mock_console.print.assert_called()  # Check if console.print was called

#     # Check that the appropriate functions were called with the correct mocked content
#     mock_console.print.assert_any_call(rich_introduce(mock_contents["introduce"]))
#     mock_console.print.assert_any_call(rich_contact(mock_contents["contact"]))


# """

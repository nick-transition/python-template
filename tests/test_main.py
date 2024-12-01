from src.main import greet


def test_greet_default():
    """Test the default greeting."""
    assert greet() == "Hello, World!"


def test_greet_custom():
    """Test a custom greeting."""
    assert greet("Poe") == "Hello, Poe!"

import pytest

from tempconv import celsius_to_fahrenheit, fahrenheit_to_celsius
from tempconv.cli import main


@pytest.mark.parametrize(
    ("celsius", "fahrenheit"),
    [(0, 32), (100, 212), (-40, -40), (37, 98.6)],
)
def test_round_trip(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(celsius)


def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(-300)
    with pytest.raises(ValueError):
        fahrenheit_to_celsius(-500)


def test_cli_converts_to_fahrenheit(capsys):
    assert main(["100", "--to", "f"]) == "212.00°F"
    assert "212.00°F" in capsys.readouterr().out

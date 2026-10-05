"""Temperature conversion functions."""

ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert degrees Celsius to degrees Fahrenheit."""
    if celsius < ABSOLUTE_ZERO_C:
        raise ValueError(f"{celsius}°C is below absolute zero")
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert degrees Fahrenheit to degrees Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    if celsius < ABSOLUTE_ZERO_C:
        raise ValueError(f"{fahrenheit}°F is below absolute zero")
    return celsius

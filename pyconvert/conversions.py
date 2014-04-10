"""A module to do various unit conversions."""


def validate_input(incoming):
    """Converts input to float if it can.

    Args:
        incoming (str): String probably coming from a 'raw_input()'.

    Returns:
        result (str or float): Depends on try statement.
    """
    try:
        result = float(incoming)
    except ValueError:
        result = incoming

    return result


def celsius_fahrenheit(number):
    """Convert celsius to fahrenheit."""
    return (number * 9.0 / 5.0) + 32.0


def fahrenheit_celsius(number):
    """Convert fahrenheit to celsius."""
    return (number - 32.0) * 5.0 / 9.0


def kms_miles(number):
    """Convert kms to miles."""
    return number * 0.62137


def miles_kms(number):
    """Convert miles to kms."""
    return number / 0.62137

if __name__ == '__main__':
    pass

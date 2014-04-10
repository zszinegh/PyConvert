"""A module to do various unit conversions.

This module's functions convert various units of measurement.

All functions expect a 'float' as an argument and return a 'float'.

'validate_input()' can be used before running any function to
convert the input to a 'float'.

"""


def validate_input(incoming):
    """Convert input to float.

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


# Conversion functions.
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

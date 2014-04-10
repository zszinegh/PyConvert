"""Main program module.

A front end for the unit conversions in 'conversions.py'.

This module can be imported like 'import pyconvert.main' and
run by calling 'pyconvert.main.main()'.

"""

import sys
import subprocess
from collections import OrderedDict

import pyconvert.conversions as convert


MENU_DICT = OrderedDict(
    [
        (1, ('Celsius to Fahrenheit', convert.celsius_fahrenheit)),
        (2, ('Fahrenheit to Celsius', convert.fahrenheit_celsius)),
        (3, ('Kilometers to Miles', convert.kms_miles)),
        (4, ('Miles to Kilometers', convert.miles_kms)),
        (5, ('Quit', 'quit'))
    ]
)


def get_running_os():
    """Get the operating system."""

    # Check for windoze to get clear screen command.
    if sys.platform.startswith('win'):
        return 'cls'
    else:
        return 'clear'


def clr_screen(clear_cmd):
    """Clear console screen.

    Args:
        clear_cmd (str): Platform specific clear screen command.
    """
    subprocess.call(clear_cmd)


def main():
    """Run the program in the console."""

    clear_cmd = get_running_os()

    while True:
        clr_screen(clear_cmd)

        print "\t Main Menu"
        print "---------------------------"

        for key, value in MENU_DICT.items():
            print str(key) + '. ' + value[0]
        print
        print 'Please enter a selection number:',

        try:
            selection = int(raw_input())
        except ValueError:
            print
            print 'Please enter a valid number.'
            raw_input('Press ENTER to continue...')
        else:
            if selection not in MENU_DICT:
                print
                print 'Invalid menu selection.'
                raw_input('Press ENTER to continue...')
            elif selection == 5:
                print
                print 'Quitting...'
                print
                break
            else:
                print
                print 'Convert %s.' % MENU_DICT[selection][0]
                num_to_convert = raw_input('Enter number to convert: ')
                num_to_convert = convert.validate_input(num_to_convert)

                if not isinstance(num_to_convert, float):
                    print
                    print '%s is not a number.' % num_to_convert
                    raw_input('Press ENTER to continue...')
                else:
                    result = MENU_DICT[selection][1](num_to_convert)

                    # Round input and output to 1 decimal place.
                    num_to_convert = round(num_to_convert, 1)
                    result = round(result, 1)

                    unit_from = MENU_DICT[selection][0].split()[0]
                    unit_to = MENU_DICT[selection][0].split()[2]

                    print
                    print('%.1f in %s is %.1f in %s.' %
                          (num_to_convert, unit_from, result, unit_to))
                    raw_input('Press ENTER to continue...')

    sys.exit(0)


if __name__ == '__main__':
    main()

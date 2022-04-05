import convert_clipboard_snakecase
import convert_clipboard_camelCase
from pynput import keyboard


def execute_snake():
    """converts last clipboarded string object into snakecase
    """
    convert_clipboard_snakecase.__main__()


def execute_camel():
    """converts last clipboarded string object into camelcase
    """
    convert_clipboard_camelCase.__main__()


# Runs the listener repeatedly to keep checking
while True:
    with keyboard.GlobalHotKeys({
        '<shift>+<alt>+<ctrl>+-': execute_snake,
            '<shift>+<alt>+<ctrl>+=': execute_camel}) as h:
        h.join()

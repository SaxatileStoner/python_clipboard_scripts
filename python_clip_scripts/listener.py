import convert_clipboard_snakecase
import convert_clipboard_camelCase
from pynput import keyboard


def execute_snake():
    convert_clipboard_snakecase.__main__()


def execute_camel():
    convert_clipboard_camelCase.__main__()


while True:
    with keyboard.GlobalHotKeys({
        '<alt>+<ctrl>+r': execute_snake,
            '<alt>+<ctrl>+t': execute_camel}) as h:
        h.join()

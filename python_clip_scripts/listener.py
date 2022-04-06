from pynput import keyboard
import convert_clipboard_snakecase
import convert_clipboard_camelCase


def execute_snake():
    """converts last clipboarded string object into snakecase
    """
    convert_clipboard_snakecase.main()


def execute_camel():
    """converts last clipboarded string object into camelcase
    """
    convert_clipboard_camelCase.main()


# Runs the listener repeatedly to keep checking
def main():
    # while True:
    with keyboard.GlobalHotKeys({
        '<shift>+<alt>+<ctrl>+-': execute_snake,
            '<shift>+<alt>+<ctrl>+=': execute_camel}) as h:
        h.join()


if __name__ == '__main__':
    main()

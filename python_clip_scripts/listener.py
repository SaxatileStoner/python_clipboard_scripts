from pynput import keyboard
import clipboard


def execute_snake():
    """converts last clipboarded string object into snakecase
    """
    clipboard.clip_to_snake()


def execute_camel():
    """converts last clipboarded string object into camelcase
    """
    clipboard.clip_to_camel()


# Runs the listener repeatedly to keep checking
def main():
    while True:
        with keyboard.GlobalHotKeys({
            '<shift>+<alt>+<ctrl>+-': execute_snake,
                '<shift>+<alt>+<ctrl>+=': execute_camel}) as h:
            h.join()


if __name__ == '__main__':
    main()

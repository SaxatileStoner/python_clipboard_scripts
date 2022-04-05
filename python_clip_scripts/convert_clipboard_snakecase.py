# from utils import win32_tray_popup
from re import sub
import win32clipboard


def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
                s.replace('-', ' '))).split()).lower()


def __main__():
    title = "convert_clipboard_snakecase.py"
    win32clipboard.OpenClipboard()
    try:
        string = str(win32clipboard.GetClipboardData())
    except TypeError:
        print("Type Error!")
        # win32_tray_popup.balloon_tip(
        #     title, "Last Clipboard Entry not of a string type")

    string = snake_case(string)
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(f"{string}")
    win32clipboard.CloseClipboard()
    # win32_tray_popup.balloon_tip(
    #     title, f"Converted last clipboarded item to snake_case! {string}")


if __name__ == '__main__':
    __main__()

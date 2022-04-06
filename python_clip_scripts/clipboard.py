import win32clipboard
import convert_case


def clip_to_snake():
    # title = "convert_clipboard_snakecase.py"
    win32clipboard.OpenClipboard()
    try:
        string = str(win32clipboard.GetClipboardData())
    except TypeError:
        print("ERROR, not same as String type")
        # win32_tray_popup.balloon_tip(
        #     title, "Last Clipboard Entry not of a string type")

    string = convert_case.snake_case(string)
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(f"{string}")
    win32clipboard.CloseClipboard()
    # win32_tray_popup.balloon_tip(
    #     title, f"Converted last clipboarded item to snake_case! {string}")


def clip_to_camel():
    # title = "convert_clipboard_camelCase.py"
    win32clipboard.OpenClipboard()
    try:
        string = str(win32clipboard.GetClipboardData())
    except TypeError:
        print("ERROR, not same as String type")
        # win32_tray_popup.balloon_tip(
        #     title, "Last Clipboard Entry not of a string type")

    string = convert_case.camel_case(string)
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(f"{string}")
    win32clipboard.CloseClipboard()
    # win32_tray_popup.balloon_tip(
    #     title, f"Converted last clipboarded item to camelCase! {string}")

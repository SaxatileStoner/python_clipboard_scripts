from pywin32_tools import win32_tray_popup
import win32clipboard
from re import sub


def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


title = "convert_clipboard_camelCase.py"
win32clipboard.OpenClipboard()
try:
    string = str(win32clipboard.GetClipboardData())
except TypeError:
    win32_tray_popup.balloon_tip(
        title, "Last Clipboard Entry not of a string type")

string = camel_case(string)
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(f"{string}")
win32clipboard.CloseClipboard()
win32_tray_popup.balloon_tip(
    title, f"Converted last clipboarded item to camelCase! {string}")

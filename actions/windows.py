import subprocess
import os


def open_chrome():

    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(
            r"~\AppData\Local\Google\Chrome\Application\chrome.exe"
        )
    ]

    for path in chrome_paths:

        if os.path.exists(path):

            subprocess.Popen(path)

            return "Chrome باز شد."

    return "Chrome پیدا نشد."
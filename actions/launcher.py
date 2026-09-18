import subprocess
import os


APPS = {

    # مرورگرها
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "کروم": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    # برنامه‌های ویندوز
    "notepad": "notepad.exe",
    "نوت پد": "notepad.exe",

    "calculator": "calc.exe",
    "ماشین حساب": "calc.exe",

    "vscode": r"C:\Users\omidn\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "وی اس کد": r"C:\Users\omidn\AppData\Local\Programs\Microsoft VS Code\Code.exe",

}


def open_app(app_name):

    app_name = app_name.lower().strip()


    for name, command in APPS.items():

        if name in app_name:

            try:
                subprocess.Popen(command)

                return f"{name} باز شد."

            except Exception as e:
                return f"خطا در باز کردن {name}: {e}"


    return "این برنامه را هنوز نمی‌شناسم."
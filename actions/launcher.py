import subprocess
import os


APPS = {

    # مرورگرها
    "chrome": "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "کروم": "C:\Program Files\Google\Chrome\Application\chrome.exe",

    # برنامه‌های ویندوز
    "notepad": "notepad.exe",
    "نوت پد": "notepad.exe",

    "calculator": "calc.exe",
    "ماشین حساب": "calc.exe",

    "vscode": "visual studio code",
    "وی اس کد": "visual studio code.exe",

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
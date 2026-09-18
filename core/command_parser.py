# دستورات انجامی در این فایل قرار میگیرند
# Executable commands are placed in this file.

class CommandParser:


    def __init__(self):
        pass


    def parse(self, command):

        command = command.lower().strip()


        result = {
            "action": None,
            "target": None,
            "raw": command
        }


        # تشخیص باز کردن
        if "باز کن" in command or "open" in command or "اجرا کن" in command:

            result["action"] = "open"


        # تشخیص بستن
        elif "ببند" in command or "close" in command:

            result["action"] = "close"


        return result
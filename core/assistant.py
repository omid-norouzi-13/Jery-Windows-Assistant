from actions.launcher import open_app
from actions.windows import open_chrome


class JeryAssistant:

    def __init__(self):
        self.name = "Jery"

    def process_command(self, command):
        command = command.lower().strip()

        if "hello" in command or "سلام" in command:
            return "سلام! من جری هستم. | hi! Im jery"

        elif "who are you" in command or "تو کی هستی" in command:
            return "من Jery هستم، دستیار شخصی شما."

        elif "باز کن" in command or "open" in command:
            return open_app(command)

        else:
            return "متوجه نشدم. لطفاً دوباره امتحان کن."
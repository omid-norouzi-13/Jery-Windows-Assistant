from actions.launcher import open_app


class Executor:


    def __init__(self):
        pass


    def execute(self, command):

        action = command.get("action")
        target = command.get("target")


        if action == "open":

            return open_app(target)


        return "دستور قابل اجرا نیست."
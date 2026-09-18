from core.command_engine import CommandEngine
from core.executor import Executor


class JeryAssistant:


    def __init__(self):

        self.engine = CommandEngine()
        self.executor = Executor()



    def process_command(self, command):

        parsed_command = self.engine.process(command)


        if parsed_command["action"] is None:

            return "متوجه نشدم چه کاری باید انجام بدهم."


        result = self.executor.execute(parsed_command)


        return result
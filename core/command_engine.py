from core.command_parser import CommandParser
from core.target_extractor import TargetExtractor


class CommandEngine:


    def __init__(self):

        self.parser = CommandParser()
        self.extractor = TargetExtractor()



    def process(self, command):

        parsed_command = self.parser.parse(command)

        target = self.extractor.extract(command)


        parsed_command["target"] = target


        return parsed_command
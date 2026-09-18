from core.command_parser import CommandParser


parser = CommandParser()


commands = [
    "کروم رو باز کن",
    "کروم رو ببند",
    "open chrome"
]


for command in commands:

    result = parser.parse(command)

    print(command)
    print(result)
    print("----------------")
from core.command_engine import CommandEngine


engine = CommandEngine()


commands = [
    "کروم رو باز کن",
    "کروم رو اجرا کن",
    "نوت پد رو باز کن",
    "وی اس کد رو اجرا کن"
]


for command in commands:

    result = engine.process(command)

    print(command)
    print(result)
    print("----------------")
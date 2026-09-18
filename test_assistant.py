from core.assistant import JeryAssistant


jery = JeryAssistant()


commands = [

    "کروم رو باز کن",
    "نوت پد رو باز کن",
    "وی اس کد رو اجرا کن"

]


for command in commands:

    result = jery.process_command(command)

    print(command)
    print(result)
    print("----------------")
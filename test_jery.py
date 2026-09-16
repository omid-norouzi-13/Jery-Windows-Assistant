from core.assistant import JeryAssistant


jery = JeryAssistant()


while True:
    command = input("You: ")

    if command == "exit":
        break

    response = jery.process_command(command)

    print("Jery:", response)
from core.executor import Executor


executor = Executor()


commands = [

    {
        "action": "open",
        "target": "chrome"
    },

    {
        "action": "open",
        "target": "notepad"
    }

]


for command in commands:

    result = executor.execute(command)

    print(command)
    print(result)
    print("----------------")
from abc import ABC

class Command(ABC):

    def __init__(self):
        self.subcommands = CommandMap()
    
    @abstractmethod
    def execute(message):
        if type(message) is str:
            message = message.split(" ")

        #elif type(message) is list:
        
        ret = subcommands.try_exec(message_list)
        return ret if ret
        
        print("Trying to execute...")

        return self.run(message)

class CommandMap:
    def __init__(self):
        self.command_table = {}

    def add(name, cmd):
        command_table[name] = cmd

    def try_exec(message):
        if type(message) is list:
            try:
                c = command_table[message[0].lower()]
                if c:
                    return c.execute(message[1:])
            except:
                print("Error")


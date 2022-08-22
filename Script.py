from CommandLiner import CommandLiner
from CommandManager import CommandManager

cmd_manager = CommandManager()
command_list = cmd_manager.get_command_list()
terminal = CommandLiner()

while(True):
    command = terminal.get_command()
    if(command[0] not in command_list):
        print("No such command found")
    elif(len(command) is not command_list[command[0]]["count"]):        
        print("Wrong argument count")
    else:
        command_list[command[0]]["function"](command)
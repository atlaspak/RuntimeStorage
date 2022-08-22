import sys

class CommandLiner():
    def get_command(self):
        print('> ', end='')
        command = str(input())
        return command.split()

    def print(self, *args):
        print(args[0])

    def exit(self):
        sys.exit()
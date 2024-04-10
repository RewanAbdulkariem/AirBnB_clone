#!/usr/bin/python3
"""
console.py
created by Rewan Abdulkariem
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Simple command processor example.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        "Quit command to exit the program\n"
        exit()

    def do_EOF(self, line):
        "^d to exit the program\n"
        return True

    def emptyline(self):
        """Override default empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

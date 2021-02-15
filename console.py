#!/usr/bin/python3

"""this module contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):

    """command interpreter class definition"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """to exit the program."""
        return True

    def do_EOF(self, arg):
        """exit the program."""
        return True

    def help_quit(self):
        """help updated and documented"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """updated and documented"""
        print("exit the program")

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

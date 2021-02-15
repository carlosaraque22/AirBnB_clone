#!/usr/bin/python3

"""this module contains the entry point of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel

found_classes = {"BaseModel": BaseModel}

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel,"""
        """saves it (to the JSON file) and prints the id"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
            return False
        if command[0] in found_classes:
            new_object = found_classes[command[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_object.id)
        new_object.save()
          
if __name__ == '__main__':
    HBNBCommand().cmdloop()

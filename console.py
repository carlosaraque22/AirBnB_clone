#!/usr/bin/python3

"""this module contains the entry point of the command interpreter"""

import cmd
import models
import shlex
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

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        command = arg.split()
        models.storage.reload()
        if (len(command) == 0):
            print("** class name missing **")
            return False
        if command[0] in found_classes:
            if (len(command) > 1):
                new_object = command[0] + '.' + command[1]
                if new_object in models.storage.all():
                    print(models.storage.all()[new_object])
                else:
                    print("** no instance found **")
            elif (len(command) == 1):
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        command = arg.split()
        models.storage.reload()
        if (len(command) == 0):
            print("** class name missing **")
            return False
        if command[0] in found_classes:
            if (len(command) > 1):
                new_object = command[0] + '.' + command[1]
                if new_object in models.storage.all():
                    models.storage.all().pop(new_object)
                    models.storage.save()
                else:
                    print("** no instance found **")
            elif (len(command) == 1):
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
         """Prints all string representation of all instances
         based or not on the class name"""
         command = arg.split()
         models.storage.reload()
         if (len(command) == 0) or (command[0] in found_classes):
             print(models.storage.all())
         else:
             print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or"""
        """updating attribute (save the change into the JSON file)"""
        models.storage.reload()
        if len(arg) == 0:
             print("** class name missing **")
             return False
        else:
            command = shlex.split(arg)
            if command[0] not in found_classes:
                print("** class doesn't exist **")
                return False
            if command[0] in found_classes and len(command) == 1:
                print("** instance id missing **")
                return False
            new_object = command[0] + '.' + command[1]
            if new_object in models.storage.all():
                updated_dic = models.storage.all()[new_object].__dict__
                if len(command) == 2:
                    print("** attribute name missing **")
                elif len(command) == 3:
                    print("** value missing **")
                else:
                    key = command[2]
                    try:
                        attr = type(updated_dic[key])
                        value = attr(command[3])
                    except KeyError:
                        value = command[3]
                    updated_dic[key] = value
                    models.storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

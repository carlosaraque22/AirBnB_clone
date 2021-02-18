#!/usr/bin/python3

"""this module contains the entry point of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

found_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": Place,
                 "Review": Review}


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
            command = arg.split()
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

    def do_count(self, arg):
        """Count instances of a Class"""
        count = 0
        arg_list = arg.split(' ')
        for key in models.storage.all():
            obj_class = models.storage.all()[key]
            if arg_list[0] == obj_class.__class__.__name__:
                count += 1
        print(count)

    ##########
    # call all function
    #########

    def do_BaseModel(self, arg):
        """Function to use all methods"""
        self.class_action("BaseModel", arg)

    def do_User(self, arg):
        """Function to use all methods"""
        self.class_action("User", arg)

    def do_State(self, arg):
        """Function to use all methods"""
        self.class_action("State", arg)

    def do_City(self, arg):
        """Function to use all methods"""
        self.class_action("City", arg)

    def do_Amenity(self, arg):
        """Function to use all methods"""
        self.class_action("Amenity", arg)

    def do_Place(self, arg):
        """Function to use all methods"""
        self.class_action("Place", arg)

    def do_Review(self, arg):
        """Function to use all methods"""
        self.class_action("Review", arg)

    def class_action(self, class_name, arg):
        """In case to not found the command this func is executed"""
        if arg[:6] == ".all()":
            self.do_all(class_name)
        elif arg[:6] == ".show(":
            self.do_show(class_name + ' ' + arg[7: -2])
        elif arg[:7] == ".count(":
            self.do_count(class_name)
        elif arg[:9] == ".destroy(":
            self.do_destroy(class_name + ' ' + arg[10: -2])
        elif arg[:8] == ".update(":
            if "{" in arg and "}" in arg:
                new_arg = arg[8:-1].split("{")
                new_arg[1] = "{" + new_arg[1]
            else:
                new_arg = arg[8:-1].split(",")
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace(" ", " ")
                self.do_update(class_name + " " + new_arg)
            # elif len(new_arg) == 2:

if __name__ == '__main__':
    HBNBCommand().cmdloop()

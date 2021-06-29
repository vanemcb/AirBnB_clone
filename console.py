#!/usr/bin/python3
""" Module class console
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""


import cmd
from models.base_model import BaseModel
from models import storage

if __name__ == '__main__':

    class HBNBCommand(cmd.Cmd):
        """Command interpreter for the AirBnB project."""

        prompt = "(hbnb) "
        file = None

        def do_quit(self, line):
            """quit: command to exit the program.\n"""
            return True

        def do_EOF(self, line):
            """End of File"""
            return True

        def emptyline(self):
            pass

        def do_create(self, class_name):
            """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.
            """
            if not class_name:
                print("** class name missing **")
            elif class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                new_object = BaseModel()
                new_object.save()
                print(new_object.id)

        def help_create(self):
            print('\n'.join([
                'create: command that creates a new instance of BaseModel,',
                'saves it (to the JSON file) and prints the id.\n',
            ]))

        def do_show(self, line):
            """ Prints the string representation of an instance based
            on the class name and id """

            args = line.split()

            if not args:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                dict_objects = storage.all()
                obj = dict_objects.get(key)
                if obj:
                    print(obj)
                else:
                    print("** no instance found **")

        def help_show(self):
            print('\n'.join([
                'show: command that prints the string representation',
                'of an instance based on the class name and id.\n',
            ]))

        def do_destroy(self, line):
            """ Deletes an instance based on the class name and id """
            args = line.split()

            if not args:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                dict_objects = storage.all()
                obj = dict_objects.get(key)
                if obj:
                    dict_objects.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")

        def help_destroy(self):
            print('\n'.join([
                'destroy: command that deletes an',
                'instance based on the class name and id.\n',
            ]))

        def do_all(self, line=None):
            """  Prints all string representation of all instances
            based or not on the class name """
            if not line or line == "BaseModel":
                dict_objects = storage.all()
                list_objects = []
                for key, obj in dict_objects.items():
                    list_objects.append(obj.__str__())
                print(list_objects)
            else:
                print("** class doesn't exist **")

        def help_all(self):
            print('\n'.join([
                'all: command that Prints all string representation of',
                'all instances based or not on the class name.\n',
            ]))

        def do_update(self, line):
            """ Updates an instance based on the class name and id
            by adding or updating attribute """
            args = line.split()

            if not args:
                print("** class name missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) > 1:
                key = args[0] + "." + args[1]
                dict_objects = storage.all()
                obj = dict_objects.get(key)
                if obj is None:
                    print("** no instance found **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(obj, args[2], str(args[3].replace('"', '')))
                        storage.save()

        def help_update(self):
            print('\n'.join([
                'update: command that updates an instance based on the class',
                'name and id by adding or updating attribute.\n',
            ]))

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

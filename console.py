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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

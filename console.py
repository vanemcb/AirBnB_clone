#!/usr/bin/python3
""" Module class console
    This module is for the project 0x00. AirBnB clone - The console
    proposed by Holberton school to learn how a web page works.
"""
import cmd
from models.base_model import BaseModel

if __name__ == '__main__':
    class HBNBCommand(cmd.Cmd):
        """Command interpreter for the AirBnB project."""

        prompt = "(hbnb) "

        def do_quit(self, line):
            """Quit command to exit the program"""
            return True

        def do_EOF(self, line):
            """Prueba 2"""
            return True

        def emptyline(self):
            pass

        def do_create(self, class_name):
            """create command that creates a new instance of BaseModel,
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
                'saves it (to the JSON file) and prints the id.',
            ]))

        def do_show(self, class_name=None, object_id=None):

            print(class_name, object_id)
            if not class_name:
                print("** class name missing **")
            elif class_name != "BaseModel":
                print("** class doesn't exist **")
            elif not object_id:
                print("** instance id missing **")
            else:
                print(FileStorage.__objects[class_name + id])

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

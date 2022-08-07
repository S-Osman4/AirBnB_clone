#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNB Console extends from cmd package
    """
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Exit command to exit the program'
        return True

    def do_create(self, inputs):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id """
        if not(inputs):
            print("** class name missing **")
        else:
            try:
                if classes[inputs]:
                    instance = classes[inputs]()
                    instance.save()
                    print(instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        clsname, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not clsname:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.clslist.get(clsname):
            print("** class doesn't exist **")
        else:
            k = clsname + "." + obj_id
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class name
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.classes.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.classes.get(arg)])
            
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = "(hbnb) "
    all_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            ' k = key, v = value'
            for k, v in objects.items():
                obj_id = objects[k].id
                obj_class = objects[k].__class__.__name__
                if obj_id == args[1] and args[0] == obj_class:
                    print(objects[k])
                    return
            print("** no instance found **")
            
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            'k = key, v = value'
            for k, v in objects.items():
                obj_id = objects[k].id
                obj_class = objects[k].__class__.__name__
                if obj_id == args[1] and args[0] == obj_class:
                    del objects[k]
                    models.storage.save()
                    break
            else:
                print("** no instance found **")
                
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = parse(arg)
        objects = models.storage.all()
        if not args:
            obj_list = []
            ' k = key, v = value'
            for k, v in objects.items():
                obj_list.append(str(objects[k]))
            if obj_list:
                print(obj_list)
        else:
            obj_list = []
            'k = key, v = value'
            for k, v in objects.items():
                if objects[k].__class__.__name__ == args[0]:
                    obj_list.append(str(objects[k]))
            if obj_list:
                print(obj_list)
            else:
                if args[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                
    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = parse(arg)
        objects = models.storage.all()
        count = 0
        if not args:
            print("** class name missing **")
        else:
            'k = key, v = value'
            for k, v in objects.items():
                if objects[k].__class__.__name__ == args[0]:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

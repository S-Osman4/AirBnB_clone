#!/usr/bin/python3
"""This is the console for AirBnB"""

import cmd
from models.base_model import BaseModel
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
        if not args:
            print('** class name missing **')
        elif args not in HBNBCommand.all_classes:
            print('** class doesn\'t exist **')
        else:
            classes = {'BaseModel': BaseModel, 'User': User,
                       'Amenity': Amenity,
                       'City': City, 'Place': Place,
                       'Review': Review, 'State': State}
            new_obj = classes[args]()
            new_obj.save()
            print('{}'.format(new_obj.id))
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

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

    def do_all(self, inputs):
        """ The command all prints all string representation
        of all instances based or not on the class name
        """
        all_objs = storage.all()
        list_obj = []
        if not(inputs):
            if all_objs == {}:
                print("[]")
                return
            for key in storage._FileStorage__objects:
                list_obj.append(str(storage._FileStorage__objects[key]))
            print(list_obj)
            return
        try:
            cl = all_classes[inputs]
        except Exception:
            print("** class doesn't exist **")
            return
        for key in storage._FileStorage__objects:
            if key.split('.')[0] == inputs:
                list_obj.append(str(storage._FileStorage__objects[key]))
        print(list_obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

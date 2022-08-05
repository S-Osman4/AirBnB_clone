<<<<<<< HEAD
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
=======
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
            classes = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
>>>>>>> df4bf6928c87ad2b5aa5e3afef70def3afa20753

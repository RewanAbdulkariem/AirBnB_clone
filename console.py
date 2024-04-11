#!/usr/bin/python3
"""
console.py
created by Rewan Abdulkariem
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Place': Place, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        "Quit command to exit the program\n"
        exit()

    def do_EOF(self, line):
        "^d to exit the program\n"
        return True

    def emptyline(self):
        """Override default empty line"""
        pass

    def do_create(self, line):
        """
        Create a new instance of a specified model class.

        Usage:
            create <class_name>
        Example:
            create BaseModel
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        if class_name not in current_classes:
            print("** class doesn't exist **")
            return
        new = current_classes[class_name]()
        new.save()
        print(new.id)

    def get_class_id(self, line):
        """
        Helper function to extract class name and instance id from input.
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return False
        elif len(args) == 1:
            print('** instance id missing **')
            return False

        class_name = args[0]
        id = args[1]
        if class_name not in current_classes:
            print("** class doesn't exist **")
            return False

        data = storage.all()
        key = f"{class_name}.{id}"
        if key not in data:
            print('** no instance found **')
            return False
        return args

    def do_show(self, line):
        """
        Show the string representation of an instance.

        Usage:
            show <class_name> <instance_id>
        Example:
            show BaseModel 1234-1234-1234
        """
        args = self.get_class_id(line)
        if not args:
            return
        class_name = args[0]
        id = args[1]
        data = storage.all()
        key = f"{class_name}.{id}"
        instance = data[key]
        print(instance)

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.

        Usage:
            destroy <class_name> <instance_id>
        Example:
            destroy BaseModel 1234-1234-1234
        """
        args = self.get_class_id(line)
        if not args:
            return
        class_name = args[0]
        id = args[1]
        data = storage.all()
        key = f"{class_name}.{id}"
        del data[key]
        storage.save()

    def do_all(self, line):
        """
        Print all string representations of instances.

        Usage:
            all <class_name> (optional)
        Example:
            all BaseModel
        """
        args = line.split()
        data = storage.all()
        if len(args) == 0:
            print(["{}".format(str(val)) for _, val in data.items()])
            return

        class_name = args[0]
        if class_name not in current_classes:
            print("** class doesn't exist **")
            return

        print(["{}".format(str(val)) for _, val in data.items()
               if val.__class__.__name__ == class_name])

    def do_update(self, line):
        """
        Update an instance based on the class name and id.

        Usage:
            update <class_name> <instance_id> <attr_name> <attr_value>
        Example:
            update BaseModel 1234-1234-1234 email "airbnb@mail.com"
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return False
        elif len(args) == 1:
            print('** instance id missing **')
            return False
        elif len(args) == 2:
            print('** attribute name missing **')
            return False
        elif len(args) == 3:
            print('** value missing **')
            return False

        class_name = args[0]
        id = args[1]
        attribute = args[2]
        value = args[3]

        if class_name not in current_classes:
            print("** class doesn't exist **")
            return False

        data = storage.all()
        key = f"{class_name}.{id}"
        if key not in data:
            print('** no instance found **')
            return False

        instance = data[key]
        setattr(instance, attribute, value)
        instance.save()

    def do_count(self, line):
        """
        """
        args = line.split()
        counter = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                counter += 1
        print(counter)

    def default(self, line):
        """
        """
        line = line.replace("(", ".").replace(
            ", ", ".").replace("\"", "").replace(
            "\'", "").replace(")", "").replace(
            "{","").replace(":","").replace(
            "}","").replace(" ",".")

        args = line.split('.')
        if len(args) < 2:
            return
        if 'all' in args[1]:
            self.do_all(args[0])
        elif 'count' in args[1]:
            self.do_count(args[0])
        elif 'show' in args[1]:
            self.do_show(args[0] + " " + args[2])
        elif 'destroy' in args[1]:
            self.do_destroy(args[0] + " " + args[2])
        elif 'update' in args[1]:
            for i in range(3, len(args), 2):
               ret = self.do_update(args[0] + " " + args[2] + " " + args[i] + " " + args[i+1])
               if not ret:
                   return

if __name__ == '__main__':
    HBNBCommand().cmdloop()

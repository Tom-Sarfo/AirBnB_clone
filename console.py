#!/usr/bin/python3
"""
    This module is the entry point for the command interpreter
"""
import cmd
import re
import shlex
from models.base_model import BaseModel
from models import storage
from models import user
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in shlex.split(arg)]
        else:
            lexer = shlex.split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = shlex.split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle endo of file condition with"""
        print("") #print new line to ensure clean output
        return True

    def emptyline(self):
        """Return when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id"""
        args = parse(arg)
        if len(args) == 0:
            print("**class name missing**")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()
    
    def do_show(self, arg):
        """ Prints the string representation of an
        instance based on the class name and id"""
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("**class name missing**")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("**class name missing**")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_all = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_all.append(obj.__str__())
                elif len(args) == 0:
                    obj_all.append(obj.__str__())
            print(obj_all)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("**class name missing**")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()

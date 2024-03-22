#!/usr/bin/python3
"""
    This module is the entry point for the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()


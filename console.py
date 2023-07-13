#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
"""console application"""


class HBNBCommand(cmd.Cmd):
    """command interpreter """
    prompt = "(hbnb) "

    def do_create(self, line):
        """
            Creates a new instance of BaseModel, 
            saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")

    
    def do_quit(self, line):
        """commnad for quit"""
        return True

    def do_EOF(self, line):
        """enable contro d"""
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()

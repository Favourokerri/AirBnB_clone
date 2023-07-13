#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

"""console application"""


class HBNBCommand(cmd.Cmd):
    """command interpreter """
    prompt = "(hbnb) "

    def do_create(self, line):
        """
            Creates a new instance of BaseModel, 
            saves it (to the JSON file) and prints the id
        """
        if not line or line == "":
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
            Prints the string representation of an instance 
            based on the class name and id. 
            Ex: $ show BaseModel 1234-1234-1234.
        """
        if not line or line == "":
            print("** class name missing **")
        else:
            word = line.split(" ")
            if word[0] in storage.classes():
                if len(word) < 2:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(word[0], word[1])
                    if key not in storage.all():
                        print("** no instance found **")
                    elif key in storage.all():
                        print(storage.all()[key])
            else:
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

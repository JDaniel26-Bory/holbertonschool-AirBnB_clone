#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

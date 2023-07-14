#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User



class_names_str = [
    "BaseModel"
]
all_data = storage.all()


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    valid_classes = {"BaseModel"}

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()  # Print a newline before exiting
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass


    def do_create(self, args: str) -> None:
        """Create a new instance of BaseModel"""
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return

        # Process
        new_instance = eval(class_name)()

        new_instance.save()
        print(new_instance.id)
        

    def do_show(self, args: str) -> None:
        """ Method to show an individual object """

        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        # Process
        model = all_data.get(f"{class_name}.{instance_id}", None)

        if model is None:
            print("** no instance found **")
            return

        print(model)

    def do_destroy(self, args: str) -> None:
        """ Destroys a specified object """

        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        # Process
        try:
            all_data.pop(f"{class_name}.{instance_id}")
        except KeyError:
            print("** no instance found **")
            return

        storage.save()

    def do_all(self, args: Optional[str]) -> None:

        arg_list = args.split()
        if arg_list and arg_list[0] not in class_names_str:
            print("** class doesn't exist **")
            return
        try:  # if only write all
            class_name = arg_list[0]
        except Exception:
            pass

        # Process
        objects = [str(obj) for obj in all_data.values()  # if only write all
                   if args == "" or str(obj).startswith(f"[{class_name}]")]

        print(objects)


    def do_update(self, args: str) -> None:
        """Update an instance"""
        arg_list = args.split()
        if not arg_list:
            print("** class name missing **")
            return

        class_name = arg_list[0]

        if class_name not in class_names_str:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]

        instance = all_data.get(f"{class_name}.{instance_id}", None)

        if instance is None:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        is_dict = False
        for i in args:
            if i == '{':
                is_dict = True

        if is_dict:
            dicty = "".join(arg_list[2:])
            dictionary = eval(dicty)

            if (isinstance(dictionary, dict)):
                for key, value in dictionary.items():
                    setattr(instance, key, value)

                instance.save()
                return

        attribute_name = arg_list[2]
        attribute_value = eval(arg_list[3])

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** this attribute can't be change **")
            return

        setattr(instance, attribute_name, attribute_value)

        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

"""
This is a program that loops infinitely
"""

import sys

from Functions import client as cl
from Functions import manager as mn


def first_menu() -> None:
    """Show Menu"""
    print("\t_____________________________\n")
    print("\tWelcome to the Banking System")
    print("\t_____________________________\n")

    print("[1] Manager Menu")
    print("[2] Client Menu")
    print("[3] Exit")



while True:
    try:
        if mn.count_managers() <= 0:
            mn.create_manager()

    except NameError:
        print("Error in first statement")

    else:
        first_menu()
        command: int = abs(int(input("Enter Numbers(1-3): ")))
        cmd_len = len(str(command))

        # Validates commands
        while (cmd_len != 1) and (command is not int):
            first_menu()
            command: int = abs(
                int(input("Values Should be One Digit Long and Numbers(1-3): "))
            )
            cmd_len = len(str(command))

        if command == 1:
            mn.ManagerControl()
        elif command == 2:
            client = cl.ClientControl()
        elif command == 3:
            sys.exit()
        else:
            print("Invalid operation")

"""
Docstring for Functions manager
"""

import sys

from Data import datadb as db


def count_managers() -> int:
    """Count Managers"""
    n_managers: int = 0

    for list_managers in db.Manager.select():
        n_managers += 1

    return n_managers


def view_manager_acc() -> None:
    """View Managers"""
    count: int = 0
    for accounts in db.Client.select():
        count = +1
        print(f"[{count}]\t {accounts.Customer_Account}  _|_  {accounts.Name}")
    sys.exit()


def view_accounts() -> None:
    """View Client Accounts"""
    get_client = db.Client.select()
    for list_clients in get_client:
        print("-----------------------------------------------")
        print(f"Account Number: {list_clients.Customer_Account}")
        print(f"Client Name:  {list_clients.Name}")
        print(f"Client Balance: {list_clients.Balance}")
        print("-----------------------------------------------")
    sys.exit()


def delete_accounts() -> None:
    """Delete Accounts"""
    id_rem: int = int(input("Enter ID: "))
    delete_client = db.Manager.delete().where(db.Manager.Account == id_rem)
    delete_client.execute()
    sys.exit()


def create_manager() -> None:
    """Create New Managers"""
    print("\t__________________________\n")
    print("\tPlease Create New Manager")
    print("\t__________________________\n")

    manager_name: str = input("Please Enter Your Name: ")
    manager_password: int = abs(int(input("Please Enter a Four(4) Digit Pin: ")))
    digits_pass = len(str(manager_password))

    while digits_pass != 4:
        manager_password = abs(int(input("Please Enter a Four(4) Digit Pin: ")))
        digits_pass = len(str(manager_password))

    new_manager = db.Manager.create(Name=manager_name, Password=manager_password)
    new_manager.save()


def create_client() -> None:
    """Create New Clients"""
    client_name: str = input("Please Enter Your Name: ")
    client_password: int = abs(int(input("Please Enter a Four(4) Digit Pin: ")))
    digits_pass = len(str(client_password))

    while digits_pass != 4:
        client_password: int = abs(int(input("Please Enter a Four(4) Digit Pin: ")))
        digits_pass = len(str(client_password))

    print("Has Client Paid Initial deposit of $50?\n\t[1] Yes\n\t[2] No")
    validation = int(input("Enter Number(1-2): "))

    if validation == 1:
        new_client = db.Client.create(
            name=client_name, Password=client_password, Balance=0.00
        )
        new_client.save()

    else:
        sys.exit()


class ManagerControl(db.Manager):
    """Count Managers"""
    def __init__(self, *args, **kwargs):
        """Menu Selector"""
        super().__init__(*args, **kwargs)
        print("\t___________________________\n")
        print("\tWelcome to Managers Console")
        print("\t___________________________\n")

        print("[1] Create New Account")
        print("[2] View All Accounts")
        print("[3] Delete Account")
        print("[4] View Manager's Details")
        print("[5] Create New Manager")
        print("[6] Back to Main Menu")
        print("[7] Exit")

        command: int = abs(int(input("Enter Numbers(1-3): ")))
        cmd_len = len(str(command))

        # Validates commands
        while (cmd_len != 1) and (command is not int):
            command: int = abs(
                int(input("Values Should be One Digit Long and Numbers(1-3): "))
            )
            cmd_len = len(str(command))

        if command == 1:
            create_client()
        elif command == 2:
            view_accounts()
        elif command == 3:
            delete_accounts()
        elif command == 4:
            view_manager_acc()
        elif command == 5:
            create_manager()
        elif command == 6:
            pass
        elif command == 7:
            sys.exit()
        else:
            sys.exit()

"""
Docstring for functions client
"""

import sys

from Data import datadb as db


def withdraw() -> None:
    """Withdrawing funds"""
    p = 2
    print(f"{p} Hello World!")


def deposit() -> None:
    """Deposit Funds"""
    amount_deposit: int = int(input("Enter Deposit Amount: "))
    print(amount_deposit)
    # for addMoney in


def transact() -> None:
    """Exchange Funds"""
    print("Hello World!")


def check_balance() -> None:
    """Check Balance"""
    id_obj = int(input("Enter Account Number: "))
    balance = db.Client.select().where(db.Client.Customer_Account == id_obj)
    for get_balance in balance:
        print(
            f"{get_balance.Customer_Account}\n{get_balance.Name}\n{get_balance.Balance}"
        )


class ClientControl(db.Client):
    """Client Control"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing global class variable and first page"""
        super().__init__(*args, **kwargs)
        self.universal_account: int = 0
        self.client_input: int = 0

        print("\t________________\n")
        print("\tWelcome Customer")
        print("\t________________\n")

        print("Are you sure you want to continue?\n\t[1] Yes\n\t[2] No")

        # Goes to the verification function after completing this function
        command: int = int(input("Enter command: "))

        if command == 1:
            self.verify()
        elif command == 2:
            sys.exit()
        else:
            sys.exit()

    def verify(self) -> None:
        """Verifies the user"""
        pin_validation: int = 0
        self.universal_account = int(input("Enter Your Account Number: "))
        get_details = db.Client.select().where(
            db.Client.Customer_Account == self.universal_account
        )

        for show_details in get_details:
            print(
                f"Account Number: {show_details.Customer_Account} belongs to {show_details.Name}."
            )
            print("\t[1] Yes. \n\t[2] No")
            pin_validation = show_details.Password

        command: int = int(input("Are you sure you want to continue? "))

        if command == 1:
            pin: int = int(input("Enter your pin to validate your Request: "))

            if pin != pin_validation:
                print("Invalid Password :( ")
                sys.exit()
            else:
                print("Successfully logged in :D")
                self.menu_select_controls()
        elif command == 2:
            sys.exit()
        else:
            sys.exit()

    def menu_select_controls(self) -> None:
        """Menu Selection option for Clients"""
        print("\t___________________________\n")
        print("\tWelcome to Customer's Console")
        print("\t___________________________\n")

        print("[1] Deposit Money")
        print("[2] Withdraw Money")
        print("[3] Transfer Money")
        print("[4] Check Balance")
        print("[5] Exit")

        self.client_input = abs(int(input("Enter Numbers(1-3): ")))
        client_input_counter = len(str(self.client_input))

        # Validates input commands
        while (client_input_counter != 1) and (self.client_input is not int):
            self.client_input = abs(
                int(input("Values Should be One Digit Long and Numbers(1-3): "))
            )
            client_input_counter = len(str(self.client_input))

        if self.client_input == 1:
            deposit()
        elif self.client_input == 2:
            withdraw()
        elif self.client_input == 3:
            transact()
        elif self.client_input == 4:
            check_balance()
        elif self.client_input == 5:
            sys.exit()
        else:
            sys.exit()

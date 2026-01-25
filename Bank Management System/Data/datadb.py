"""
Connects to db
"""

from peewee import (
    Model,
    SqliteDatabase,
    AutoField,
    CharField,
    DecimalField,
    BooleanField,
    IntegerField,
)

db = SqliteDatabase("data.sqlite3")


class Manager(Model):
    """
    Creation of Manager Table
    """

    Account = AutoField()
    Name = CharField(30)
    Password = IntegerField()

    class Meta:
        """Meta"""

        database = db
        db_table = "Managers"


class Client(Model):
    """
    Creation of Client Table
    """

    Customer_Account = AutoField()
    Name = CharField(30)
    Balance = DecimalField(max_digits=12, decimal_places=2, auto_round=True)
    InitialDeposit = BooleanField(null=False, default=True)
    Password = IntegerField()

    class Meta:
        """Meta"""

        database = db
        db_table = "Client"




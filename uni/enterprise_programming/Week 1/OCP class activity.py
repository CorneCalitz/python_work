"""Look at the class below, check if it violates the open and close principle.
If so write the code such that it does not violate the principle anymore"""


class Account:

    def __init__(self, account_type, amount):

        self.account_type = account_type
        self.amount = amount

    def calculate_interest(self):

        if self.account_type == "Savings":
            return 0.1 * self.amount
        elif self.account_type == "Current":
            return 0.15 * self.amount
        elif self.account_type == "Credit":
            return 0.2 * self.amount
        elif self.account_type == "Business":
            return 0.5 * self.amount


"""Your Answer"""

from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def calc_interest(self):
        pass


class Savings(Account):
    def __init__(self, amount):
        super().__init__(amount)

    def calc_interest(self):
        return 0.1 * self.amount


class Current(Account):
    def __init__(self, amount):
        super().__init__(amount)

    def calc_interest(self):
        return 0.15 * self.amount


class Credit(Account):
    def __init__(self, amount):
        super().__init__(amount)

    def calc_interest(self):
        return 0.2 * self.amount


class Business(Account):
    def __init__(self, amount):
        super().__init__(amount)

    def calc_interest(self):
        return 0.5 * self.amount


"""Teacher's answer"""
"""This version does not require a super() call since there are no new properties being constructed once the 
subclasses are being created. Super() is only required if you are constructing new properties in the subclass"""
from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingAccount(Account):

    def calculate_interest(self):
        return 0.1 * self.amount


class CurrentAccount(Account):

    def calculate_interest(self):
        return 0.15 * self.amount


class CreditAccount(Account):

    def calculate_interest(self):
        return 0.2 * self.amount


class BusinessAccount(Account):

    def calculate_interest(self):
        return 0.5 * self.amount


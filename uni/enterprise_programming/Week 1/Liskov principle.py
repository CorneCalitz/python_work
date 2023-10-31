"""A child or subclass needs to be able to substitute a parent or base class without introducing bugs"""

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

# Liskov principle
def get_all_interest(accounts):
    interest = 0.0

    for account in accounts:
        interest += account.calculate_interest()

    print(interest)


accounts = [SavingAccount(1000), CurrentAccount(1000), CreditAccount(1000), BusinessAccount(1000)]
get_all_interest(accounts)


"""
Interface segeration principle
Classes should not be forced to depend upon function that they do not use
"""

"""Wrong implementation"""
from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldModelPrinter(Printer):
    def print(self, document):
        print(document)

    def fax(self, document):
        raise NotImplementedError("Printer does not have this functionality")

    def scan(self, document):
        raise NotImplementedError("Printer does not have this functionality")


class NewModelPrinter(Printer):
    def print(self, document):
        print(document)

    def fax(self, document):
        print(document)

    def scan(self, document):
        print(document)


"""Correct implementation"""
from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass


class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldModelPrinter(Printer):
    def print(self, document):
        print(document)


class NewModelPrinter(Printer, FaxMachine, Scanner):
    def print(self, document):
        print(document)

    def fax(self, document):
        print(document)

    def scan(self, document):
        print(document)

"""
The request from client applications should come in as a stand alone object.
Therefore , all transformations that should be performed on request should be done in the object
"""

from typing import List
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def CreateOrder(self, name, orderItems):
        pass


class OrderCommand(Command):
    def __init__(self, name, orderItems):
        self.name = name
        self.orderItems = orderItems

    def CreateOrder(self):
        totalPrice = 0.0
        for orderItem in self.orderItems:
            totalPrice += (orderItem.quantity * orderItem.unitPrice)

            return Order(self.name, self.orderItems, totalPrice)


class OrderItem:
    def __init__(self, productName, quantity, unitPrice):
        self.productName = productName
        self.quantity = quantity
        self.unitPrice = unitPrice


class Order:
    def __init__(self, name, orderItems: List[OrderItem], totalPrice: float):
        self.name = name
        self.orderItems = orderItems
        self.totalPrice = totalPrice


class OrderService:

    def __init__(self, command: Command):
        self.command = command

    def CreateOrder(self):
        return self.command.CreateOrder()


orderItems = [OrderItem("Coke", 2, 10), OrderItem("Milk", 1, 5)]

orderCommand = OrderCommand("fred", orderItems)
orderService = OrderService(orderCommand)

order = orderService.CreateOrder()

print(order.name)
for orderItem in orderItems:
    print(orderItem.productName)
    print(orderItem.unitPrice)
    print(orderItem.quantity)
print(order.totalPrice)

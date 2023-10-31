"""
You are building an online store where customers want to receive different types of sms, email and mobile notifications.
Create classes to simulate the observer pattern for this problem

    * Create a produce class that produces each of the notification types above
    * Create an Event notifier class for consumers to subscribe to notifications
    * Create at least one consumer class that will receive the notification types above
"""

from abc import ABC, abstractmethod


class Consumer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class NotificationService:
    def __init__(self):
        self.container = {}

    def subscribe(self, consumer: Consumer, event):
        if event in self.container:
            self.container[event].append(consumer)

        else:
            self.container[event] = [consumer]

    def unsubscribe(self, consumer: Consumer, event):
        if event in self.container:
            self.container[event].remove(consumer)

    def notify(self, event):
        for consumer in self.container[event]:
            consumer.update(event)


class SmsConsumer(Consumer):
    def update(self, message):
        print("Received sms")


class EmailConsumer(Consumer):
    def update(self, message):
        print("receive email")


class MobileConsumer(Consumer):
    def update(self, message):
        print("Mobile")


class Producer:
    def __init__(self, service: NotificationService):
        self.service = service

    def produceEvent(self, event):
        self.service.notify(event)


notificationService = NotificationService()

smsConsumer = SmsConsumer()
emailConsumer = EmailConsumer()

notificationService.subscribe(smsConsumer,"sms")
notificationService.subscribe(emailConsumer, "email")

producer = Producer(notificationService)

producer.produceEvent("sms")


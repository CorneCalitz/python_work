"""Singleton pattern
It states a class is allowed to only have a single instance for the lifetime of the application
"""

class Connection:

    _instance = None

    @staticmethod
    def getInstance():
        if Connection._instance is None:
            Connection()
        else:
            return Connection._instance

    def __init__(self):
        if Connection._instance != None:
            raise Exception("Connection instance already created.")
        else:
            Connection._instance = self
        self.connectionString = None

    def open(self, connectionString):
        self.connectionString = connectionString
        print("Connection is opened")

    def close(self):
        print("Connection is closed")

    @staticmethod
    def print_string():
        """A static method is not bound to the instance or the class and doesn't receive any special parameters.
        A static method can be called on the class itself or on an instance of the class."""
        print("Explaining static methods")


conn1 = Connection()
conn1.open("test")

conn2 = Connection()
conn2.open("dev")

print(conn1.connectionString)
print(conn2.connectionString)

Connection.print_string()




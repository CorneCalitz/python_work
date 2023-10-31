"""
Prototype pattern
Helps you hide the complexity in creating a replica of an object instance.
"""
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        """Return identical copy of function"""
        return copy.copy(self)


first = Point(6,7)
second = first.clone()

print(first)
print(second)

print(first.x)
print(first.y)
print(second.x)
print(second.y)
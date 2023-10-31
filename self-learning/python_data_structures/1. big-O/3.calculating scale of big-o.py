"""
We only care about the most significant terms in Big-O. As the input grows larger only the fastest growing terms will
matter. Similar to taking limits to infinity in calculus.
"""

def print_once(lst):

    for val in lst:
        print(val)
    print("END")

print_once([1,2,3])


def print_3(lst):

    for val in lst:
        print(val)

    for val in lst:
        print(val)

    for val in lst:
        print(val)

    print("END")

print_3([1,2,3])

"""
The first function will print O(n) items and the second will print O(3n) items. However for n going to infinity the
constant can be dropped, since it will not have a large effect, so both function are O(n)
"""

def complex_example(lst):
    """
    Prints the first item O(1)
    Prints the first 1/2 of the list O(n/2)
    Prints a string 10 times O(10)
    """

    print(lst[0])

    midpoint = len(lst) // 2

    for val in lst[:midpoint]:
        print(val)

    for x in range(10):
        print('number')

    print("END")


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
complex_example(lst)

"""
We can combine each operation to get the total Big-O of the function

        O(1 + n / 2 + 10)

1 and 10 terms become insignificant and the 1/2 term multiplied against n will also not have much value as n goes to
infinity. The function is simply O(n)

Many times we are only concerned with the worst possible case of an algorithm, but in an interview setting its important
to keep in mind that worst case and best case scenarios may be completely different Big-O times. For example, consider 
the following function:
"""

def matcher(lst,match):
    """Given a list lst, return a boolean indicating if match item is in the list"""
    for item in lst:
        if item == match:
            return True
    return False


print(matcher(lst,1))
print(matcher(lst,11))
"""
In the first scenario the best case was O(1) since the match was found in the first element.
In the case of no matches, every element must be checked, which results in a worst case time of O(n)
"""

"""
Space complexity is concerned with how much memory/space an algorithm uses. The notation remains exactly the same.
"""


def printer(n=10):
    """Prints "hello world!" n times"""
    for x in range(n):
        print('Hello World!')


printer()

"""
We only assign the string variable once, not every time we print. This algorithm has O(1) space complexity and
an O(n) time complexity
 """


def create_list(n):
    new_list = []

    for num in range(n):
        new_list.append('new')

    return new_list


print(create_list(5))

"""
Here the size of the new_list object scales with the input n, which shows that it is an O(n) algorithm with regards
to space complexity
"""





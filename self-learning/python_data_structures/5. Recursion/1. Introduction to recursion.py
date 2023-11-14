"""

Two instances of recursion.
First instance of recursion is as a technique in which a function makes one or more calls to itself.
Second is when a data structure uses smaller instances of the exact same type of data structure when it represents
itself.

Recursion occurs in the real world, such as fractal patters seen in plants.

Why use it?
Allows you to perform repetitions of tasks in where a loop is not ideal. Modern programming languages support recursion
and recursion serves as a great tool for building particular data structures.


Factorial example:

Factorial function is denoted with an exclamation point and is defined as the product of the integers from 1 to n.
    n! = n.(n-1).(n-2)... 3x2x1

NOTE: if n=0 then n!=1. This wil serve as our base case.

    4! = 4x3x2x1 = 24

We can state this in a recursive manner by using the concept the "base case". The base case is key to solving problems
with recursion. Rewrite the equation like this:
    4! = 4.(3.2.1) = 24

    This is the same as:
    4! = 4.3! = 24

    Meaning we can rewrite the formal recursion definition in terms of recursion like so:
    n! = n.(n-1)!

NOTE: if n = 0 then n! = 1. This means that the base case occurs once n=0, the recursive cases are defined in the
equation above. Whenever you are trying to develop a recursive solution it is important to think about the base case,
as your solution will need to return the base case once all the recursive cases have been worked through.

"""

def fact(n):
    """
    Returns factorial of n (n!).
    Use of recursion
    """

    # BASE CASE
    if n == 0:
        return 1

    # RECURSION
    else:
        return n * (fact(n-1))


print(fact(5))

# Figure depicting recursion
'http://faculty.cs.niu.edu/~freedman/241/241notes/recur.gif'



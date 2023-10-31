from timeit import timeit

"""
Lists

In python lists act as dynamic arrays and support a number of common operations through methods called on them.
Common operation are indexing and assigning to an index position. Both of these run in constant time. O(1)
"""

setup1 = """def method1():
    l = []
    for n in range(10000):
        l = l + [n]
        """


setup2 = """def method2():
    l = []
    for n in range(10000):
        l.append(n)
        """


setup3 = """def method3():
    l = [n for n in range(10000)]
    """


setup4 = """def method4():
    l = list(range(10000))
    """

print(timeit(stmt="method1()", setup=setup1, number=1))
print(timeit(stmt="method2()", setup=setup2, number=1))
print(timeit(stmt="method3()", setup=setup3, number=1))
print(timeit(stmt="method4()", setup=setup4, number=1))

"""
Common list operations with Big-O

Operation       |   Big-O Efficiency
-----------------------------------
index []        |   O(1)
index assignment|   O(1)
append          |   O(1)
pop()           |   O(1)
pop(i)          |   O(n)
insert(i,item)  |   O(n)
del operator    |   O(n)
iteration       |   O(n)
contains (in)   |   O(n)
get slice [x:y] |   O(k)
del slice       |   O(n)
set slice       |   O(n+k)
reverse         |   O(n)
concatenate     |   O(k)
sort            |   O(n log n)
multiply        |   O(nk)
----------------------------------

"""
"""
Dictionaries

Dictionaries are hash tables. They use keys and values. Getting and setting items in a dictionary is O(1) which makes 
hash tables a very efficient data structure.

Operation   |   Big-O Efficiency
---------------------------------
copy        |   O(n)
get item    |   O(1)
set item    |   O(1)
delete item |   O(1)
contains(in)|   O(1)
iteration   |   O(n)
"""











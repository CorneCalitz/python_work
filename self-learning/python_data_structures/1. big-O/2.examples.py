"""
O(1)
This function is constant because regardless of the list size, the function will only take a constant step size
A list of 100 values will print just 1 item and a list of n values will print just 1 item.
"""
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func_constant(values):
    """Prints first item in a list"""
    print(values[0])
    print("end of constant")


func_constant(data)


"""
O(log n)
Logarithmic time complexity is when the algorithm reduces the size of the input data in each step. (It does not need
to look at the values of the input data). Commonly found in binary trees and when using binary search.
"""

def func_logn(lst):
    for i in range(0, len(lst), 3):
        print(lst[i])
    print("end of logarithmic")


func_logn(data)


"""
O(n)
This function runs in O(n) (linear time). The number operation taking place scales linearly with n, so we can here that
an input list of 100 values will print 100 times. Thus, a list of n values will print n times. Best possible time
complexity if every needs to be examined.
"""

def func_lin(lst):
    """Takes in list and prints out all the values"""
    for val in lst:
        print(val)
    print("end of linear")


func_lin(data)


"""
O(n log n)
Algorithm is quasilinear when each operation in the input data have a logarithm time complexity. Often seen in sorting 
algorithms such as mergesort, timsort and heapsort.
"""

def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')


def func_quasi(lst1, lst2):
    result = []
    for val in lst1:
        result.append(binary_search(lst2, val))
        print(result[-1])
    print("end of quasi")

func_quasi([1, 6], data)


"""
O(n^2)
We have two loops and one is nested in the other. This means that for a list of n items, we will have to perform
n operations for every item in the list. This means in total, we will perform n times n assignments, or n^2. 
So a list of 10 items will have 10^2 or 100 operations. This can become very dangerous for large inputs; thus, 
1. big-O is so important.
"""

def func_quad(lst):
    """Prints pairs for every item in list"""
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)
    print("end of quadratic")


func_quad([0, 1, 2])


"""
O(n^3)
Cubic algorithm is similar to quadratic except it scales to the power of 3.
"""

def func_cubic(lst):
    for item1 in lst:
        for item2 in lst:
            for item3 in lst:
                print(item1,item2,item3)

    print("end of cubic")

func_cubic([1,2,3])


"""
O(2^n)
Exponential time complexity lets the growth double with each addition to the input data set. This type of complexity is
often seen in brute-force algorithms. The recursive fibonacci algorithm is an example.
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))
print("end of exponential")


"""
O(n!)
Grows in a factorial way based on the size of the input data. Heap's algorithm is a good example since. It is used to
generate all possible permutation of n objects.
"""

def heap_permutation(data, n):
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]

heap_permutation([1,2,3],len(data))



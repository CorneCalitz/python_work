"""
Problem

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

    5 is the missing number
"""

"""O(n^2) my solution"""


def finder(arr1, arr2):
    for num in arr1:
        if num not in arr2:
            return num


arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [9, 8, 7, 5, 4, 3, 2, 1]
print(finder(arr1, arr2))

"""O(nlogn) solution"""


def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    # otherwise return last element
    return arr1[-1]


arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr2 = [9, 8, 7, 5, 4, 3, 2, 1]
print(finder2(arr1, arr2))

"""O(n) solution (can find missing duplicates, relies on a hashtable)"""

import collections


def finder3(arr1, arr2):
    # using default dict to avoid errors
    d = collections.defaultdict(int)

    # add a count for every instance in array
    for num in arr2:
        d[num] += 1

    # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num

        # otherwise, subtract a count
        else:
            d[num] -= 1


arr1 = [5,5,7,7]
arr2 = [5,7,7]
print(finder3(arr1, arr2))


"""One possible solution is computing the sum of all the numbers in arr1 and arr2, and subtracting arr2’s sum from 
array1’s sum. The difference is the missing number in arr2. However, this approach could be problematic if the arrays 
are too long, or the numbers are very large. Then overflow will occur while summing up the numbers. 

By performing a very clever trick, we can achieve linear time and constant space complexity without any problems. 
Here it is: initialize a variable to 0, then XOR every element in the first and second arrays with that variable. In 
the end, the value of the variable is the result, missing element in array2. """


def finder4(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
        print(result)

    return result

arr1 = [5,5,7,7]
arr2 = [5,7,7]
print(finder4(arr1, arr2))
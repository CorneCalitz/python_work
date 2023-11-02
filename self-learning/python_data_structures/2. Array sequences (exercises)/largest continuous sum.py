"""
Given an array of integers (positive and negative) find the largest continuous sum.
"""

"""my solution O(n)"""


def large_cont_sum(arr):

    c = 0
    cont_sums_dict = {}
    cont_nums = []
    sum_val = int()

    # remove negative numbers at the start of the arr
    if arr[0] < 0:
        while c != len(arr):
            if arr[c] < 0:
                arr.pop(c)
                c += 1
            # once starting negative numbers removed exit loop
            else:
                break

    # for every number in array
    for num in arr:
        # creates sum value, creates a list of cont nums
        # adds sum value as key with cont_nums list as value
        sum_val += num
        cont_nums.append(num)
        cont_nums_copy = cont_nums.copy()
        cont_sums_dict[sum_val] = cont_nums_copy

    # finds max key and gives returns max value in list
    return max(cont_sums_dict.keys())


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))  # answer = 29
print(large_cont_sum([-1, 1]))  # answer = 1
print(large_cont_sum([1, 2, -1, 3, 4, -1]))  # a = 9


"""their solution O(n) (their solution only gives back the max sum, not the start and end)"""

def large_cont_sum2(arr):
    # Check to see if array is length 0
    if len(arr) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = arr[0]

    # For every element in array
    for num in arr[1:]:
        # Set current sum as the higher of the two
        current_sum = max(current_sum + num, num)

        # Set max as the higher between the currentSum and the current max
        max_sum = max(current_sum, max_sum)

    return max_sum


print(large_cont_sum2([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_cont_sum2([-1, 1]))

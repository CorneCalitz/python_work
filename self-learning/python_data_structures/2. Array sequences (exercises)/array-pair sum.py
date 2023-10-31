"""
Problem
Given an integer array, output all the ** unique ** pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

Solution
Fill out your solution below:
"""


def pair_sum(arr, k):
    pairs = []
    distinct_pairs = []

    for num1 in arr:
        for num2 in arr:
            if num1 + num2 == k:
                pairs.append([num1, num2])

    for pair in pairs:
        pair.sort()
        if pair not in distinct_pairs:
            distinct_pairs.append(pair)

    print(distinct_pairs)


pair_sum([1, 3, 2, 2], 4)
pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
pair_sum([0, 1, 3, 2, 2, 4], 2)


"""
Their solution
My solution uses an O(n^2) complexity whereas theirs has an O(n) complexity.
"""


def pair_sum_solution(arr, k):
    if len(arr) < 2:
        return

    # sets for tracking (Python sets do not contain duplicates and are unordered)
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target has not been seen
        if target not in seen:
            seen.add(num)

        else:
            # add a tuple with the corresponding pair
            output.add((min(num,target), max(num,target)))

    # For testing
    return "\n".join(map(str,list(output)))


print(pair_sum_solution([1,3,2,2],4))





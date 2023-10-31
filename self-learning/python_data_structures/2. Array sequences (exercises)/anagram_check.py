"""
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
"""

"""My solution"""
def anagram(word1, word2):

    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    if len(word1) != len(word2):
        return False

    for letter in word1:
        if letter not in word2:
            return False

    return True


print(anagram('clint eastwood','old west action'))


"""
Their solution
This solution has a O(n) time complexity since it relies on a count dictionary to see if letters are the same.
Mine has a O(n^2) time complexity since it uses two loops to find matching letters.
"""


def anagram2(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    # Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}

    # Fill dictionary for first string (add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True


print(anagram2("god","dog"))


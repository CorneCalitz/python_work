"""
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem,
you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1'
even though this technically takes more space.

The function should also be case-sensitive, so that a string 'AAAaaa' returns 'A3a3'."""

"""
my solution O(n^2)) compresses every character into one without considering position,
which is not the correct way to compress unless you save the position of characters.
"""


def compress(s):
    char_count = {}

    for char in s:
        if char not in char_count.keys():
            char_count[char] = 1

        else:
            char_count[char] += 1

    compressed_str = ''
    for key in char_count.keys():
        compressed_str += f'{key}{char_count[key]}'

    return compressed_str


print(compress(''))  # ''
print(compress('AABBCC'))  # A2B2C2
print(compress('AAABCCDDDDD'))  # A3B1C2D5
print(compress('AaB5a'))  # A1a2B151

"""their solution O(n) complexity"""


def compress2(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    # Initialize Values
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r


print(compress2(''))  # ''
print(compress2('AABBCC'))  # A2B2C2
print(compress2('AAABCCDDDDD'))  # A3B1C2D5
print(compress2('AaB5a'))  # A1a1B151a1

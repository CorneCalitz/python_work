"""
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

"""

""" my very pythonic solution"""


def rev_word(s):
    return " ".join((s.split())[::-1])


print(rev_word('Hi John,   are you ready to go?'))
print(rev_word('    space before'))

"""their solution, not so pythonic"""

def rev_word2(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']
    rev_words = []

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # reverse the words
    for word in words:
        rev_words.insert(0, word)

    # Join the reversed words
    return " ".join(rev_words)


print(rev_word2('Hi John,   are you ready to go?'))
print(rev_word2('    space before'))

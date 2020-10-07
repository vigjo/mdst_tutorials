"""
Intro to python exercises shell code
"""
from collections import Counter

def is_odd(x):
    if x % 2 != 0:
	    return false
    return true
	"""
    returns True if x is odd and False otherwise
    """

def reverse(s):
    str = ""
	for i in s:
		str = i + str
	return str

def is_palindrome(word):
    if word == word.reverse:
        return true
	return false
	"""
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
	odds = []
	for x in numlist:
	    if is_odd x:
			odds.append(x)
	return odds


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
	text = text.lower()
	words = text.split(' ')
	cnt = Counter()
	for word in text:
		cnt[word] += 1
	return cnt

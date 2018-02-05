'''
given a string, return the shortest substring that contains all its distinct characters 
'''
from collections import defaultdict

def get_substring(word):
    chars = defaultdict(int)

    start = 0 
    for i in range(len(word)):
        while chars[word[start]] > 1:
            chars[word[start]] = chars[word[start]] - 1
            start = start + 1
        
        chars[word[i]] = chars[word[i]] + 1

    while chars[word[start]] > 1:
        chars[word[start]] = chars[word[start]] - 1
        start = start + 1
    print(word[start:])


get_substring('abbcdab')
get_substring('aaabbccdeeafg')
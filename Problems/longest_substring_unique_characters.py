'''
given a string, find the longest substring with all the characters unique
'''


def longest_unique(word):
    locations = {}
    start = 0
    max_length = 0
    for i in range(len(word)):
        if word[i] in locations and locations[word[i]] >= start:
            max_length = max(max_length, i - start)
            start = locations[word[i]] + 1
        locations[word[i]] = i

    print(max(max_length, len(word) - start))


longest_unique('abcdalmbdlm')
longest_unique('abcdefal')

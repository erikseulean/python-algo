'''
1. Check if a string has all unique characters.
R. Use hashset to store the visited characters.
Whenever there's a character that is already in the set, return.
What if you cannot use additional memory?
Sort - using quicksort (nlogn)
Go and check if characters one after each other are unique.
If not return false
'''


def check_unique(s):
    if type(s) is not str:
        return False
    x = set()
    for i in s:
        if i in x:
            return False
        x.add(i)
    return True


assert check_unique('abracadabra') is False
assert check_unique('abcdefg') is True
assert check_unique(5) is False
assert check_unique('') is True
assert check_unique(' ') is True


def check_unique_sort(s):
    if type(s) is not str:
        return False
    s = sorted(s)
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


assert check_unique_sort('abracadabra') is False
assert check_unique_sort('abcdefg') is True
assert check_unique_sort(5) is False
assert check_unique_sort('') is True
assert check_unique_sort(' ') is True

print('all good in the hood')


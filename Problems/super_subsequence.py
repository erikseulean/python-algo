'''
Given 2 arrays, one with distinct numbers and one larger
Find the smallest supersequence that contains all the numbers in the smaller array.BaseException

Eg. 
small = {1, 5, 9}
large = {7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7}

anwser is large = {7, 5, 9, 0, 2, 1, 3, [5, 7, 9, 1], 1, 5, 8, 8, 9, 7}
'''
from collections import Counter

def go(start, end, array, data):
    while start < end and array[start] not in data:
        start += 1
    return start

def compute_subsequence(small, large):
    if len(small) == 0 or len(large) == 0:
        return []
    
    s_min, e_min = 0, len(large)

    data = Counter(small)
    required = len(small)

    start, end = 0, 0
    while end < len(large) and large[end] not in data:
        end += 1
    
    start = end
    required -= 1
    data[large[end]] -= 1
    for end in range(end + 1, len(large)):
        if large[end] in data:
            required -= data[large[end]] > 0
            data[large[end]] -= 1
        if required == 0: 
            if end - start < e_min - s_min:
               e_min, s_min = end, start
            data[large[start]] += 1
            required += data[large[start]] > 0
            start = go(start + 1, end, large, data)
    
    return large[s_min: e_min + 1]

print(compute_subsequence([1, 5, 9], [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]))

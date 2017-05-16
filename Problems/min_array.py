'''
Given 2 arrays, one with distinct numbers and one larger
Find the smallest supersequence that contains all the numbers in the smaller array.BaseException

Eg. 
small = {1, 5, 9}
large = {7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7}

anwser is large = {7, 5, 9, 0, 2, 1, 3, [5, 7, 9, 1], 1, 5, 8, 8, 9, 7}
'''

def find_supersequence(small, large):

    data = set(small)
    extra = dict()

    i = 0
    while i < len(large) and large[i] not in data:
        i += 1
    
    j = i + 1
    extra[large[i]] = i
    min_len = mini = minj = len(large) + 1

    while j < len(large):
        if large[j] in data and large[j] not in extra:
            extra[large[j]] = j
        if len(extra) == len(data):
            if min_len > j - i:
                min_len = j - i
                mini = i
                minj = j
            
            extra.pop(large[i])
            i += 1
            while i < j and large[i] not in data:
                i += 1
            if large[i] not in extra:
                extra[large[i]] = i
        else: 
            j += 1
    
    print(large[mini:minj+1])



find_supersequence([1, 5, 9], [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7])
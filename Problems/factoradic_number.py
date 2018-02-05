'''
https://www.quora.com/How-can-we-find-the-lexicographically-Kth-permutation-of-the-sequence-1-N-efficiently
get the factoradic number of a certain value
'''

def get_factoradic_number(nr):

    res = []
    i = 1
    while nr != 0:
        res.append(nr % i)
        nr = nr//i
        i = i + 1
    
    return res[::-1]

def get_kth_permutation(data, k):
    res = []
    factoradic_representation = get_factoradic_number(k)
    factoradic_representation = [0 for _ in range(len(data) - len(factoradic_representation))] + factoradic_representation
    print(factoradic_representation)
    for nr in factoradic_representation:
        res.append(data.pop(nr))
    return res + data


print(get_kth_permutation(['a','b','c','d'], 4))
'''
given an array, find the next permutation order lexicographycally
'''

def next_permutation(perm):

    i = len(perm) - 2
    while i >= 0 and perm[i] > perm[i+1]:
        i = i - 1

    if i < 0:
        return None

    j = len(perm) - 1
    while j > i and perm[j] <= perm[i]:
        j = j - 1
    
    if j == i:
        return None

    aux = perm[i]
    perm[i] = perm[j]
    perm[j] = aux

    return perm[:i+1] + perm[i+1:][::-1]

print(next_permutation([2,0,5,4,3,1]))
print(next_permutation([1,5,4,3,2]))
print(next_permutation([6,7,9,8]))
print(next_permutation([8,4,7,6,5,3,2]))


def check_anagram(first, second):
    count = [0 for i in range(0, 64)]
    for letter in first:
        count[ord(letter) - ord('a')] += 1

    for letter in second:
        count[ord(letter) - ord('b')] -= 1

    for letter in count:
        if letter is not 0:
            return False
    return True

anagram = ['alabala', 'malcala', 'rabala', 'shabala', 'balara', 'bacaine', 'caalalm']

sortedDict = sorted(anagram, cmp=check_anagram)

print(sortedDict)



anagram.sort(key=check_anagram)
print(anagram)

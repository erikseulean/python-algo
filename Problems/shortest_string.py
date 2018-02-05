'''
find the shortest substring that contains all the required characters
'''
from collections import defaultdict

def find_substring(characters, word):
    character_count = defaultdict(int)
    total_count = 0
    start = 0
    min_length = len(word)
    min_start, min_end = 0,0
    for i in range(len(word)):
        if word[i] in characters:
            if word[i] not in character_count or character_count[word[i]] < 1:
                total_count = total_count + 1
            character_count[word[i]] = character_count[word[i]] + 1
                
            while total_count == len(characters):
                if min_length > i - start:
                    min_length = i - start
                    min_start, min_end = start, i
                if word[start] in characters:
                    character_count[word[start]] = character_count[word[start]] - 1
                    if character_count[word[start]] < 1:
                        total_count = total_count - 1
                start = start + 1
                while word[start] not in characters:
                    start = start + 1
    
    print(word[min_start:min_end + 1])


#find_substring(set(['a', 'b', 'd']), 'abcefddalmbd')
#find_substring(set(['a', 'b', 'c']), 'mbalmpdabcl')




def shortest_substring(words, text):
    total, start, mstart, mend = 0, 0, 0, 0
    min_value = len(text)
    counts = defaultdict(int)
    for i in range(len(text)):
        if text[i] in words:
            counts[text[i]] = counts[text[i]] + 1
            if counts[text[i]] == 1:
                total = total + 1
            
            while total == len(words):
                if min_value > i - start:
                    min_value = i - start
                    mstart, mend = start, i
                
                if text[start] in words:
                    counts[text[start]] = counts[text[start]] - 1
                    if counts[text[start]] < 1:
                        total = total - 1
                start = start + 1
                while text[start] not in words:
                    start = start + 1

    return text[mstart: mend + 1] 

print(shortest_substring(set(['a', 'b', 'd']), 'abcefddalmbd'))
print(shortest_substring(set(['a', 'b', 'c']), 'mbalmpdabcl'))
print(shortest_substring(set(['a', 'b', 'c']), 'mbalmpdampzzzbcla'))


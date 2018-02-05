'''
given a list of words and a text, find the shortest subarray that contains all the words in the given order
'''

def compute_locations(words, text): #O(n + m)
    locations = [[] for _ in range(len(words))]
    indexes = { words[i]:i for i in range(len(words))}
    for i in range(len(text)):
        if text[i] in indexes:
            locations[indexes[text[i]]].append(i)
    
    return locations


def find_shortest_array(words, text):

    locations = compute_locations(words, text)

    current_positions = {}
    current_positions[-1] = -1
    current_positions[0] = -1
    max_length, mstart, mend = len(text), 0, 0
    while True: # O(m*k) m = words, k = max locations
        for i in range(len(words)):
            start = current_positions[i] if i in current_positions else 0
            if i == 0: 
                start = start + 1
            while i != 0 and start < len(locations[i]) and locations[i][start] < locations[i-1][current_positions[i-1]]:
                start = start + 1
            if start == len(locations[i]):
                return text[mstart: mend + 1]
            
            current_positions[i] = start
        if max_length > locations[-1][current_positions[len(words)-1]] - locations[0][current_positions[0]]:
            max_length = locations[-1][current_positions[len(words)-1]] - locations[0][current_positions[0]]
            mstart, mend = locations[0][current_positions[0]], locations[-1][current_positions[len(words)-1] ]


words = ['dog', 'cat', 'mouse']
text = '''
There is a cat on the tree. 
The dog is barking at it. The mouse is smart but not as smart as the dog . A cat tale. 
The mouse is laughing because the dog cannot get after the cat and the mouse is too smart.'''.split( )

#print(find_shortest_array(words, text))


def find_occurence(words, text):
    indexes = { words[i]:i for i in range(len(words))}
    last_location = {}
    dp = [-1 for _ in range(len(text))]
    min_value, mstart, mend = len(text), 0, 0
    for i in range(len(text)):
        if text[i] in indexes:
            last_location[indexes[text[i]]] = i
            if indexes[text[i]] == 0:
                dp[i] = 0
            elif indexes[text[i]] - 1 in last_location and dp[last_location[indexes[text[i]] - 1]] != -1:
                dp[i] = dp[last_location[indexes[text[i]] - 1]] + i - last_location[indexes[text[i]] - 1]
            else:
                dp[i] = -1
            if indexes[text[i]] == len(indexes) - 1:
                if dp[i] < min_value and dp[i] != -1:
                    min_value = dp[i]
                    mstart, mend = i - dp[i], i + 1
    
    return text[mstart:mend + 1]

#print(find_occurence(words, text))


def improved(words, text):
    indexes = { words[i]:i for i in range(len(words))}
    last_occurence = {}
    dp = [-1 for _ in range(len(words))]
    min_value, mstart, mend = len(text), 0, 0
    for i in range(len(text)):
        if text[i] in indexes:
            last_occurence[indexes[text[i]]] = i
            if indexes[text[i]] == 0:
                dp[0] = 0
            elif dp[indexes[text[i]] - 1] != -1:
                dp[indexes[text[i]]] = dp[indexes[text[i]] - 1] + i - last_occurence[indexes[text[i]] - 1] 
            else:
                dp[indexes[text[i]]] = -1
            
            if dp[indexes[text[i]]] != -1 and indexes[text[i]] == len(words) - 1 and min_value > dp[indexes[text[i]]]:
                min_value = dp[indexes[text[i]]]
                mstart, mend = i - dp[indexes[text[i]]], i + 1

    return text[mstart:mend]

print(find_shortest_array(words, text))
print(improved(words, text))                    
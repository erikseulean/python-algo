
def permute(s, mine, used):
    if len(mine) == len(s):
        print(mine)

    for elem in s:
        if elem not in used:
            mine += elem
            used.add(elem)
            permute(s, mine, used)
            used.remove(elem)
            mine = mine[:-1]


# permute('broasc', '', set())

def is_empty(wordmap):
    for key in wordmap:
        if wordmap[key] is not 0:
            return False
    return True

def word_permutation(word_map, current, perms):
    if is_empty(word_map):
        perms.append(current)
        return
    
    for key in word_map:
        if word_map[key] is not 0:
            word_map[key] -= 1
            word_permutation(word_map, current + key, perms)
            word_map[key] += 1

def word_map(word):
    _map = dict()
    for letter in word:
        if letter in _map:
            _map[letter] += 1
        else:
            _map[letter] = 1
    return _map

def permute_unique(word):
    data = []
    word_permutation(word_map(word), '', data)
    print(data)

permute_unique('abra')




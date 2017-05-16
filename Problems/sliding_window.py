'''
given a string return its compressed for
compression is nr of characters that are repeated in the sequence
in the previous window
'''

def running_sequence(word, i, j):
    count = 0
    while j < len(word) and word[i] == word[j]:
        count += 1
        i += 1
        j += 1
    
    return count

def get_max(word, start, size):
    back = max(0, start - size)
    max_compression, start_compression = -1, back
    for i in range(back, start):
        if word[i] == word[start]:
            run = running_sequence(word, i, start)
            if run >= max_compression:
                max_compression = run
                back = start - i
    if max_compression == -1:
        return 0,0,word[start]
    w = word[start + max_compression] if start + max_compression < len(word) else '^'
    return back, max_compression, w


def get_compression(word, window):
    if len(word) == 0 or window == 0:
        return word

    res = '(0,0)' + word[0]
    i = 1 
    while i < len(word):
        start, how_many, end_char = get_max(word, i, window)
        res += '({},{}){}'.format(start,how_many, (end_char if how_many == 0 else ''))
        print(res)
        i += max(how_many,1)
    
    return res

print(get_compression('aabcbbabc', 9))


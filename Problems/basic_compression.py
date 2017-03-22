'''
Having a string, compress it using the following trick:
aabcccaaa = a2b1c2a3. If the length of the initial string is smaller
then the compressed one, return the initial string.
'''


def compression(s):
    if type(s) is not str:
        return
    l = list()
    counter = 1
    l.append(s[0]) if len(s) > 0 else l.append('')
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            l.append(str(counter))
            l.append(s[i])
            counter = 1

    l.append(str(counter))
    word = ''.join(l)
    if len(word) < len(s):
        return word
    else: return s


assert compression('aabcccaaa') == 'a2b1c3a3'
assert compression('aaaaaaaaa') == 'a9'
assert compression('') == ''
assert compression('abcdefgh') == 'abcdefgh'
print('all good in the hood')


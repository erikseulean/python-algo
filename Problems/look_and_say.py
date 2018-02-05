'''
generate the nth element in the look and say word
'''

def look_and_say(n):

    word = '1'
    for k in range(1, n):
        counter = '1'
        current = word
        word = ''
        counter = 1
        digit = current[0]
        for i in range(1, len(current)):
            if current[i] == digit:
                counter = counter + 1
            else:
                word = word + str(counter)
                word = word + str(digit)
                digit = current[i]
                counter = 1
            
        word = word + str(counter)
        word = word + str(digit)
    
    return word
for i in range(1, 10):
    print(look_and_say(i))
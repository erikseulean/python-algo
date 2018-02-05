'''
given a number written as an array of digits. increment the number
'''


def increment(a):

    carry = 1
    for i in range(len(a)-1, -1, -1):
        carry, a[i] = (a[i] + carry)//10, (a[i] + carry) % 10
    
    if carry:
        a.insert(0, 1)
    
    return a

print(increment([1,3,9]))
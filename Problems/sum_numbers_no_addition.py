
def sum(a,b):
    carry = 0
    while b:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a

def sum_a(a,b):

    nr = a ^ b

    carry_nr = 0
    bit = 0
    counter = 0
    while a or b:
        bit = (a & b & 1) | (a & bit) | (b & bit)
        carry_nr = carry_nr | (bit<<counter)
        counter += 1
        a = a >> 1
        b = b >> 1
    carry_nr = carry_nr << 1
    nr = nr ^ carry_nr
    return nr

print(sum(17,27))
print(sum(15,3))
print(sum(15,15))
print(sum(42,24))
print(sum(8,2))
print(sum(1111,1))
print(sum(9999,1))
print(sum(10,10))
'''
    Count the number of digits(2) from 0 to n 
'''


def count_digits(nr):

    if nr < 2:
        return 0

    power = 1
    while power * 10 < nr:
        power *= 10

    msb = nr // power
    remaining = nr % power

    result = 0
    if msb > 2:
        result += power
    if msb == 2:
        result += remaining + 1

    result += msb * count_digits(power)
    result += count_digits(remaining)
    return result


print(count_digits(100))
print(count_digits(10))
print(count_digits(319))

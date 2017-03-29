'''
count the number of ways you can run up n stairs while you do 1,2 or 3 steps at a time
'''


def count_stairs(steps, n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    count = 0
    for step in steps:
        count += count_stairs(steps, n-step)
    return count


print(count_stairs([1, 2, 3], 4))

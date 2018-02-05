

def pascal_triangle(n):

    print([1])

    last, current = [], [1,1]

    for k in range(n-1):
        last = current
        print(last)
        current = []
        for i in range(len(last) + 1):
            if i == 0 or i == len(last):
                current.append(1)
            else:
                current.append(last[i-1] + last[i])


pascal_triangle(8)
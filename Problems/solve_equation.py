
def operation(first, second, op):
    if op is '+':
        return first + second
    if op is '-':
        return first - second
    if op is '*':
        return first * second
    if op is '/':
        return first/second


def solve(equation):

    signs = set(['-', '+', '*', '/'])
    number = None
    prev = None
    elem = []
    equation += '+'
    for it in equation:
        if it in signs:
            if prev is '*' or prev is '/':
                first = elem.pop()
                elem.append(operation(first, int(number), prev))
            else:
                if prev is not None:
                    elem.append(prev)
                elem.append(int(number))
            prev = it
            number = None
        else:
            number = number + it if number is not None else it

    res = elem[0]
    for i in range(1, len(elem)-1, 2):
        res = operation(res, elem[i+1], elem[i])

    return res


print(solve('2*3+5/6*3+15'))
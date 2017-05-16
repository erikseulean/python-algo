import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_inputs():
    number = 0
    items = []
    with open(os.path.join(__location__, "input.txt")) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        number = int(content[0])
        for i in range(0, number):
            line = content[i+1].split()
            elem = [int(data) for data in line]
            items.append(elem)

    return number, items


def unicorns():
    n, tests = read_inputs()
    for test in tests:
        stables = test[0]
        unicorns = test[1:]
        x = put_unicorns(stables, unicorns, '')
        print(x if x is not None else 'None')
    
d = {
    0: 'R',
    1: 'O',
    2: 'Y',
    3: 'G',
    4: 'B',
    5: 'V'
}

def put_unicorns(n, unicorns, now):
    if len(now) == n:
        return now
    print(now)
    max_next = 0
    max_i = 0        
    for i in range(0, 6):
        if unicorns[i] != 0:
            if max_next < unicorns[i]:
                print('here')
            if max_next < unicorns[i] and (now == '' or (len(now) == n-1 and now[0] != d[i] and now[len(now)-1] != d[i]) or (len(now) != n-1 and now[len(now)-1] != d[i])):
                max_next = unicorns[i]
                max_i = i
    
    unicorns[max_i] -= 1
    now = now + d[max_i]
    return put_unicorns(n, unicorns, now)


    unicorns()

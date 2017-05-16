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
            line = content[i+1]
            items.append(line)
    return number, items
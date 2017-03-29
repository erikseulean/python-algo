'''
given 2 lists, get all the intersections that maintain the relative order of the elements
'''


all_lists = []


def get_intersections(first, second, intermediary):
    if len(first) == 0 and len(second) == 0:
        all_lists.append(intermediary)
        return
    if len(first) != 0:
        next = intermediary.copy()
        next.append(first[0])
        get_intersections(first[1:], second, next)
    if len(second) != 0:
        next = intermediary.copy()
        next.append(second[0])
        get_intersections(first, second[1:], next)


def get_all():
    all_lists = []
    get_intersections([1, 2], [3, 4], [])
    print(all_lists)


if __name__ == "__main__":
    get_all()

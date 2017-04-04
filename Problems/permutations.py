
def permute(s, mine, used):
    if len(mine) == len(s):
        print(mine)

    for elem in s:
        if elem not in used:
            mine += elem
            used.add(elem)
            permute(s, mine, used)
            used.remove(elem)
            mine = mine[:-1]


permute('broasc', '', set())

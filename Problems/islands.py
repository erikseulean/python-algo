

lookup = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]

def in_matrix(i, j, n, m):
    return not (i < 0 or j < 0 or i >= n or j >= m)


def navigate(i, j, n, m, matrix):
    if not in_matrix(i, j, n, m) or matrix[i][j] != 0:
        return 0
    matrix[i][j] = -1
    island_size = 0
    for left, right in lookup:
        island_size += navigate(i + left, j + right, n, m, matrix)
    return 1 + island_size



def find_islands(matrix):
    n = len(matrix)
    m = len(matrix[0])

    lens = []
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 0:
                lens.append(navigate(i, j, n, m, matrix))
    print(lens)


matrix = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
find_islands(matrix)
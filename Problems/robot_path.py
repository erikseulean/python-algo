
def outside(i,j, n, m):
    return i >= n or j >=m


def robot_path(matrix, i, j, path):
    if outside(i,j, len(matrix), len(matrix[0])) or matrix[i][j] == 'x':
        return

    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        print(path)

    path.append((i, j))
    robot_path(matrix, i+1, j,path)
    robot_path(matrix, i, j+1, path)
    path.pop()


matrix = [
    [' ', 'x', ' ', ' '],
    [' ', 'x', ' ', ' '],
    [' ', ' ', ' ', 'x'],
    [' ', 'x', ' ', ' ']
]

robot_path(matrix, 0, 0, [])
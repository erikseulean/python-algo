


def generate_spiral_matrix(size):

    matrix = [[None for _ in range(size)] for _ in range(size)]

    k = 1
    for i in range(0, size):
        for j in range(0, size):
            matrix[i][j] = k
            k = k + 1
    
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))


#generate_spiral_matrix(4)


def another_spiral_matrix(size):
    counter = 1
    start_element = 0
    line_idx = 0
    column_idx = size - 1
    times = size - 1
    steps = size - 1
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    while times >= 1:
        for i in range(start_element, steps):
            matrix[line_idx][i] = counter
            counter = counter + 1
        for i in range(start_element, steps):
            matrix[i][column_idx] = counter
            counter = counter + 1
        for i in range(column_idx, size - steps - 1, -1):
            matrix[column_idx][i] = counter
            counter = counter + 1
        for i in range(column_idx, size - steps - 1, -1):
            matrix[i][line_idx] = counter
            counter = counter + 1
        start_element = start_element + 1
        line_idx = line_idx + 1
        column_idx = column_idx - 1
        times = times - 2
        steps = steps - 1
    
    if times == 0:
        matrix[size//2][size//2] = counter
    
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))


another_spiral_matrix(4)
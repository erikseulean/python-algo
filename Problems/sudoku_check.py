'''
check if unfinished sudoku is a valid combination
'''

def check_subsquare(matrix, start_index):
    numbers = set()
    for i in range(start_index, start_index+3):
        for j in range(start_index, start_index+3):
            if matrix[i][j] is None:
                continue
            if matrix[i][j] in numbers:
                return False
            else:
                numbers.add(matrix[i][j])
    
    return True


def check_row_column(matrix, index):
    row_numbers = set()
    column_numbers = set()
    
    for i in range(len(matrix)):
        if matrix[i][index] is not None:
            if matrix[i][index] in row_numbers:
                return False
            else:
                row_numbers.append(matrix[i][index])
        if matrix[index][i] is not None:
            if matrix[i][index] in column_numbers:
                return False
            else:
                column_numbers.append(matrix[index][i])
    
    return True


def check_sudoku(matrix):

    for i in len(matrix):
        if not check_row_column(matrix, i):
            return False
    
    gaps = sqrt(len(matrix))
    for i in range(0, len(matrix), gaps):
        if not check_subsquare(matrix, i):
            return False
    
    return True

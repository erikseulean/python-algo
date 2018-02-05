'''
rotate matrix clockwise. hate this problem :-)
'''


def rotate(matrix):
    n = len(matrix) - 1
    for i in range(len(matrix)//2):
        for j in range(i, len(matrix) - i - 1):
            aux = matrix[n - j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i] = matrix[i][j]
            matrix[i][j] = aux
    
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))


matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

rotate(matrix)
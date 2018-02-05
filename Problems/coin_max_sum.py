'''
given an array representing coin values, 2 players are picking alternatively from both ends of the array.
calculate the max sum a player can get
'''

def total(array):
    v = [[0 for _ in range(len(array))] for _ in range(len(array))]
    
    def max_sum(sum, i, j, player):
        if(i >= j):
            return v[i][j]
        if v[i][j] != 0:
            return v[i][j]

        if(player):
            v1 = max(max_sum(sum + array[i], i+2, j, !player), max_sum(sum + array[j], i+1, j-1, !player))
            v2 = max(max_sum(sum + array[j], i+1, j-1, !player), max_sum(sum + array[j], i, j-2, !player))
            v[i][j] = max(v1,v2)
        else:
            v[i][j] = max(max_sum(v[i-1][j]))
        return v[i][j]
    

    print(max_sum(0, 0, len(array) - 1))

total([4,9,2,1,7,3])
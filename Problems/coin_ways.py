

def get_ways(coins, n):

    arr = [0 for i in range(0, n+1)]
    arr[0] = 1

    for coin in coins:
        for amount in range(coin, n+1):
            arr[amount] += arr[amount - coin]
    return arr[n]


print(get_ways([5,10,25], 20))
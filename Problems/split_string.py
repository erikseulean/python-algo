'''
given a sentence that has its spaces removed, split the sentance in order to get the
least numbers of unknown characters

eg. jesslookedjustliketimherbrother
split it like: jess looked just like tim her brother
'''

def isValid(word):
    return word in set(['looked', 'just', 'like', 'her', 'brother'])

def split_sentance(sentance):

    if not isinstance(sentance, str) or len(sentance) == 0:
        return 

    dp = [ -1 for _ in range(len(sentance) + 1) ]

    dp[0] = 0

    backwards = {}

    for i in range(1, len(sentance) + 1):
        for j in range(i-1, -1, -1):
            word = sentance[j:i]
            extra = 0
            if not isValid(word):
                extra = i - j
            
            if dp[i] == -1 or extra + dp[j] < dp[i]:
                dp[i] = dp[j] + extra
                backwards[i] = j
            
    print(dp[len(sentance)])
        


split_sentance('jesslookedjustliketimherbrother')
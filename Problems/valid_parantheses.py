

def valid_parantheses(close, open, s):
    if close == 0:
        print(s)
        return

    if open > 0:
        s += '('
        valid_parantheses(close, open-1, s)
        s = s[:-1]
    if close > open:
        s += ')'
        valid_parantheses(close-1, open, s)
        s = s[:-1]


valid_parantheses(4, 4, '')

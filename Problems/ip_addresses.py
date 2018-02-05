'''
get all valid ip addresses out of a string
'''


def is_valid(number):
    return 0 <= int(number) and 255 >= int(number)

def valid_ips(ip):
    ips = []
    
    def get_ip(word, dots, current):
        if dots == 1:
            if is_valid(word):
                ips.append(current + '.' + word)
            return

        for i in range(1,len(word)):
            if is_valid(word[:i]):
                get_ip(word[i:], dots-1, current + '.' + word[:i] if len(current) != 0 else word[:i])
            else:
                return
    
    get_ip(ip, 4, '')
    print(ips)

valid_ips("19216811")
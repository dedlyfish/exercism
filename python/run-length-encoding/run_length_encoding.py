from itertools import groupby

def decode(string):
    prev = ''
    c = ''
    num = 1
    result = ''
    pairs = []
    for i in string:
        if not i.isdigit():
            pairs.append((i, num))
            num = 1
            c = ''
        else:
            c = c + i
            num = int(c)
        prev = i
    for i,k in pairs:
    	result += k * i
    return result


def encode(string):
    r=''
    for i,j in groupby(string):
        num = len(list(j))
        if num > 1:
            r += str(num)
        r += i
    return r


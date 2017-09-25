def decode():
    pass


def encode(string):
    res = ''
    num = 0
    c = string[0]
    for i in string:
    	if i==c:
    		num += 1
    	else:
    		if num>1:
    			res += str(num)+c
    		else:
    			res += c
    		c = i
    		num = 1
    return res

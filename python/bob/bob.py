def hey(string):
    if string.isupper():
        return 'Whoa, chill out!'
    if not string.strip():
    	return 'Fine. Be that way!'
    if string.strip()[-1] == '?':
    	return 'Sure.'
    return 'Whatever.'

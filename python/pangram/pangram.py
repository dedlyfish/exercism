def is_pangram(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
    	if not word.lower().count(i):
    		return False
    return True

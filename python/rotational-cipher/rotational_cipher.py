def rotate(string, r):

	def translate(letter):
	    if not letter.isalpha():
	            return letter
	    if letter.isupper():
	            return d[letter.lower()].upper()
	    return d[letter]

	alphabet='abcdefghijklmnopqrstuvwxyz'
	cipher=alphabet[r:] + alphabet[:r]
	d = dict(zip(alphabet, cipher))
	return "".join(list(map(translate,string)))

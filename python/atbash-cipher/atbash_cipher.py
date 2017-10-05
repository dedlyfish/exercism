alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
cipher_encode = dict(zip(alphabet + numbers, alphabet[::-1] + numbers))
cipher_decode = dict(zip(alphabet[::-1] + numbers, alphabet + numbers))

def encode(plain_text):
    s = "".join(map(lambda x: cipher_encode[x.lower()] if x.isalpha() or x.isdigit() else '', plain_text))
    return "".join([s[i:i+5] + ' ' for i in range(0, len(s), 5)]).strip()

def decode(ciphered_text):
    cipher = dict(zip(alphabet[::-1] + numbers, alphabet + numbers))
    return "".join(map(lambda x: cipher_decode[x] if x.isalpha() or x.isdigit() else '', ciphered_text))

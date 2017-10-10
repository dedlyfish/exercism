DICT = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
         10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eightteen', 19: 'nineteen' }

DOZENS = { 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety' }

def group(n):
    r = ''
    h = False
    if n // 100 > 0:
        r = DICT[n // 100] + ' hundred '
        h = True
    if (n % 100) < 20 and (n % 100) > 0:
        if h:
            r += ' and '
        r += DICT[n % 100]
        return r
    if (n % 100 // 10) > 0:
        if h:
            r += ' and '
        r += DOZENS[n % 100 // 10]
    if (n % 10) > 0:
        r += '-' + DICT[n % 10]
    return r


def say(num):
    if num == 0:
        return 'zero'
    if num < 0 or num > 999999999999:
        raise AttributeError('number not in range 0..999999999999')
    s = str(int(num)).zfill(12)
    r = []
    out = ''
    for i in range(0,10,3):
        r.append(int(s[i:i+3]))
    if r[0] > 0:
        out += group(r[0]) + ' billion '
    if r[1] > 0:
        out += group(r[1]) + ' million '
    if r[2] > 0:
        out += group(r[2]) + ' thousand '
    if r[3] > 0:
        if r[2] == 0 and (r[1] > 0 or r[0] > 0):
            out += ' and '
        out += group(r[3])
    return out.strip().replace('  ',' ')

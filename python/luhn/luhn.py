class Luhn(object):
    def __init__(self,string):
        self.num = string.replace(' ','')[::-1]
    def is_valid(self):
        s = 0
        if len(self.num) > 1:
            for i in range(1, len(self.num)+1):
                if not self.num[i-1].isdigit():
                    return False
                t = int(self.num[i-1])
                if i % 2 == 0:
                    t *= 2
                    if t > 9:
                        t -= 9
                s += t
            if s % 10 == 0:
                return True
        return False

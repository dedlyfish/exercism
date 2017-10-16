def flatten(iterable):
    r = []
    def fltr(l):
        for i in l:
                if isinstance(i, list):
                        fltr(i)
                elif (i != None) and (i != ()):
                        r.append(i)
    fltr(iterable)
    return r

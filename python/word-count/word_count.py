def word_count(str):
    words = ''.join(list(filter(lambda x: x.isalnum() or x.isspace() or x=='_' or x==',', str))).lower().replace('_',' ').replace(',',' ').split()
    d = {}
    for i in words:
    	d[i] = words.count(i)
    return d

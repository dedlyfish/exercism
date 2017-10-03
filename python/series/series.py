def slices(str, num):
    if (num > len(str)) or (num == 0):
        raise ValueError("Invalid input")
    r = []
    for i in range(len(str) - num + 1):
        r.append(list(map(lambda x: int(x), str[i:num + i])))
    return r
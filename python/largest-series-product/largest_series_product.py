from functools import reduce

def largest_product(series, size):
    if (series == '' and size > 0) or (size < 0) or (size > len(series)):
        raise ValueError();
    if series == '' or size == 0:
        return 1
    values = []
    for i in range(len(series) - size + 1):
        values.append(reduce(lambda x,y: int(x) * int(y), series[i: i + size]))
    return max(values)

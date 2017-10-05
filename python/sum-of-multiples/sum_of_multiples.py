def sum_of_multiples(num, multiples):
    r = []
    for i in range(1, num):
        if not all(list(map(lambda x: True if i % x else False, multiples))):
            r.append(i)
    return sum(r)

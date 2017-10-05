def sum_of_multiples(num, multiples):
    r = []
    for i in range(1, num):
        if sum(list(map(lambda x: 1 if i % x else 0, multiples))) <= len(multiples) - 1:
            r.append(i)
    return sum(r)

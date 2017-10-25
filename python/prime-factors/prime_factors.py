def prime_factors(natural_number):
    out = []
    d = 2
    while natural_number > 1:
        if natural_number % d == 0:
            out.append(d)
            natural_number = natural_number // d
        else:
            d += 1
    return out

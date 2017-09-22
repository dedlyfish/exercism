def distance(dna1,dna2):
    if len(dna1) != len(dna2):
        raise ValueError("DNA length doesn't match")
    return sum(map(lambda a,b: a!=b, dna1, dna2))


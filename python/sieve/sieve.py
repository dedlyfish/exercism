def sieve(num):
    a = [True] * (num + 1)
    for i in range(2, num + 1):
        for j in range(i*2, num + 1, i):
            a[j] = False
    return [i for i in range(2,num + 1) if a[i]]
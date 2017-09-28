def detect_anagrams(word, array):
    res = []
    for i in array:
        if (sorted(word.lower()) == sorted(i.lower())) and (word.lower() != i.lower()):
            res.append(i)
    return res

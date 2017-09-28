def detect_anagrams(word, array):
    res = []
    for i in array:
            is_anagram = True
            for j in i:
                    if (len(word) != len(i)):
                        is_anagram = False
                        break
                    if (word.lower().count(j) != i.lower().count(j)) or (word.lower() == i.lower()):
                        is_anagram = False
                        break
            if is_anagram:
                res.append(i)
    return res

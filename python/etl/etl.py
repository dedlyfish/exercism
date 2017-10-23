def transform(legacy_data):
    r = {}
    for i in legacy_data:
        for j in legacy_data[i]:
            r[j.lower()] = i
    return r

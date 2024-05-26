def intersection(a, b):
    out = []
    iA, iB = 0, 0

    while iA < len(a) and iB < len(b):
        eleA, eleB = a[iA], b[iB]
        if eleA < eleB:
            iA += 1
        elif eleB < eleA:
            iB += 1
        else:
            out.append(eleA)
            iA, iB = iA + 1, iB + 1

    return out


foo = [1, 2, 3, 4]
bar = [3, 4, 5]
print(intersection(foo,bar))

def find_duplicates(lst):
    n = len(lst)

    count = [0] * n

    for i in lst:
        count[i] += 1

    out = []

    for i in range(len(count)):
        if count[i] > 1:
            out.append(i)
            
    return out


'''
lst = [2, 4, 4, 1, 2]
print(find_duplicates(lst))
'''
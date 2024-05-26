def SortLst(lst):
    count = [0] * len(lst)
    out = []

    for i in lst:
        count[i] += 1

    index = 0
    for i in range(len(count)):
        for j in range(count[i]):
            lst[index] = i
            index += 1


lst = [2, 0, 2, 1, 1, 2]
SortLst(lst)
print(lst)

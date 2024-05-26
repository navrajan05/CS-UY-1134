import copy


def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    else:
        out = []
        priorPerms = permutations(lst, low, high - 1)
        for perm in priorPerms:
            for index in range(len(perm) + 1):
                myArray = copy.copy(perm)
                myArray.insert(index, lst[high])
                out.append(myArray)
        return out


'''
lst = [1, 2, 3, 4]
print(permutations(lst, 0, 2))
'''

def remove_all(lst, value):

    back = [0] * len(lst)
    removed = 0

    for i in range(len(lst)):
        back[i] = removed
        if lst[i] == value:
            removed += 1

    for i in range(len(lst)):
        lst[i - back[i]] = lst[i]

    for i in range(removed):
        lst.pop()

    return lst




'''
myList = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9]
print(myList)
remove_all(myList, 5)
print(myList)
'''
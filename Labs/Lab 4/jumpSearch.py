from math import sqrt


def jump_search(lst, val):

    k = int(sqrt(len(lst))) + 1

    index = k - 1
    while index < len(lst):
        if lst[index] >= val:
            found = False
            for i in range(k):
                temp = index - i
                if lst[temp] == val:
                    return temp
            return None
        index += k

    index -= k
    while index < len(lst):
        if lst[index] == val:
            return index
        index += 1
    return None


arr = [1, 3, 6, 7, 10, 12, 15, 20, 22, 24, 29, 33, 39, 55, 61, 64, 99, 101, 134, 150]
print(jump_search(arr, 22))
def reverse_list(lst, low = None, high = None):

    if low == None:
        first = 0
    else:
        first = low

    if high == None:
        last = len(lst) - 1
    else:
        last = high

    while first < last:
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1


    return lst

def shift(lst, k):

    lst1 = lst[:k]
    lst2 = lst[k:]

    return lst2 + reverse_list(lst1)


print(shift([1, 2, 3, 4, 5, 6], 2))
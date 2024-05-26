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

lst = [1, 2, 3, 4, 5, 6]
low = 1
high = 3

print(reverse_list(lst, low, high))

def nested_sum(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total


lst = [[1, 2], 3, [4, [5, 6, [7], 8]]]
print(nested_sum(lst))
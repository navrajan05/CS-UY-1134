def split_parity(lst):
    # no second pointer needed, moving all the odds left sends evens right
    odd_index = 0
    i = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst[i], lst[odd_index] = lst[odd_index], lst[i]
            odd_index += 1


lst = [1, 3, 5, 6, 4, 34, 5, 3, 4, 2, 5, 2, 2, 4, 1, 4, 4, 3, 5]
split_parity(lst)
print(lst)

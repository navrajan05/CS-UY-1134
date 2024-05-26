def split_parity(lst, low, high, even_index=None):

    if even_index is None:
        even_index = low

    if low > high:
        return lst
    else:

        if lst[low] % 2 == 0:
            lst[low], lst[even_index] = lst[even_index], lst[low]
            even_index += 1

        split_parity(lst, low + 1, high, even_index)


lst = [4, -5, 2, 3, -1, -6, 7, 9, 0]
split_parity(lst, 0, len(lst) - 1)
print(lst)
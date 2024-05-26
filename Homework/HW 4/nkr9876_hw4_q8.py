def flat_list(lst, low, high):
    if low > high:
        return []
    else:
        val = lst[high]
        out = flat_list(lst, low, high - 1)
        if isinstance(val, list):
            x = flat_list(val, 0, len(val) - 1)
            out.extend(x)
        else:
            out.append(val)

        return out

'''
nested_lst=[[1, 2], 3, [4, [5, 6, [7], 8]]]
print(flat_list(nested_lst,0,2))
'''
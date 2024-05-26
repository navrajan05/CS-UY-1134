def nested_depth_level(lst):
    if not isinstance(lst, list):
        return 0
    else:
        depths = [0] * len(lst)
        maximum = 0
        for i in lst:
            maximum = max(maximum, nested_depth_level(i))

        return maximum + 1


lst1 = [1, 2]
lst2 = [[1], 2]
lst3 = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]

print(nested_depth_level(lst1), nested_depth_level(lst2), nested_depth_level(lst3))
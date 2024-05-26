def binary_search(arr, val, left, right):
    if right >= left:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return binary_search(arr, val, left, mid - 1)
        else:
            return binary_search(arr, val, mid + 1, right)
    else:
        return -1


def find_pivot(lst):
    left = 0
    right = len(lst) - 1

    out = 0;
    breakout = False
    while not breakout:
        mid = (left + right) // 2
        if lst[mid] < lst[mid - 1]:
            out = mid
            breakout = True
        elif lst[mid] < lst[left]:
            right = mid - 1
        else:
            left = mid + 1
        if left > right:
            breakout = True

    if out == 0: out = None
    return out


def shift_binary_search(lst, target):
    pivot = find_pivot(lst)
    if pivot is not None:
        out1 = binary_search(lst, target, 0, pivot - 1)
        out2 = binary_search(lst, target, pivot, len(lst) - 1)
        return max(out1, out2)
    else:
        return binary_search(lst, target, 0, len(lst))


nums = [15, 20, 21, 1, 3, 6, 7, 10, 12, 14]

print(find_pivot(nums))
print(shift_binary_search(nums, 7))

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


myArr = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(myArr, 6, 0, 6))

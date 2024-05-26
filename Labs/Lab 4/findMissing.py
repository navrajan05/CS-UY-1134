def find_missing_sorted(lst):
    left = 0
    right = len(lst) - 1

    while True:
        mid = left + right // 2
        if left > right: break

        if lst[mid] != mid and lst[mid - 1] == mid - 1:
            return mid
        elif lst[mid] == mid:
            left = mid + 1
        elif lst[mid] != mid:
            right = mid - 1


def find_missing_unsorted(lst):
    expected = len(lst) * (len(lst) + 1) /2
    actual = sum(lst)

    return int(expected - actual)


myList = [0, 1, 2, 3, 4, 5, 6, 8]

print(find_missing_sorted(myList))
print(find_missing_unsorted(myList))
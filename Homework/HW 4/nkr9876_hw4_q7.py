def split_by_sign(lst, low, high):
    if low <= high:
        if lst[low] > 0 and lst[high] < 0: lst[low], lst[high] = lst[high], lst[low]
        if lst[low] < 0: low += 1
        if lst[high] > 0: high -= 1
        split_by_sign(lst, low, high)

'''
myList = [i for i in range(1, 16)]

import random
for i in range(len(myList)):
    myList[i] *= random.choice([1, -1])

print(myList)
split_by_sign(myList, 0, len(myList) - 1)
print(myList)
'''
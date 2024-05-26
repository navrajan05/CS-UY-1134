def maxSub(lst, k):
    p1 = 0
    p2 = k


    length = len(lst)

    max = 0
    for i in lst[:k]:
        max += i
    current = max

    while p2 < length:
        val = current + lst[p2] - lst[p1]
        current = val
        if val > max:
            max = val

        p1 +=1
        p2 +=1

    return max

nums = [1,12,-5,-6,50,3]
k = 3

print(maxSub(nums, k))

def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1

    # greedy solution with two pointers
    while left < right:
        total = srt_lst[left] + srt_lst[right]
        if total == target:
            return (left, right)
        elif total < target:
            left += 1
        elif total > target:
            right -= 1

    return None


'''
lst = [-2, 7, 11, 15, 20, 21]
tar = 22

print(two_sum(lst, tar))
'''

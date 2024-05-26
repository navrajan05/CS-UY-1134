def move_zeroes(nums):
    i1 = 1
    i2 = 0
    length = len(nums)

    while i1 < length:
        if nums[i1] != 0:
            if nums[i2] != 0:
                i2 +=1
            else:
                nums[i2], nums[i1] = nums[i1], nums[i2]
        else:
            i1 += 1

    return nums
print(move_zeroes([0, 1, 0, 3, 13, 0]))
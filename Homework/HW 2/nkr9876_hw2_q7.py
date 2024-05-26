def findChange(lst01):

    left, right = 0, len(lst01) - 1
    breakout = False

    out = None

    # pretty much just binary search
    while not breakout:

        mid = (left + right) // 2

        if lst01[mid] == 1 and lst01[mid - 1] == 0: out, breakout = mid, True
        elif lst01[mid] == 1: right = mid - 1
        else: left = mid + 1

        if left > right:
            breakout = True

    return out


'''
myList = [0, 0, 0, 0, 0, 1, 1, 1]
print(findChange(myList))
'''

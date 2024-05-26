def appearances(s, low, high):
    if low > high:
        return {}
    else:
        log = appearances(s, low + 1, high)
        char = s[low]

        if char in log:
            log[char] += 1
        else:
            log[char] = 1

        return log


'''
myString = "Are you suggesting coconuts migrate?"
print(appearances(myString, 0, len(myString) - 1))
print(len(myString))
'''
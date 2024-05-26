def sumSquares(n):
    sum = 0
    for i in range(n):
        sum += (i * i)
    return sum


def sumSquares2(n):
    return sum([i * i for i in range(n)])


def sumOddSquares(n):
    sum = 0
    for i in range(1, n, 2):
        sum += (i * i)
    return sum


def sumOddSquares2(n):
    return sum([i * i for i in range(1, n, 2)])

'''
print(sumSquares(7))
print(sumSquares2(7))

print(sumOddSquares(7))
print(sumOddSquares2(7))
'''
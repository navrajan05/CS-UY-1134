def isPowerOfTwo(x):
    if x == 1:
        return True
    else:
        div2 = x % 2 == 0
        half2pow = isPowerOfTwo(x // 2)
        return div2 and half2pow

for i in range(1,9):
    print(str(i),str(isPowerOfTwo(i)))

def fibs(n):
    prev = 0
    curr = 1
    for i in range(n):
        yield curr
        prev, curr = curr, curr + prev


'''
for curr in fibs(8):
    print(curr)
'''
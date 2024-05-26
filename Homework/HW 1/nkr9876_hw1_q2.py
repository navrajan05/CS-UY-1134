def shift(lst, k, direction='left'):

    if direction == 'left':
        for i in range(k):
            lst.append(lst.pop(0))
    else:
        for i in range(k):
            lst.insert(0, lst.pop(-1))

'''
m = [1,2,3,4,5,6]
shift(m, 2, 'right')
print(m)
'''
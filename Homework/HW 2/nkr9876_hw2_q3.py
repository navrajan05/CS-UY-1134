from math import sqrt, ceil, floor

def factors(n):
    root_n = sqrt(n)

    '''
    ceil and floor are used to handle square 
    numbers properly without double counting 
    the square root. you could also hardcode
    the algorithm to handle them correctly,
    but this felt more elegant.
    '''

    for i in range(1, ceil(root_n), 1):
        if n % i == 0: yield i

    for i in range(floor(root_n), 0, -1):
        if n % i == 0:
            yield int(n / i)


'''
for i in factors(112):
    print(i)
'''

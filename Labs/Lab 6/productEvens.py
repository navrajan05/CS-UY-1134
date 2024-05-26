def product_evens(n):
    if n == 2: return n
    else: return n * product_evens(n-2)

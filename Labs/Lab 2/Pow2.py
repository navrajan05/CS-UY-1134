def powers_of_two(n):
    for v in range(n):
        yield pow(2, v)


for i in powers_of_two(6):print(i)

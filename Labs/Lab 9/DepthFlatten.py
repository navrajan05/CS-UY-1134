from Queues import ArrayQueue


def depth_flatten(lst):
    myQ = ArrayQueue()
    out = []
    for i in lst:
        myQ.enqueue(i)

    while len(myQ) > 0:
        x = myQ.dequeue()
        if isinstance(x, list):
            for i in x:
                myQ.enqueue(i)
        else:
            out.append(x)

    return out


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
print(depth_flatten(lst))

from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import copy

def permutations(lst):
    values = ArrayStack()

    for i in range(len(lst)): values.push(lst[i])

    permutation_queue = ArrayQueue()
    permutation_queue.enqueue([])

    while values.is_empty() is not True:

        x = values.pop()
        n = len(permutation_queue)

        for element in range(n):
            p = permutation_queue.dequeue()
            for index in range(len(p) + 1):
                newP = copy.copy(p)
                newP.insert(index, x)
                permutation_queue.enqueue(newP)

    out = []
    while permutation_queue.is_empty() is not True:
        out.append(permutation_queue.dequeue())

    return out


lst = [1, 2, 3]
print(permutations(lst))
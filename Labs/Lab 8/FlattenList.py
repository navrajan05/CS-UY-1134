from ArrayStack import *


def flatten_list(lst):
    stack = ArrayStack()
    while len(lst) > 0:
        x = lst.pop()
        if isinstance(x, list):
            lst.extend(x)
        else:
            stack.push(x)

    while not stack.is_empty():
        lst.append(stack.pop())


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
flatten_list(lst)
print(lst)

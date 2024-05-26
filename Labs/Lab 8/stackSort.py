import random

from ArrayStack import ArrayStack



def stack_sort_alternate(s):
    actions = 0
    helperStack = ArrayStack()

    while not s.is_empty():
        x = s.pop()
        while not helperStack.is_empty() and x < helperStack.top():
            actions += 1
            s.push(helperStack.pop())
        helperStack.push(x)

    while not helperStack.is_empty():
        s.push(helperStack.pop())
    print(actions)
def stack_sort(s):
    helperStack = ArrayStack()
    L = len(s)
    n = None
    for i in range(L):
        iter = L - i
        max = None
        #print(iter)
        out = []
        for j in range(iter):

            n = s.pop()
            out.append(n)
            if max is None:
                max = n
            elif n > max:
                helperStack.push(max)
                max = n
            else:
                helperStack.push(n)

        s.push(max)
        #print(max, out)
        while not helperStack.is_empty():
            s.push(helperStack.pop())

myStack = ArrayStack()

values = []
for i in range(32):
    values.append(random.randint(1,101))

for i in values:
    myStack.push(i)

stack_sort_alternate(myStack)

print(values)
'''
print()
while not myStack.is_empty():
    print(myStack.pop())
'''
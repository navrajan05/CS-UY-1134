from ArrayStack import *
def stackSum(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        out = stackSum(s) + val
        s.push(val)
        return out

s = ArrayStack()
s.push(1)
s.push(2)
s.push(4)
s.push(8)
print(stackSum(s))
print(stackSum(s))
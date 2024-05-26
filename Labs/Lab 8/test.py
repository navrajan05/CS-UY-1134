from ArrayStack import *

s = ArrayStack()
i=2
s.push(1)
s.push(2)
s.push(4)
s.push(8)
i += s.top()
s.push(i)
s.pop()
s.pop()
print(i)
print(s.top())
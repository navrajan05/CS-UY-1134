from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()

    def is_empty(self):
        return self.stack.is_empty()

    def __len__(self):
        return len(self.stack)

    def top(self):
        if self.is_empty(): raise Exception("MaxStack is empty!")
        return self.stack.top()[0]

    def pop(self):
        if self.is_empty(): raise Exception("MaxStack is empty!")
        top = self.stack.pop()[0]
        return top

    def push(self, val):
        if self.is_empty():
            self.stack.push((val, val))
        else:
            self.stack.push((val, max(self.max(), val)))

    def max(self):
        if self.is_empty():
            raise Exception("stack is empty!")
        else:
            maxi = self.stack.top()[1]
            return maxi

'''
maxS = MaxStack()

maxS.push(3)
maxS.push(1)
maxS.push(6)
maxS.push(4)

print(maxS.max())
print(maxS.pop())
print(maxS.pop())
print(maxS.max())
'''
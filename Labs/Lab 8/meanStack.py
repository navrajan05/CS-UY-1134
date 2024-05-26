from ArrayStack import *

class MeanStack:
    
    def __init__(self):
        self.stack = ArrayStack()
        self.total = 0

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, e):
        if isinstance(e, int):
            self.stack.push(e)
            self.total += e
        else:
            raise ValueError

    def pop(self):
        var = self.stack.pop()
        self.total -= var
        return var

    def top(self):
        return self.stack.top()

    def sum(self):
        return self.total

    def mean(self):
        return self.total/len(self)
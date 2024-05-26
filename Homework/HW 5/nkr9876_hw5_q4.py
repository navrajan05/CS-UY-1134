
from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.mainStack = ArrayStack()
        self.reverseStack = ArrayStack()

    def enqueue(self, val):
        self.mainStack.push(val)

    def first(self):
        if self.reverseStack.is_empty():
            while self.mainStack.is_empty() is False:
                self.reverseStack.push(self.mainStack.pop())

        return self.reverseStack.top()

    def is_empty(self):
        return self.mainStack.is_empty() and self.reverseStack.is_empty()

    def __len__(self):
        return len(self.mainStack) + len(self.reverseStack)

    def dequeue(self):
        if self.reverseStack.is_empty():
            while self.mainStack.is_empty() is False:
                self.reverseStack.push(self.mainStack.pop())

        return self.reverseStack.pop()
from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.topStack = ArrayDeque()
        self.bottomStack = ArrayStack()

    def __len__(self):
        return len(self.topStack) + len(self.bottomStack)

    def is_empty(self):
        return len(self) == 0

    def pop(self):
        if self.is_empty(): raise Exception("MidStack is empty")
        if self.topStack.is_empty():
            self.topStack.enqueue_last(self.bottomStack.pop())

        out = self.topStack.dequeue_first()
        self.__balance()
        return out

    def push(self, val):
        self.topStack.enqueue_first(val)
        self.__balance()

    def top(self):
        if self.is_empty(): raise Exception("MidStack is empty")
        return self.topStack.first()

    def mid_push(self, val):
        self.bottomStack.push(val)
        self.__balance()


    def __balance(self):

        top_len_golden = len(self) - ((len(self) + 1) // 2)

        while len(self.topStack) != top_len_golden:
            if len(self.topStack) > top_len_golden:
                self.bottomStack.push(self.topStack.dequeue_last())
            else:
                self.topStack.enqueue_last(self.bottomStack.pop())

'''

midS = MidStack()
midS.push(2)
midS.push(4)
midS.push(6)
midS.push(8)
midS.mid_push(10)

print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())
print(midS.pop())


print("\n")

midS2 = MidStack()
midS2.push(2)
midS2.push(4)
midS2.push(6)
midS2.push(8)
midS2.push(10)
midS2.mid_push(12)


print(midS2.pop())
print(midS2.pop())
print(midS2.pop())
print(midS2.pop())
print(midS2.pop())
print(midS2.pop())

'''
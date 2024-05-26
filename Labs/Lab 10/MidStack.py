from DoublyLinkedList import DoublyLinkedList


class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.midNode = self.data.header
        self.midPos = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):

        self.data.add_last(e)

        newMid = (len(self.data) + 1) // 2
        while self.midPos < newMid:
            self.midNode = self.midNode.next
            self.midPos += 1

    def top(self):
        if self.is_empty(): raise Exception("empty list!")
        else:
            x = self.data.trailer.prev.data
            return x

    def pop(self):
        if self.is_empty():
            raise Exception("empty list!")
        else:
            x = self.data.delete_last()
            return x

        newMid = (len(self.data) + 1) // 2
        while self.midPos > newMid:
            self.midNode = self.midNode.prev
            self.midPos -= 1

    def mid_push(self, e):
        self.data.add_after(self.midNode, e)
        newMid = (len(self.data) + 1) // 2
        while self.midPos < newMid:
            self.midNode = self.midNode.next
            self.midPos += 1


ms = MidStack()
for i in range(6):
    ms.push(i)

ms.mid_push("hello!")
ms.mid_push("how are you!")


for i in range(8):
    print(ms.pop())

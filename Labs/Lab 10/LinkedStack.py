from DoublyLinkedList import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.dataDLL = DoublyLinkedList()

    def __len__(self):
        return len(self.dataDLL)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.dataDLL.add_last(e)

    def top(self):
        first = self.dataDLL.delete_first()
        self.dataDLL.add_first(first)
        return first

    def pop(self):
        first = self.dataDLL.delete_first()
        return first


ls = LinkedStack()

for i in range(5): ls.push(i)
for i in range(3): print(ls.pop())

print(ls.top())
print(ls.top())


print("\n")

myDLL = DoublyLinkedList()
for i in range(3, 30, 3):
    myDLL.add_last(i)

for i in range(len(myDLL)):
    print(myDLL[i])

class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        newNode = self.Node(val)
        prevNode = node
        nextNode = prevNode.next

        prevNode.next = newNode
        newNode.next = nextNode

        self.size += 1

    def add_first(self, val):
        newNode = self.Node(val)

        if len(self) == 0:
            self.header = newNode
            self.tail = newNode
            self.size += 1
        else:

            newNode.next = self.header
            self.header = newNode

            self.size += 1

    def add_last(self, val):
        newNode = self.Node(val)

        if len(self) == 0:
            self.header = newNode
            self.tail = newNode
            self.size += 1

        else:
            newNode = self.Node(val)
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def delete_first(self):
        if len(self) == 0:
            raise Exception("empty")
        else:
            first = self.header
            newHeader = first.next

            first.disconnect()

            self.size -= 1

            self.header = newHeader

            if self.size == 0:
                self.trailer = None

            return first



    def delete_last(self):
        if len(self) == 0:
            raise Exception("empty")
        if len(self) == 1:
            self.delete_first()
        else:
            self.reverse()
            self.delete_first()
            self.reverse()



    def reverse(self):

        cursor = None
        firstNode = None
        lastNode = None

        index = 0

        for i in self:
            myNode = self.Node(i, cursor)
            if index == 0:
                lastNode = myNode
            if index == len(self) - 2:
                firstNode = myNode

            index += 1
            cursor = myNode

        cursor = self.header

        while cursor is not None:
            cursor.data = None
            cursor = cursor.next

        self.header = firstNode
        self.tail = lastNode

        return self.header

    def __iter__(self):
        cursor = self.header
        while (cursor is not None):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"


sll = SinglyLinkedList()



for i in range(5, 45, 5):
    sll.add_last(i)

print(sll)
sll.reverse()
print(sll)


sll2 = SinglyLinkedList()

for i in range(5, 45, 5):
    sll2.add_last(i)

for i in range(8):
    sll2.delete_last()
    print(sll2)
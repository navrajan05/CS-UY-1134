from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, elem):
        self.data.add_last(elem)

    def dequeue(self):
        x = self.data.delete_first()
        return x

    def first(self):
        x = self.data.header.next.data
        return x
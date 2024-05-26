from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for digit in num_str:
            self.data.add_last(int(digit))

        cursor = self.data.header.next
        breakout = False
        while (not breakout) and cursor is not None:
            if cursor.data == 0:
                cursorSavepoint = cursor.next
                self.data.delete_node(cursor)
                cursor = cursorSavepoint
            else:
                breakout = True

        if len(self.data) == 0:
            self.data.add_first(0)

    def __add__(self, other):
        carry = 0
        cursor1 = self.data.trailer.prev
        cursor2 = other.data.trailer.prev

        value = ""

        for i in range(max(len(self.data), len(other.data))):


            if cursor1.data is None: data1 = 0
            else: data1 = cursor1.data

            if cursor2.data is None: data2 = 0
            else: data2 = cursor2.data

            sum = data1 + data2 + carry
            digit = sum % 10
            carry = sum // 10

            if cursor1.prev is not None: cursor1 = cursor1.prev
            if cursor2.prev is not None: cursor2 = cursor2.prev

            value = str(digit) + value

        if carry > 0: value = str(carry) + value

        return Integer(value)

    def __repr__(self):
         return "".join(str(digit) for digit in self.data)

    def __mul__(self, other):

        otherCursor = other.data.trailer.prev

        sums = DoublyLinkedList()

        while otherCursor.prev is not None:
            loops = otherCursor.data
            out = Integer('0')
            for i in range(loops):
                out = out + self

            sums.add_last(out)

            otherCursor = otherCursor.prev

        sumCursor = sums.trailer.prev
        out = Integer('0')

        digits = 0
        for i in sums:
            for j in range(digits):
                i.data.add_last(0)

            digits += 1

        out = Integer("0")
        for i in sums:
            out = out + i

        return out
''' 

n1 = Integer("131")
n2 = Integer("007")
print(n1, n2, n1+ n2, n1 * n2)
'''
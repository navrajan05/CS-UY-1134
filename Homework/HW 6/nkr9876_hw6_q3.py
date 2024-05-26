from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str= ""):
        self.data = DoublyLinkedList()
        for char in orig_str:
            self.data.add_last((char, 1))
        if len(self.data) > 0:
            self.__compress()

    def __add__(self, other):

        out = CompactString()

        for i in self.data:
            out.data.add_last(i)

        for i in other.data:
            out.data.add_last(i)

        out.__compress()
        return out

    def __compress(self):
        cursor = self.data.header.next

        while cursor is not None and cursor.next is not None and cursor.next.data is not None:
            if cursor.data[0] == cursor.next.data[0]:
                cursor.data = (cursor.data[0], cursor.data[1] + cursor.next.data[1])
                self.data.delete_node(cursor.next)
            else:
                cursor = cursor.next

    def __repr__(self):
        out = ""

        for i in self.data:
            out += i[0] * i[1]
        return out

    def __lt__(self, other):
        selfCursor = self.data.header.next
        otherCursor = other.data.header.next

        if(self.data.is_empty() and not other.data.is_empty()):
            return True

        while selfCursor.data is not None and otherCursor.data is not None:
            char1, count1 = selfCursor.data[0], selfCursor.data[1]
            char2, count2 = otherCursor.data[0], otherCursor.data[1]

            if char1 != char2 or count1 != count2:
                if char1 < char2:
                    return True
                elif char2 > char1:
                    return False
                else:
                    if selfCursor.next.data is not None:
                        nextChar1 = selfCursor.next.data[0]
                    else: nextChar1 = None

                    if otherCursor.next.data is not None:
                        nextChar2 = otherCursor.next.data[0]
                    else: nextChar2 = None

                    if count1 < count2:
                        if nextChar1 is None: return True
                        elif nextChar1 < char2: return True
                        else: return False
                    elif count2 < count1:
                        if nextChar2 is None:return False
                        elif nextChar2 < char1:return False
                        else: return True
            selfCursor = selfCursor.next
            otherCursor = otherCursor.next
        return False

    def __eq__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next

        if len(self.data) != len(other.data):
            return False

        while cursor1.data is not None and cursor2.data is not None:
            char1, count1 = cursor1.data[0], cursor1.data[1]
            char2, count2 = cursor2.data[0], cursor2.data[1]

            if char1 != char2 or count1 != count2:
                return False

            cursor1 = cursor1.next
            cursor2 = cursor2.next

        return True

    def __le__(self, other):
        if self < other or self == other: return True
        else: return False

    def __gt__(self, other):
        if self <= other: return False
        else: return True

    def __ge__(self, other):
        if self < other: return False
        else: return True


x = CompactString("ro")
y = CompactString("RO")

print(x + y)
print(x == y)

'''

x = CompactString('')
x2 = CompactString('aabbbcab')
y = CompactString('cjjrje')
print(x + y)
print(x2.data)
print(x.data)
print(x == x2)
print(x < x2)
print(x > x2)
print(x <= x2)
print(x >= x2)
'''
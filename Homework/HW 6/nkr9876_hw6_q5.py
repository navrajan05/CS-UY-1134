from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):

    def merge_sublists(cursor1, cursor2):
        useFirstCursor = False
        if cursor1.data is None and cursor2.data is None:
            return DoublyLinkedList()
        elif cursor1.data is None:
            inMerge = merge_sublists(cursor1, cursor2.prev)
            inMerge.add_last(cursor2.data)
        elif cursor2.data is None:
            inMerge = merge_sublists(cursor1.prev, cursor2)
            inMerge.add_last(cursor1.data)
        else:
            if cursor1.data > cursor2.data:
                inMerge = merge_sublists(cursor1.prev, cursor2)
                inMerge.add_last(cursor1.data)
            else:
                inMerge = merge_sublists(cursor1, cursor2.prev)
                inMerge.add_last(cursor2.data)

        return inMerge

    merge = merge_sublists(srt_lnk_lst1.trailer.prev, srt_lnk_lst2.trailer.prev)
    return merge


list1 = DoublyLinkedList()
for i in range(1, 100, 7):
    list1.add_last(i)

list2 = DoublyLinkedList()
for i in range(5, 10, 1):
    list2.add_last(i)

list3 = DoublyLinkedList()

print(list1)
print(list2)
print(merge_linked_lists(list1, list3))
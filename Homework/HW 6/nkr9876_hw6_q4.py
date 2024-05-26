from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    copyList = DoublyLinkedList()
    for i in lnk_lst:
        copyList.add_last(i)

    return copyList


def deep_copy_linked_list(lnk_lst):
    deepCopy = DoublyLinkedList()
    for i in lnk_lst:
        if isinstance(i, int):
            deepCopy.add_last(i)
        else:
            subcopy = deep_copy_linked_list(i)
            deepCopy.add_last(subcopy)
    return deepCopy

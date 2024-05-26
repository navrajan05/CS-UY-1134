from BinarySearchTreeMap import BinartSearchTreeMap as BSTMap

# Runtime of O(h)
def compare_BST(bst1, bst2):
    list1 = []
    list2 = []

    for i in bst1:
        list1.append(i)

    for i in bst2:
        list2.append(i)



    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False


    return True


a = BSTMap()
b = BSTMap()
for i in range(8):
    a.insert(i, "hello")
    b.insert(i, i)

b.insert(15, "hello")

print(compare_BST(a, b))


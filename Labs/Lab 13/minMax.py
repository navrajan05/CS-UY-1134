from BinarySearchTreeMap import BinartSearchTreeMap as BSTMap

# Runtime of O(h)
def min_max_BST(bst):
    L = bst.root
    R = bst.root

    while L.left is not None:
        L = L.left

    while R.right is not None:
        R = R.right

    return (L.item.key, R.item.key)

a = BSTMap()
for i in range(8):
    a.insert(i, i)


print(min_max_BST(a))

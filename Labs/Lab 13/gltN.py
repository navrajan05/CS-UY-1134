from BinarySearchTreeMap import BinartSearchTreeMap as BSTMap

# Runtime of O(h)
def glt_n(bst, n):

    node = bst.root

    path = [-1]

    while node is not None:
        path.append(node.item.key)

        #print(node.item)
        #print(path)
        if n < node.item.key:
            node = node.left
        elif n > node.item.key:
            node = node.right
        else:
            return node.item.key

    best = path[0]

    for i in path:
        if i <= n:
            if i > best:
                best = i

    return best


a = BSTMap()
for i in range(8, 60, 4):
    a.insert(i, i)


print(glt_n(a, 15))
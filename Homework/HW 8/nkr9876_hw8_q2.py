from nkr9876_BinarySearchTreeMap import BinarySearchTreeMap


def create_chain_bst(n):
    myMap = BinarySearchTreeMap()
    for i in range(1, n+1):
        myMap[i] = None

    return myMap


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, low, high):
    if low < high:

        mid = (low + high) // 2
        #print(mid)
        ltree = BinarySearchTreeMap()
        rtree = BinarySearchTreeMap()

        add_items(ltree, low, mid-1)
        add_items(rtree, mid+1, high)

        bst[mid] = None
        bst.root.left, bst.root.right = ltree.root, rtree.root
        ltree.root.parent, rtree.root.parent = bst.root, bst.root
        bst.n = bst.n + ltree.n + rtree.n

    else:
        bst[low] = None
        #print(low)

'''
x = create_complete_bst(7)
'''
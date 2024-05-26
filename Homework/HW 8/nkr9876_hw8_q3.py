from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):

    if len(prefix_lst) == 0:
        return BinarySearchTreeMap()

    leftBranches = []
    item = BinarySearchTreeMap.Item(prefix_lst[0])
    root = BinarySearchTreeMap.Node(item)

    leftBranches.append([root])

    for i in range(1, len(prefix_lst)):
        item = BinarySearchTreeMap.Item(prefix_lst[i])
        node = BinarySearchTreeMap.Node(item)

        if node.item.key < leftBranches[-1][-1].item.key:
            leftBranches[-1][-1].left = node
            node.parent = leftBranches[-1][-1]
            leftBranches[-1].append(node)
        else:
            leftBranches.append([node])

    '''
    for i in leftBranches:
        for node in i:
            print(node.item.key)
        print("\n")
    '''

    strand = leftBranches[0]
    trails = leftBranches[1:]

    for i in trails:
        keys = [n.item.key for n in strand]
        attached = False

        while not attached:

            if len(strand) == 1 or strand[-2].item.key > i[0].item.key:
                strand[-1].right = i[0]
                i[0].parent = strand[-1]

                #print(i[0].item.key, "joined to", strand[-1].item.key)

                strand.pop()
                strand.extend(i)
                attached = True

            else:
                strand.pop()

    outTree = BinarySearchTreeMap()
    outTree.root = root
    outTree.n = len(prefix_lst)

    return(outTree)


tree = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])

#print(tree.root.right.left.item.key)
#print(len(tree))


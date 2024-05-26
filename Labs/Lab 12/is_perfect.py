from LinkedBinaryTree import LinkedBinaryTree


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)

tree = LinkedBinaryTree(c)


def is_perfect_recursive(root):
    if root is not None:
        leftPerfect, leftHeight = is_perfect_recursive(root.left)
        rightPerfect, rightHeight = is_perfect_recursive(root.right)

        if (leftPerfect and rightPerfect) and (leftHeight == rightHeight):
            return (True, leftHeight + 1)
        else:
            return (False, max(leftHeight, rightHeight) + 1)

    else:
        return (True, -1)


def is_perfect_iterative(root):


    def subtree_height(r):
        if (r.left is None and r.right is None):
            return 0
        elif (r.left is None):
            return 1 + subtree_height(r.right)
        elif (r.right is None):
            return 1 + subtree_height(r.left)
        else:
            left_height = subtree_height(r.left)
            right_height = subtree_height(r.right)
            return 1 + max(left_height, right_height)



    myList = []
    def fullList(r):
        if r is not None:
            myList.append(r)
            fullList(r.left)
            fullList(r.right)

    fullList(root)
    nodeCount = len(myList)

    height = subtree_height(root)

    maxCount = 2 ** (height + 1) - 1

    print(nodeCount)
    print(maxCount)
    return maxCount == nodeCount

print(is_perfect_iterative(tree.root))
print(is_perfect_recursive(tree.root)[0])
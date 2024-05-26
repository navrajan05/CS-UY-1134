from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):

    if bin_tree.is_empty():
        raise Exception("Tree is empty!")

    def subtree_min_and_max(root):

        if root is None:
            return (None, None)

        lVals = subtree_min_and_max(root.left)
        rVals = subtree_min_and_max(root.right)

        minima = []
        if lVals[0] is not None: minima.append(lVals[0])
        if rVals[0] is not None: minima.append(rVals[0])
        minima.append(root.data)

        maxima = []
        if lVals[1] is not None: maxima.append(lVals[1])
        if rVals[1] is not None: maxima.append(rVals[1])
        maxima.append(root.data)

        return (min(minima), max(maxima))

    return subtree_min_and_max(bin_tree.root)
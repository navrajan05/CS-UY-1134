from LinkedBinaryTree import LinkedBinaryTree


def is_height_balanced(bin_tree):
    def subtree_balanced(node):
        if node is None:
            return (0, True)
        else:
            left = subtree_balanced(node.left)
            right = subtree_balanced(node.right)

            difference = abs(left[0] - right[0]) <= 1

            height = max(left[0], right[0]) + 1
            balance = left[1] and right[1] and difference

            return (height, balance)

    return subtree_balanced(bin_tree.root)[1]



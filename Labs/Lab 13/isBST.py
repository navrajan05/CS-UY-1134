from LinkedBinaryTree import LinkedBinaryTree

def is_BST(root):

    tree = LinkedBinaryTree(root)
    out = []
    for i in tree.inorder():
        out.append(i)

    for i in range(len(out) - 1):
        if out[i+1] > out[i]:
            return False

    return True

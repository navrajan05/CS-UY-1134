from LinkedBinaryTree import LinkedBinaryTree

def is_full(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    elif is_full(root.left) and is_full(root.right):
        return True
    else:
        return False


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)

tree2 = LinkedBinaryTree(c)

d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)

tree1 = LinkedBinaryTree(f)


print(tree1.bt_even_sum())
print(tree1.__contains__(5), tree1.__contains__("hello world"))

print("\n")

print(is_full(e))
print(is_full(c))

l1 = LinkedBinaryTree.Node(7)
h1 = LinkedBinaryTree.Node(10, l1, None)

treeA = LinkedBinaryTree(h1)

l2 = LinkedBinaryTree.Node(3)
r2 = LinkedBinaryTree.Node(5)
h2 = LinkedBinaryTree.Node(8, l2, r2)

treeB = LinkedBinaryTree(h2)

print("\n")

m = treeA + treeB
print(m.data)
print(m.left.data)
print(m.right.data)

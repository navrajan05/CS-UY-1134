from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue

a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)

tree = LinkedBinaryTree(c)

def invert_recursive(root):
    if root is None:
        return None
    else:
        l_invert = invert_recursive(root.left)
        r_invert = invert_recursive(root.right)

        root.left, root.right = r_invert, l_invert
        return root


def invert_iterative(root):
    nodeQueue = ArrayQueue()
    nodeQueue.enqueue(root)
    while not nodeQueue.is_empty():
        currentNode = nodeQueue.pop()
        currentNode.left, currentNode.right = currentNode.right, currentNode.left
        nodeQueue.enqueue(currentNode.right)
        nodeQueue.enqueue(currentNode.left)

a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)

tree = LinkedBinaryTree(c)
for i in tree: print(i)

invert_recursive(tree.root)
print("\n")

for i in tree: print(i)

print("\n")


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)

tree = LinkedBinaryTree(c)
for i in tree: print(i)

invert_recursive(tree.root)
print("\n")

for i in tree: print(i)

print("\n")


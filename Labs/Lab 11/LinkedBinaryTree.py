from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self
            self.parent = None

    def bt_even_sum(self):
        def subtree_even_sum(root):
            if (root is None):
                return 0
            elif root.data % 2 == 0:
                left_sum = subtree_even_sum(root.left)
                right_sum = subtree_even_sum(root.right)
                return left_sum + right_sum + root.data
            else:
                left_sum = subtree_even_sum(root.left)
                right_sum = subtree_even_sum(root.right)
                return left_sum + right_sum

        return subtree_even_sum(self.root)

    def __contains__(self, item):
        def subtree_contains(root, val):
            if (root is None):
                return False
            else:
                iContain = (root.data == val)
                lContains = subtree_contains(root.left, val)
                rContains = subtree_contains(root.right, val)
                return iContain or lContains or rContains

        return subtree_contains(self.root, item)

    def __add__(self, other):

        def merge_bt(root1, root2):

            if root1.left is not None and root2.left is not None:
                root3L = merge_bt(root1.left, root2.left)
            elif root1.left is not None:
                root3L = root1.left
            elif root2.left is not None:
                root3L = root2.left
            else:
                root3L = None


            if root1.right is not None and root2.right is not None:
                root3R = merge_bt(root1.right, root2.right)
            elif root1.right is not None:
                root3R = root1.right
            elif root2.right is not None:
                root3R = root2.right
            else:
                root3R = None

            root3 = self.Node(root1.data + root2.data, root3L, root3R)
            return root3

        return merge_bt(self.root, other.root)

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return left_count + right_count + 1

        return subtree_count(self.root)

    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return left_sum + right_sum + root.data

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if ((root.left is None) and (root.right is None)):
                return 0
            elif (root.right is None):  # left is not None
                left_height = subtree_height(root.left)
                return 1 + left_height
            elif (root.left is None):  # right is not None
                right_height = subtree_height(root.right)
                return 1 + right_height
            else:  # both subtrees are not None
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if (self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)

    def breadth_first(self):
        if (self.is_empty()):
            return
        bfs_queue = ArrayQueue()
        bfs_queue.enqueue(self.root)
        while (bfs_queue.is_empty() == False):
            curr_node = bfs_queue.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                bfs_queue.enqueue(curr_node.left)
            if (curr_node.right is not None):
                bfs_queue.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.data

    def preorder_with_stack(self):
        ''' Returns a generator function that iterates through
        the tree using the preorder traversal '''
        stack = ArrayStack()
        stack.push(self.root)
        while (len(stack) > 0):
            node = stack.pop()
            if (node.right is not None):
                stack.push(node.right)
            if (node.left is not None):
                stack.push(node.left)
            yield node.data


def eval_exp_tree(exp_t):
    def subtree_eval_exp(root):
        if ((root.left is None) and (root.right is None)):
            return root.data
        else:
            left_arg = subtree_eval_exp(root.left)
            right_arg = subtree_eval_exp(root.right)
            if (root.data == "+"):
                return left_arg + right_arg
            elif (root.data == "-"):
                return left_arg - right_arg
            if (root.data == "*"):
                return left_arg * right_arg
            if (root.data == "/"):
                return left_arg / right_arg

    return subtree_eval_exp(exp_t.root)

from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):

    def Node(x):
        return LinkedBinaryTree.Node(x)

    items = prefix_exp_str.split()

    myNodes = DoublyLinkedList()
    for item in items:
        if item.isnumeric():
            myNodes.add_last((Node(int(item))))
        else:
            myNodes.add_last((Node(item)))



    '''
    
    
    This code is made significantly harder to trace by the fact that 
    both LinkedBinaryTrees and DoublyLinkedLists refer to the element
    stored in each node by the variable 'data' internally. Sorry :(.
        
    '''

    cursor = myNodes.trailer.prev
    #print(cursor)

    while cursor.data is not None:

        '''
        
        Debug code, ignore.
        
        print(cursor.data.data)
        out = ' '
        for i in myNodes:
            out = out + str(i.data) + " "

        print(out)
        print("\n")
        
        '''

        if not isinstance(cursor.data.data, int):

            rootNode = cursor.data
            leftNode = cursor.next.data
            rightNode = cursor.next.next.data

            rootNode.left = leftNode
            leftNode.parent = rootNode

            rootNode.right = rightNode
            rightNode.parent = rootNode

            myNodes.delete_node(cursor.next.next)
            myNodes.delete_node(cursor.next)


        cursor = cursor.prev


    for i in myNodes: return LinkedBinaryTree(i)

#print(create_expression_tree('* 2 + - 15 6 4').root.right.left.right.data)


def prefix_to_postfix(prefix_exp_str):
    myTree = create_expression_tree(prefix_exp_str)
    out = []
    generator = myTree.postorder()
    for i in generator:
        out.append(str(i.data))
    #print(out)
    x = " ".join(out)
    return(x)

#print(prefix_to_postfix('* 2 + - 15 6 4'))

# Please import this module next time so I don't need to paste it in ;-;
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        next_node.prev = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if (self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"

    def remove_all(self, elem):
        cursor = self.header.next
        while (cursor.next is not None):
            if (cursor.data == elem):
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next

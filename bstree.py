class BSTNode:
    def __init__(value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__:
        self.head = None

    def add_node(self, val):
        node = BSTNode(val)
        if val > self.head:
            old = self.head
            self.head = node

            node.left = old

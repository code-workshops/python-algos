class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = None
        self.right = None


def _insert_node_into_bst(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_bst(node.left, data);
        else:
            node.right = _insert_node_into_bst(node.right, data);
    return node

# BST alternative method
def isPresent (root,val):
    if root.value == val:
        return 1
    elif root.right == None and root.left == None:
        return 0

    if val <= root.left.value:
        isPresent(root.left, val)
    elif val >= root.right.value:
        isPresent(root.right, val)

    return 0
    
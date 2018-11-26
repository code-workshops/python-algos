class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def set_next(self, node):
        self.next = node
        node.previous = self

    def set_previous(self, node):
        self.previous = node
        node.next = self.next

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, item):
        self.head = None

    def insert(self, value):
        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self, item):
        current = self.head
        while current:
            if current.get_value() == item:
                # Need current.previous to point it to current.next
                current.set_previous(current.get_previous())
                return 0
            else
                current = current.get_next()
        return "Item not found."

    def search(self, item):
        current = self.head
        while current:
            if current.get_value() == item:
                return current.get_value()
            else
                current = current.get_next()
        return "Item not found."

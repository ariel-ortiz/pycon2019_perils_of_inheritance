class LinkedList:

    class Node:

        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.header = LinkedList.Node()
        self.length = 0

    def insert(self, value):
        new_node = LinkedList.Node(value)
        new_node.next = self.header.next
        self.header.next = new_node
        self.length += 1

    def insert_all(self, iterable):
        for value in iterable:
            self.insert(value)

    def remove(self):
        if self.header.next is None:
            raise RuntimeError("Can't remove element from an empty list.")
        node = self.header.next
        self.header.next = node.next
        self.length -= 1
        return node.value

    def clear(self):
        self.length = 0
        self.header.next = None

    def __iter__(self):
        current = self.header.next
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return f"[{', '.join(str(value) for value in self)}]"

    def __len__(self):
        return self.length

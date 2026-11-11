from __future__ import annotations


class Node:
    def __init__(self, *, value: str):
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None

    def __repr__(self):
        return "{}"


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, data):
        """从尾部插入"""
        node = Node(value=data)
        current = self.tail
        if current:
            current.next = node
            node.prev = current
        self.tail = node

    def prepend(self, node):
        pass


if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list.head, linked_list.tail)
    linked_list.append(12)
    print(linked_list.head, linked_list.tail)

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def push(self, data: T):
        pass


class BinaryTree:
    def __init__(self):
        self.root: Node | None = None


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(1)
    print(bt)

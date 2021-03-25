from __future__ import annotations

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def add_left(self, node: Node) -> None:
        self.left = node

    def add_right(self, node: Node) -> None:
        self.right = node

class TreeNode(Node):
    def __init__(self, name, value) -> None:
        super().__init__(value)
        self.name = name


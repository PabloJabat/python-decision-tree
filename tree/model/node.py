from __future__ import annotations

from tree.model import DataBlob


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
    def __init__(self, tag, blob: DataBlob) -> None:
        super().__init__(tag)
        self._blob = blob

    @property
    def blob(self) -> DataBlob:
        return self._blob

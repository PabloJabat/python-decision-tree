import numpy as np


class DataBlob:
    def __init__(self, data: np.array) -> None:
        self.labels = frozenset(data)
        self._data = data  # It can't be modified
        self._entropy = None  # Entropy cache

    @property
    def data(self) -> np.array:
        return self._data

    @property
    def entropy(self) -> float:
        """Check if entropy is stored in cache, otherwise compute it"""
        if self._entropy:
            return self._entropy
        else:
            return 1.0

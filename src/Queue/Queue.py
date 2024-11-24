from AbstractQueue import AbstractQueue

class Queue(AbstractQueue):
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    @property
    def size(self):
        return len(self._items)

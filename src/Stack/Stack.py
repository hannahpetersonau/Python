from AbstractStack import AbstractStack

class Stack(AbstractStack):
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return not bool(self._items)

    @property
    def size(self):
        return len(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]
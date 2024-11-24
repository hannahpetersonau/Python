from AbstractStack import AbstractStack

class LinkedStack(AbstractStack):
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self._top = None
        self._size = 0

    @property
    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    def push(self, item):
        self._top = self.Node(item, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty:
            raise IndexError('Pop from empty stack')
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty:
            raise IndexError('Peek from empty stack')
        return self._top.data
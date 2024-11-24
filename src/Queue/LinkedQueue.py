from AbstractQueue import AbstractQueue

class LinkedQueue(AbstractQueue):
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    @property
    def is_empty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    def enqueue(self, item):
        new_node = self.Node(item)
        if self.is_empty:
            self._front = new_node
        else:
            self._back.next = new_node

        self._back = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty:
            raise IndexError('Dequeue from empty queue')
        data = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._back = None
        self._size -= 1
        return data

    def peek(self):
        if self.is_empty:
            raise IndexError('Peek from empty queue')
        return self._front.data
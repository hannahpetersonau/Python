from AbstractList import AbstractList
from src.Lists.Node import Node

class UnorderedList(AbstractList):
    def __init__(self):
        self._head = None

    @property
    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self._head
        self._head = temp

    @property
    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self._head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def get_at_index(self, index):
        current = self._head
        count = 0

        while current is not None and count < index:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Index out of range")

        return current.data

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        temp = Node(item)
        if self._head is None:
            self._head = temp
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = temp

    def index(self, item):
        current = self._head
        count = 0
        while current is not None:
            if current.data == item:
                return count
            count += 1
            current = current.next
        return -1

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            current = self._head
            count = 0
            while count < pos - 1 and current is not None:
                current = current.next
                count += 1

            if current is None:
                raise IndexError("Index out of range")

            temp = Node(item)
            temp.next = current.next
            current.next = temp

    def pop(self, pos=None):
        if pos is None:
            current = self._head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            if previous is None:
                self._head = None
            else:
                previous.next = None
            return current.data
        else:
            if pos == 0:
                if self._head is None:
                    raise IndexError("Index out of range")
                else:
                    item = self._head.data
                    self._head = self._head.next
                    return item
            else:
                current = self._head
                previous = None
                count = 0
                while count < pos and current is not None:
                    previous = current
                    current = current.next
                    count += 1

                if current is None:
                    raise IndexError("Index out of range")

                previous.next = current.next
                return current.data
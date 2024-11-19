from abc import ABC, abstractmethod


class AbstractList(ABC):

    @property
    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def add(self, item):
        raise NotImplementedError

    @property
    @abstractmethod
    def size(self):
        raise NotImplementedError

    @abstractmethod
    def search(self, item):
        raise NotImplementedError

    @abstractmethod
    def get_at_index(self, index):
        raise NotImplementedError

    @abstractmethod
    def remove(self, item):
        raise NotImplementedError

    @abstractmethod
    def append(self, item):
        raise NotImplementedError

    @abstractmethod
    def index(self, item):
        raise NotImplementedError

    @abstractmethod
    def insert(self, pos, item):
        raise NotImplementedError

    @abstractmethod
    def pop(self, pos):
        raise NotImplementedError


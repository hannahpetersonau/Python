from abc import ABC, abstractmethod

class AbstractQueue(ABC):

    @abstractmethod
    def enqueue(self, item):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def size(self):
        raise NotImplementedError

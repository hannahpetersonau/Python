from abc import ABC, abstractmethod

class AbstractStack(ABC):

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def is_empty(self):
        raise NotImplementedError

    @abstractmethod
    def push(self, item):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def size(self):
        raise NotImplementedError

import unittest
from src.Queue.Queue import Queue


class TestQueueMethods(unittest.TestCase):

    def setUp(self):
        """Setting up"""
        self.queue = Queue()

    def test_is_empty(self):
        """Testing is_empty() method"""
        assert self.queue.is_empty
        self.queue.enqueue(42)
        assert not self.queue.is_empty

    def test_size(self):
        """Testing size() method"""
        assert self.queue.size == 0
        self.queue.enqueue(42)
        assert self.queue.size == 1

    def test_enqueue(self):
        """Testing enqueue() method"""
        self.queue.enqueue(42)
        assert self.queue.size == 1
        self.queue.enqueue(True)
        assert self.queue.size == 2

    def test_dequeue(self):
        """Testing dequeue() method"""
        self.queue.enqueue(42)
        self.queue.enqueue('taco')
        self.queue.enqueue(False)
        assert self.queue.dequeue() == 42
        assert self.queue.size == 2

        self.queue.enqueue(2)
        self.queue.enqueue('banana')
        assert self.queue.dequeue() == 'taco'


if __name__ == "__main__":
    unittest.main()

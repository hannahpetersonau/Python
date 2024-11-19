import unittest
from src.Stack.LinkedStack import LinkedStack


class TestStackMethods(unittest.TestCase):
    def setUp(self):
        """Setting up"""
        self.stack = LinkedStack()

    def test_is_empty(self):
        """Testing is_empty() method"""
        assert self.stack.is_empty
        self.stack.push(42)
        assert not self.stack.is_empty

    def test_size(self):
        """Testing size() method"""
        assert self.stack.size == 0
        self.stack.push(42)
        assert self.stack.size == 1

    def test_push(self):
        """Testing push() method"""
        self.stack.push(42)
        assert self.stack.size == 1
        self.stack.push('taco')
        assert self.stack.size == 2

    def test_pop(self):
        """Testing pop() method"""
        self.stack.push(42)
        assert self.stack.pop() == 42
        self.stack.push(8.5)
        self.stack.push('banana')
        assert self.stack.pop() == 'banana'
        assert self.stack.size == 1

    def test_peek(self):
        """Testing peek() method"""
        self.stack.push(42)
        assert self.stack.peek() == 42
        assert self.stack.size == 1

        self.stack.push(8.5)
        self.stack.push('banana')
        assert self.stack.peek() == 'banana'
        assert self.stack.size == 3


if __name__ == "__main__":
    unittest.main()

"""
Activity: Implement a Stack in Python.

A stack follows the LIFO principle:
Last In, First Out.
The last element added must be the first element removed.

Do not change the names of the class or the methods.
The automated tests expect exactly this interface.
"""


class Stack:
    def __init__(self):
        """Creates an empty stack."""
        self._items = []

    def push(self, item):
        """Adds an element to the top of the stack."""
        # TODO: implement this method
        pass

    def pop(self):
        """
        Removes and returns the top element of the stack.

        Must raise IndexError if the stack is empty.
        """
        # TODO: implement this method
        pass

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Must raise IndexError if the stack is empty.
        """
        # TODO: implement this method
        pass

    def is_empty(self):
        """ Returns True if the stack is empty; False otherwise."""
        # TODO: implement this method
        pass

    def size(self):
        """ Returns the number of elements in the stack."""
        # TODO: implement this method
        pass

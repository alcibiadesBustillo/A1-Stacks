import pytest

from stack import Stack


def test_new_stack_is_empty():
    stack = Stack()

    assert stack.is_empty() is True, "A newly created stack must be empty."
    assert stack.size() == 0, "The initial size of an empty stack must be 0."


def test_push_adds_one_element():
    stack = Stack()

    stack.push("A")

    assert stack.is_empty() is False, "After push(), the stack must not be empty."
    assert stack.size() == 1, "After adding one element, size() must return 1."
    assert stack.peek() == "A", "peek() must show the last element added."


def test_push_adds_multiple_elements():
    stack = Stack()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    assert stack.size() == 3, "After three push() operations, size() must return 3."
    assert stack.peek() == "C", "The top must be the last element added."


def test_pop_returns_elements_in_lifo_order():
    stack = Stack()

    stack.push("A")
    stack.push("B")
    stack.push("C")

    assert stack.pop() == "C", "Stack uses LIFO: the last element added must be removed first."
    assert stack.pop() == "B", "After removing C, the new top must be B."
    assert stack.pop() == "A", "The first element added must be removed last."


def test_pop_removes_the_element():
    stack = Stack()

    stack.push(10)

    item = stack.pop()

    assert item == 10, "pop() must return the removed element."
    assert stack.size() == 0, "pop() must reduce the size of the stack."
    assert stack.is_empty() is True, "After removing the only element, the stack must be empty."


def test_pop_on_empty_stack_raises_index_error():
    stack = Stack()

    with pytest.raises(IndexError):
        stack.pop()


def test_peek_returns_top_without_removing_it():
    stack = Stack()

    stack.push("A")
    stack.push("B")

    assert stack.peek() == "B", "peek() must return the top of the stack."
    assert stack.size() == 2, "peek() must not remove elements."
    assert stack.peek() == "B", "Calling peek() multiple times must not change the top."


def test_peek_on_empty_stack_raises_index_error():
    stack = Stack()

    with pytest.raises(IndexError):
        stack.peek()


def test_is_empty_changes_after_push_and_pop():
    stack = Stack()

    assert stack.is_empty() is True, "The stack starts empty."

    stack.push("A")
    assert stack.is_empty() is False, "After push(), the stack must not be empty."

    stack.pop()
    assert stack.is_empty() is True, "After removing the only element, the stack must be empty."


def test_size_updates_after_operations():
    stack = Stack()

    assert stack.size() == 0

    stack.push("A")
    stack.push("B")
    assert stack.size() == 2

    stack.pop()
    assert stack.size() == 1

    stack.pop()
    assert stack.size() == 0


def test_combined_sequence_of_operations():
    stack = Stack()

    stack.push("A")
    stack.push("B")
    assert stack.pop() == "B", "B must be removed because it was the last element added."

    stack.push("C")
    stack.push("D")

    assert stack.peek() == "D", "The top must be D."
    assert stack.pop() == "D", "D must be removed before C."
    assert stack.pop() == "C", "After D, C must be removed."
    assert stack.pop() == "A", "A must remain until the end."
    assert stack.is_empty() is True

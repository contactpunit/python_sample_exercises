from ds.ds.stack import Stack
import pytest


@pytest.fixture()
def stack():
    """ Provides Stack class object """
    return Stack()


def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0


def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(6)
    assert len(stack) == 2


def test_pop(stack):
    stack.push(4)
    stack.push(10)
    stack.push(20)
    item = stack.pop()
    assert item == 20
    item = stack.pop()
    assert item == 10
    item = stack.pop()
    assert item == 4
    item = stack.pop()
    assert item is None

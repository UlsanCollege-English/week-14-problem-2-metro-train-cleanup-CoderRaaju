import pathlib
import sys

import pytest

THIS_FILE = pathlib.Path(__file__).resolve()
HW_DIR = THIS_FILE.parents[1]
if str(HW_DIR) not in sys.path:
    sys.path.append(str(HW_DIR))

from main import Node, remove_cars  # noqa: E402


def to_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


def from_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def test_remove_middle_and_tail():
    head = from_list([1, 2, 3, 2, 4])
    new_head = remove_cars(head, 2)
    assert to_list(new_head) == [1, 3, 4]


def test_remove_head_only():
    head = from_list([5, 1, 2])
    new_head = remove_cars(head, 5)
    assert to_list(new_head) == [1, 2]


def test_remove_all_nodes():
    head = from_list([7, 7, 7])
    new_head = remove_cars(head, 7)
    assert new_head is None


def test_no_removals():
    head = from_list([1, 2, 3])
    new_head = remove_cars(head, 9)
    # Structure should be unchanged
    assert to_list(new_head) == [1, 2, 3]


def test_empty_list():
    new_head = remove_cars(None, 3)
    assert new_head is None


def test_alternate_pattern():
    head = from_list([2, 1, 2, 1, 2, 1])
    new_head = remove_cars(head, 2)
    assert to_list(new_head) == [1, 1, 1]


def test_longer_list_stress_like():
    values = [0, 1, 0, 2, 0, 3, 0, 4]
    head = from_list(values)
    new_head = remove_cars(head, 0)
    assert to_list(new_head) == [1, 2, 3, 4]

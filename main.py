
## main.py
```python
"""
HW02 — Metro Train Cleanup (Linked List Filter)

Implement a singly linked list Node class and a function remove_cars(head, target)
that removes all nodes with value == target and returns the new head.
"""


class Node:
    """
    Simple singly linked list node.

    value: the car ID (int or any value)
    next: the next Node in the list, or None
    """

    def __init__(self, value, next=None):
        # TODO: store value and next on the instance
        # Example:
        # self.value = value
        # self.next = next
        pass


def remove_cars(head, target):
    """
    Remove all nodes whose value == target from the list starting at head.

    :param head: Node or None, the head of the list
    :param target: value to remove from the list
    :return: new head Node (or None if list becomes empty)
    """
    # TODO (8 Steps of Coding):
    # 1. Re-read the problem and examples.
    # 2. Re-phrase the task (remove certain cars from a train).
    # 3. Identify inputs, outputs, and helper pointers (head, current, previous).
    # 4. Break down handling of head nodes vs middle nodes.
    # 5. Write pseudocode for updating .next pointers.
    # 6. Implement pointer updates in Python.
    # 7. Debug with small hand-drawn lists.
    # 8. Confirm one full pass only (O(N)), and constant extra space.
    raise NotImplementedError("Implement remove_cars and Node in main.py")


if __name__ == "__main__":
    # Optional manual test
    # Example train: 1 -> 2 -> 2 -> 3, remove cars with ID 2
    n4 = Node(3)
    n3 = Node(2, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)

    new_head = remove_cars(n1, 2)
    curr = new_head
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()

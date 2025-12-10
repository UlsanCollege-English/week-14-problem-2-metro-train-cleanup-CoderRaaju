class Node:
    """
    Simple singly linked list node.

    value: the car ID (int or any value)
    next: the next Node in the list, or None
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_cars(head, target):
    """
    Remove all nodes whose value == target from the list starting at head.

    :param head: Node or None, the head of the list
    :param target: value to remove from the list
    :return: new head Node (or None if list becomes empty)
    """

    # Step 1: Remove matching nodes at the head
    while head is not None and head.value == target:
        head = head.next

    # After removing head matches, if list becomes empty
    if head is None:
        return None

    # Step 2: Process the rest using prev/current pointers
    prev = head
    current = head.next

    while current is not None:
        if current.value == target:
            # Skip the current node
            prev.next = current.next
        else:
            # Move prev forward only if current is kept
            prev = current
        current = current.next

    return head
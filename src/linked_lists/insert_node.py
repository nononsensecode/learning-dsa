from .node import Node


def insert_node(head: Node, value: str, index: int) -> Node:
    current = head
    current_index = 0
    prev = None

    while current is not None:
        if current_index == index:
            new_node = Node(val=value)
            if prev is not None:
                next = prev.next
                prev.next = new_node
                new_node.next = next
                break
            new_node.next = head
            break

        prev = current
        current = current.next
        current_index += 1

    return head

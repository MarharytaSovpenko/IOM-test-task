### Reverse a linked list
##### Given the head of a singly linked list, reverse the list, and return the reversed list.
input = [10, 20, 30, 40]
output = [40, 30, 20, 10]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def print_linked_list(head):
    if not head:
        print("List is empty")
        return
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()


if __name__ == "__main__":
    # Creating the linked list from input [10, 20, 30, 40]
    nodes = [ListNode(val) for val in [10, 20, 30, 40]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    print("Original linked list:")
    print_linked_list(head)

    new_head = reverse_linked_list(head)

    print("Reversed linked list:")
    print_linked_list(new_head)

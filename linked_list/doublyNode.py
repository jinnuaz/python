class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val= val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


head = tail = DoublyNode(1)
print(f"head = {head}")
print(f"tail = {tail}")


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

def insert_at_begining(head, tail, val):
    new_node = DoublyNode(val, next = head)
    head.prev = new_node
    return head, new_node

head, tail = insert_at_begining(head, tail, 3)
display(head)
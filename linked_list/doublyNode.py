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

display(head)

# Head.next = A
# A.next = B
# B.next = C
#
# # print(Head)
#
# # curr = Head
# # while curr:
# #     print(curr)
# #     curr = curr.next
#
#
# def display(head):
#     curr = head
#     elements = []
#     while curr:
#         elements.append(str(curr.val))
#         curr = curr.next
#     print(' -> '.join(elements))
#
# display(Head)
#
# def search(head, val):
#     curr = head
#     while curr:
#         if val == curr.val:
#             return True
#         curr = curr.next
#     return False
# res = search(Head, 7)
# print(f"Result of search function is {res}")
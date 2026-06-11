class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    def __str__(self):
        return str(self.val)

l1 = ListNode(3)
l1.next = ListNode(4)
l1.next.next = ListNode(2)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


def addTwoNumbers(l1, l2):
    dummy = curr = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry = carry + l1.val
            l1 = l1.next
        if l2:
            carry = carry + l2.val
            l2 = l2.next

        curr.next = ListNode(carry % 10)
        curr = curr.next
        carry = carry // 10

    return dummy.next

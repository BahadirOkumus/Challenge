class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for i in range(n + 1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

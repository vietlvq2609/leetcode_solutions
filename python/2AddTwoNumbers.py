from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode((l1.val + l2.val) % 10)
        head = sum
        remain = 0

        if (l1.val + l2.val >= 10):
            remain = 1

        while l1.next or l2.next:
            if not l1.next:
                l2 = l2.next
                sum.next =  ListNode((l2.val + remain) % 10)
                if (l2.val + remain >= 10):
                    remain = 1
                else:
                    remain = 0
            elif not l2.next:
                l1 = l1.next
                sum.next = ListNode((l1.val + remain) % 10)
                if (l1.val + remain >= 10):
                    remain = 1
                else:
                    remain = 0
            else:
                l1 = l1.next
                l2 = l2.next
                sum.next = ListNode((l1.val + l2.val + remain) % 10)
                if (l1.val + l2.val + remain >= 10):
                    remain = 1
                else:
                    remain = 0
            sum = sum.next

        if remain == 1:
            sum.next = ListNode(1)
        return head

solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
solution.addTwoNumbers(l1, ListNode(5, ListNode(6, ListNode(4))) )
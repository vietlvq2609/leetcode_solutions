from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while not head is None:
            next = head.next
            head.next = tail
            tail = head
            head = next
        return tail

solution = Solution()
print(solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) # 5 -> 4 -> 3 -> 2 -> 1
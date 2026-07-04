# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        s = ListNode
        s.next = head

        while n>0:
            f = f.next
            n -= 1
        
        while f:
            f = f.next
            s = s.next

        if s.next == head:
            s.next = s.next.next
            return s.next

        s.next = s.next.next
        return head
        


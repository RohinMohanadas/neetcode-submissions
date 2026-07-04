# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        ctr = 1
        ptr1 = head
        ptr2 = head
        dummy = ListNode(0,head)
        lpprev = dummy

        while ctr < left:
            lpprev = ptr1
            ptr1 = ptr1.next
            ctr+=1
        
        ctr = 0
        prev = None
        while ctr < (right - left + 1):
            tmp = ptr1.next
            ptr1.next = prev
            prev, ptr1 = ptr1, tmp
            ctr+=1

        lpprev.next.next = ptr1
        lpprev.next = prev

        return dummy.next



           

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pt1 = head
        pt2 = head
        while pt2:
            pt1 = pt1.next
            pt2 = pt2.next
            if pt2:
                pt2 = pt2.next
            else:
                break
            if pt1 == pt2:
                return True

        return False
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = None
        head = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    res = list1
                else:
                    res.next = list1
                    res = list1
                list1 = list1.next
            elif list1.val > list2.val:
                if not head:
                    head = list2
                    res = list2
                else:
                    res.next = list2
                    res = list2
                list2 = list2.next
        
        if list1:
            if not head:
                head = list1
            else:
                res.next = list1
        
        if list2:
            if not head:
                head = list2
            else:
                res.next = list2


        return head      

        
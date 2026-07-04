# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #minimum = float("inf")
        remaining = True
        
        head = ListNode()
        res = head
        ctr = 0
        
        while True:
            minimum = float("inf")
            remaining = False
            for i in range(len(lists)): # find min
                j = i
                if lists[i]:
                    
                    if minimum == float("inf") or lists[minimum].val > lists[i].val:
                        minimum = i

            if minimum == float("inf"):
                break

            res.next = lists[minimum]
            lists[minimum] = lists[minimum].next
            res = res.next
            
        return head.next
        
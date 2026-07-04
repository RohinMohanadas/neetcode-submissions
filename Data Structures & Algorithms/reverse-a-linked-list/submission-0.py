# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        plainlist = []
        
        while head:
            plainlist.append(head)
            head = head.next

        print(plainlist)

        if not plainlist:
            return None
        
        print(len(plainlist))
        head = plainlist[-1]

        length = len(plainlist)
        for i,v in enumerate(plainlist[::-1]):
            print("i",length-i-1)
            v.next = plainlist[length-i-2] if (length-i-1)>0 else None

        return head

            
        
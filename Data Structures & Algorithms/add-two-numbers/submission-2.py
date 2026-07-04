# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ptr = res
        carry = 0

        while l1 and l2:
            node = ListNode()
            ptr.next = node
            node.val = l1.val+l2.val+ carry
            carry = node.val//10
            node.val = node.val%10
            ptr = node
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            
            node = ListNode()
            ptr.next = node
            node.val = l1.val + carry
            carry = node.val//10
            node.val = node.val%10
            print("carry, val",carry, node.val)
            ptr = node
            l1 = l1.next
        
        while l2:
            node = ListNode()
            ptr.next = node
            node.val = l2.val + carry
            carry = node.val//10
            node.val = node.val%10
            ptr = node   
            l2 = l2.next

        print(carry)
        if carry!=0:
            node = ListNode()
            ptr.next = node
            node.val = carry
            

        print(res)
        return res.next
            
        

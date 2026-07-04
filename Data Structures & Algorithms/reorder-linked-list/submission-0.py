# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        idx = 0
        ptr = head
        while ptr:
            array.append(ptr)
            ptr = ptr.next
            idx+=1

            
        print(array, len(array))
        #head = array[0]

        i,j = 0, idx-1

        while i<j:
            array[i].next = array[j]
            i+=1
            if i>=j:
                break
            array[j].next = array[i]
            j-=1

        array[i].next = None
            
        
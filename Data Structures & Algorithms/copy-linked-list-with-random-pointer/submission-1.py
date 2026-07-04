"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = defaultdict(Node)
        ptr = head

        if not head:
            return head
        while ptr:
            node = Node(ptr.val,None,None)
            hashmap[ptr] = node
            ptr = ptr.next
        
        for k,v in hashmap.items():
            if k.next:
                v.next = hashmap[k.next]
            else:
                v.next = None
            if k.random:
                v.random = hashmap[k.random]
            else: 
                v.random = None
        
        return hashmap[head]
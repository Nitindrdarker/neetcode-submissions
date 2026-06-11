# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        aNode = bNode = None
        aPrev = None
        bPrev = None
        dummy = node = ListNode(next = head)
        prev = None
        count = 0
        while node and count < left:
            prev = node
            node = node.next
            count += 1
        
        startPrev = prev
        start = node
        
        while count < right:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
            count += 1
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt
        startPrev.next = prev
        start.next = node
        return dummy.next
        


        
        
        
        
        
        

    
            
        
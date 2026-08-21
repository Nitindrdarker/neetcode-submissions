# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while a > 0:
                rem = b % a
                b = a
                a = rem
            return b

        node = head
        while node and node.next:
            
            a = node
            b = node.next
            g = gcd(a.val, b.val)
            a.next = ListNode(g)
            a.next.next = b
            node = b
        return head

        
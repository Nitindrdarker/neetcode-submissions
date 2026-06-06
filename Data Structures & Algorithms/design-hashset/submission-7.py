
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.totalKey = 10000
        self.l = [ListNode(0) for i in range(self.totalKey)]
        

    def add(self, key: int) -> None:
        h = key % self.totalKey
        head = self.l[h]
        
        while head.next != None:
            if head.next.val == key:
                return
            head = head.next
        head.next = ListNode(val = key)
        

    def remove(self, key: int) -> None:
        h = key % self.totalKey
        head = self.l[h]
        while head.next != None:
            if head.next.val == key:
                head.next = head.next.next
                return
            head = head.next
        

    def contains(self, key: int) -> bool:
        h = key % self.totalKey
        head = self.l[h]
        head = head.next
        while head != None:
            if head.val == key:
                return True
            head = head.next
        return False
        

    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
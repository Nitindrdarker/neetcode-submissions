class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.l = [ListNode(key=0, val=0) for i in range(self.size)]

        

    def put(self, key: int, value: int) -> None:
        k = key % self.size
        head = self.l[k]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = ListNode(key=key, val=value)

        

    def get(self, key: int) -> int:
        k = key % self.size
        head = self.l[k]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1
        

    def remove(self, key: int) -> None:
        k = key % self.size
        head = self.l[k]
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
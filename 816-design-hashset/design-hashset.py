class Listnode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [Listnode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        curr = self.set[key%len(self.set)]
        while curr.next:
            curr = curr.next
            if curr.key == key:
                return 
        curr.next = Listnode(key)
    def remove(self, key: int) -> None:
        curr = self.set[key%len(self.set)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key%len(self.set)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class Listnode:
    def __init__(self,key=-1,value = -1,next =None):
        self.key = key
        self.val = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.arr = [Listnode() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        curr = self.arr[key%len(self.arr)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Listnode(key,value)

    def get(self, key: int) -> int:
        curr = self.arr[key%len(self.arr)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.arr[key % len(self.arr)] 
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next 
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
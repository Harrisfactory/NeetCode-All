class MyHashSet:

    def __init__(self):
        self.hs = []

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            self.hs.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hs)):
            if self.hs[i] == key:
                self.hs.pop(i)
                return

    def contains(self, key: int) -> bool:
        if key in self.hs:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
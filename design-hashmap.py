class MyHashMap:

    def __init__(self):
        #an array that contains two values each except empty
        self.hm = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.hm)):
            if self.hm[i][0] == key:
                self.hm[i][1] = value
                return
        #else we need to put the kvp in
        self.hm.append([key,value])
        

    def get(self, key: int) -> int:
        for i in range(len(self.hm)):
            if self.hm[i][0] == key:
                return self.hm[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hm)):
            if self.hm[i][0] == key:
                self.hm.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
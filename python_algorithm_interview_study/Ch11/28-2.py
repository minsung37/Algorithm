# https://leetcode.com/problems/design-hashmap/
# 254ms 17.1MB
class MyHashMap:
    def __init__(self):
        self.s = dict()

    def put(self, key: int, value: int) -> None:
        self.s[key] = value

    def get(self, key: int) -> int:
        if key in self.s:
            return self.s[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.s:
            del(self.s[key])
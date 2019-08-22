class LRUCache:
    def __init__(self, capacity: int):
        self.dic, self.cap = collections.OrderedDict(), capacity

    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic: self.dic.move_to_end(key)
        elif len(self.dic) == self.cap: self.dic.popitem(0)
        self.dic[key] = value
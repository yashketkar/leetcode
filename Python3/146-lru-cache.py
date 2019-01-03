from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            value = self.d[key]
            del self.d[key]
            self.d[key] = value
            return value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.d:
            if len(self.d) == self.capacity:
                self.d.popitem(last=False)
        else:
            del self.d[key]
        self.d[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

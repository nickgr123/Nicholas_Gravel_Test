from time import time
import collections


class Entry():

    def __init__(self, value, expiryTime=10):
        self.value = value
        self.expiry = time() + expiryTime
        self.isExpired = False

    def isEntryExpired(self):
        if not self.isExpired:
            return self.expiry < time()
        return True


class Cache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            entry = self.cache.pop(key)
            if entry.isEntryExpired():
                raise Exception("Entry expired")
            self.cache[key] = Entry(entry.value)
            return entry.value
        except KeyError:
            raise Exception("Key not found")

    def set(self, key, value, expiryTime=10):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = Entry(value, expiryTime)

    def clean(self):
        for key, entry in self.cache.iteritems():
            if entry.isEntryExpired():
                self.cache.pop(key)

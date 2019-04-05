import unittest
from questionC import Cache

CAPACITY = 5


class TestCache(unittest.TestCase):

    def test_getUknownKey(self):
        cache = Cache(CAPACITY)
        with self.assertRaises(Exception) as e:
            cache.get("uknownKey")
        self.assertTrue('Key not found' in e.exception)

    def test_getKey(self):
        cache = Cache(CAPACITY)
        cache.set("abc", "123")
        self.assertEqual(cache.get("abc"), "123")

    def test_getExpiredKey(self):
        cache = Cache(CAPACITY)
        cache.set("abc", "123", -1)
        with self.assertRaises(Exception) as e:
            cache.get("abc")
        self.assertTrue('Entry expired' in e.exception)

    def test_setExcedesCapacity(self):
        cache = Cache(2)
        cache.set("abc", "123")
        cache.set("def", "456")
        cache.set("ghi", "789")
        with self.assertRaises(Exception) as e:
            cache.get("abc")
        self.assertTrue('Key not found' in e.exception)

    def test_setReOrdersCorrectly(self):
        cache = Cache(2)
        cache.set("abc", "123")
        cache.set("def", "456")
        cache.set("abc", "123")
        cache.set("ghi", "789")
        with self.assertRaises(Exception) as e:
            cache.get("def")
        self.assertTrue('Key not found' in e.exception)
        self.assertEqual(cache.get("abc"), "123")

    def test_clean(self):
        cache = Cache(3)
        cache.set("abc", "123", -1)
        cache.set("def", "456")
        cache.set("ghi", "789", -1)
        cache.clean()

        testCases = ["abc", "ghi"]
        for testCase in testCases:
            with self.assertRaises(Exception) as e:
                cache.get(testCase)
            self.assertTrue('Key not found' in e.exception)

        self.assertEqual(cache.get("def"), "456")


if __name__ == '__main__':
    unittest.main()

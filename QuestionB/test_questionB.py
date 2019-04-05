import unittest
from questionB import Version


class TestVersion(unittest.TestCase):

    def test_isNone(self):
        with self.assertRaises(Exception) as e:
            Version(None)
        self.assertTrue('Version can not be None' in e.exception)

    def test_isString(self):
        testCases = [
            False,
            1,
            1.2,
            ["string"],
            ("string", "string"),
            {"string"}
        ]
        for testCase in testCases:
            with self.assertRaises(Exception) as e:
                Version(testCase)
            self.assertTrue('Version must be string' in e.exception)

    def test_isValidFormat(self):
        testCases = [
            "A",
            "!.1",
            "A.1"
            "1.A",
            "1.2A",
            "1.!2",
            "1.2 3.4",
        ]
        for testCase in testCases:
            with self.assertRaises(Exception) as e:
                Version(testCase)
            self.assertTrue('Invalid Format' in e.exception)

    def test_versionEquals(self):
        testCases = [
            ["1.1", "1.1", True],
            ["1.1", "1.10", False],
            ["1.10", "1.10", True],
            ["1.12.13", "1.12.1", False],
        ]
        for testCase in testCases:
            version1 = Version(testCase[0])
            version2 = Version(testCase[1])
            self.assertEqual(version1 == version2, testCase[2])

    def test_versionNotEquals(self):
        testCases = [
            ["1.1", "1.1", False],
            ["1.1", "1.10", True],
            ["1.10", "1.10", False],
            ["1.12.13", "1.12.1", True],
        ]
        for testCase in testCases:
            version1 = Version(testCase[0])
            version2 = Version(testCase[1])
            self.assertEqual(version1 != version2, testCase[2])

    def test_versionGreaterThan(self):
        testCases = [
            ["1.1", "1.1", False],
            ["1.1", "1.10", False],
            ["1.10", "1.1", True],
            ["1.12", "1.11.2", True],
        ]
        for testCase in testCases:
            version1 = Version(testCase[0])
            version2 = Version(testCase[1])
            self.assertEqual(version1 > version2, testCase[2])

    def test_versionLessThan(self):
        testCases = [
            ["1.1", "1.1", False],
            ["1.1", "1.10", True],
            ["1.10", "1.1", False],
            ["1.12", "1.11.2", False],
        ]
        for testCase in testCases:
            version1 = Version(testCase[0])
            version2 = Version(testCase[1])
            self.assertEqual(version1 < version2, testCase[2])


if __name__ == '__main__':
    unittest.main()

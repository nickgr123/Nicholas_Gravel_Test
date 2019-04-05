import unittest
from questionA import isOverlapping


class TestisOverlapping(unittest.TestCase):

    def test_isTuple(self):
        testCases = [
            ["string", (0, 1)],
            [(0, 1), "string"],
            [1, "string"],
            [False, (0, 1)],
            [(0, 1), False],
            ["string", False],
            [(0, 1), None],
            [None, None]
        ]
        for testCase in testCases:
            with self.assertRaises(Exception) as e:
                isOverlapping(testCase[0], testCase[1])
            self.assertTrue('Lines must be tuples' in e.exception)

    def test_isTupleProperLength(self):
        testCases = [
            [(0, 1, 2), (1, 2)],
            [(1, None, "string", False), (1, 2)],
            [(0, 1), (1, 2, 3)],
            [(0, 1), (1, False, None, 'string')],
        ]
        for testCase in testCases:
            with self.assertRaises(Exception) as e:
                isOverlapping(testCase[0], testCase[1])
            self.assertTrue('Lines must contain 2 positions' in e.exception)

    def test_tupleContainsIntegers(self):
        testCases = [
            [(1, None), (1, 2)],
            [(0, 1), (1, "string")],
            [(0, 1), (1, 1.234)],
            [(-0.235, 1), (1, 2)],
        ]
        for testCase in testCases:
            with self.assertRaises(Exception) as e:
                isOverlapping(testCase[0], testCase[1])
            self.assertTrue('Positions must be integers' in e.exception)

    def test_isOverlapping(self):
        testCases = [
            [(1, 5), (2, 6), True],
            [(1, 5), (-2, 8), True],
            [(1, 5), (8, -2), True],
            [(5, 1), (8, -6), True],
            [(1, 5), (6, 8), False],
            [(5, 1), (8, 6), False],
            [(-1, -5), (5, 1), False],
        ]
        for testCase in testCases:
            self.assertEqual(isOverlapping(testCase[0], testCase[1]), testCase[2])


if __name__ == '__main__':
    unittest.main()

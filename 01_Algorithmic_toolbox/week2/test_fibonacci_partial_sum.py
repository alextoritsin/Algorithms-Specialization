import unittest
from fibonacci_partial_sum import fib_partial_sum as fib


class TestFiboPartialSum(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(fib(3, 7), 1)

    def test_equal(self):
        self.assertEqual(fib(10, 10), 5)

    def test_more_60(self):
        self.assertEqual(fib(10, 200), 2)

    def test_more_0_and_more_60(self):
        self.assertEqual(fib(0, 239), 0)

if __name__ == '__main__':
    unittest.main()

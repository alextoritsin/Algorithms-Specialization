import unittest, random
from fractional_knapsack import knapsack


class TestFiboPartialSum(unittest.TestCase):

    
    def test_normal(self):
        self.assertEqual(knapsack([(60, 20), (100, 50), (120, 30)], 50), 180.0000)

    def test_one_item(self):
        self.assertEqual(knapsack([(500, 30)], 10), 166.66667)

    
    
    # def test_equal(self):
    #     self.assertEqual(fib(10, 10), 5)

    # def test_more_60(self):
    #     self.assertEqual(fib(10, 200), 2)

    # def test_more_0_and_more_60(self):
    #     self.assertEqual(fib(0, 239), 0)

if __name__ == '__main__':
    unittest.main()

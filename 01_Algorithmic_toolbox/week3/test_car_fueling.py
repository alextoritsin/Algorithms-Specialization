import unittest, random
from car_fueling import count_refils


class TestFiboPartialSum(unittest.TestCase):

    
    def test_normal(self):
        self.assertEqual(count_refils([50, 150, 300, 400, 450, 550, 700], 250), 3)

    
    def test_before_end(self):
        self.assertEqual(count_refils([50, 150, 300, 400, 450, 550, 900], 250), -1)

    def test_exactly(self):
        self.assertEqual(count_refils([50, 150, 300, 400, 450, 550, 800], 250), 3)

    
    def test_no_stop(self):
        self.assertEqual(count_refils([100, 200], 250), 0)

    
    def test_negative(self):
        self.assertEqual(count_refils([1, 2, 5, 9, 10], 3), -1)

    
    def test_abort_afterstart(self):
        self.assertEqual(count_refils([10, 20, 30, 40, 50], 5), -1)

    
    def test_one_stop(self):
        self.assertEqual(count_refils([30, 50], 35), 1)

    
    def test_one_stop_before(self):
        self.assertEqual(count_refils([30, 50], 10), -1)

    
if __name__ == '__main__':
    unittest.main()

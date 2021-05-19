import unittest
from Modules.sum import summation
from Modules.mean import mean


class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it sums up a list of integers.
        """
        data = [1, 2, 3, 4]
        result = summation(data)
        self.assertEqual(result, 10)

    def test_list_float(self):
        """
        Test that it sums up a list of floats
        """
        data = [1/4, 1/4, 1/2]
        result = summation(data)
        self.assertEqual(result, 1.0)

    def test_mean(self):
        """
        Test that it calculates mean of a list of numbers
        """
        data = [1, 2, 3, 4, 5]
        result = mean(data)
        self.assertEqual(result, 3.0)


if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import random
import numpy as np


sys.path.append('../src/')  # noqa
import my_utils


class TestUtils(unittest.TestCase):

    def test_mean(self):

        for i in range(50):
            random_array = [random.randint(0, 100) for _ in range(10)]
            expected = sum(random_array) / len(random_array)
            self.assertEqual(my_utils.mean(random_array), expected)

            np_random_array = np.random.rand(10)
            np_expected = np.mean(np_random_array)
            self.assertAlmostEqual(my_utils.mean(list(np_random_array)),
                                   np_expected, places=5)

        self.assertRaises(SystemExit, my_utils.mean, [])

    def test_median(self):

        for i in range(50):
            random_array = [random.randint(0, 100) for _ in range(11)]
            expected = sorted(random_array)[len(random_array) // 2]
            self.assertEqual(my_utils.median(random_array), expected)

            np_random_array = np.random.rand(10)
            np_expected = np.median(np_random_array)
            self.assertAlmostEqual(my_utils.median(list(np_random_array)),
                                   np_expected, places=5)

        self.assertRaises(SystemExit, my_utils.median, [])

    def test_standard_deviation(self):
        for i in range(50):

            random_array = list(np.random.rand(10))
            np_expected = np.std(random_array)
            self.assertAlmostEqual(my_utils.standard_deviation(random_array),
                                   np_expected, places=5)

        self.assertRaises(SystemExit, my_utils.standard_deviation, [])

    def test_get_column(self):
        result = my_utils.get_column(
            '../src/Agrofood_co2_emission.csv',
            query_column=0,
            query_value='United States of America',
            result_column='Forest fires'
        )

        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        self.assertRaises(SystemExit, my_utils.get_column,
                          'nonexistentdata.csv',
                          query_column=0,
                          query_value='United States of America',
                          result_column='Forest fires')


if __name__ == '__main__':
    unittest.main()

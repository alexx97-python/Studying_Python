"""
our task, is to create NxN multiplication table, of size provided in parameter.
for example, when given size is 3:
1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""

import unittest


def multiplication_table(size):
    if type(size) != int:
        raise ValueError('The provided size should be integer!')
    result = []
    for num in range(1, size + 1):
        result.append([num * n for n in range(1, size + 1)])
    return result


class TestMultiplicationTable(unittest.TestCase):

    def test_multiplication_table_result(self):
        self.assertEqual(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
        self.assertEqual(multiplication_table(4), [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])

    def test_value_rises(self):
        with self.assertRaises(ValueError):
            multiplication_table('3')

        with self.assertRaises(ValueError):
            multiplication_table([4])


if __name__ == '__main__':
    unittest.main()
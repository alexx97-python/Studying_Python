"""
The task is described in the title: find the sum of all numbers with the same digits(permutations) including duplicates.
However, due to the fact that this is a performance edition kata, num can go up to 10**10000.
That's a number with 10001 digits(at most). Be sure to use efficient algorithms and good luck! All numbers
tested for will be positive.

Examples
sum_arrangements(98) returns 89+98 = 187
sum_arrangements(123) returns 1332 #123 + 132 + 213 + 231 + 312 + 321 = 1332
"""

from itertools import permutations
import unittest


def sum_arrangements(num):
    sum_of_all = 0
    list_of_elements = []
    for n in str(num):
        list_of_elements.append(int(n))
    combination = permutations(list_of_elements, len(str(num)))
    for i in list(combination):
        integer = [str(e) for e in i]
        res = int(''.join(integer))
        sum_of_all += res
    return sum_of_all


class TestSumArrangements(unittest.TestCase):

    def test_result(self):
        self.assertEqual(sum_arrangements(123), 1332)
        self.assertEqual(sum_arrangements(1185), 99990)


if __name__ == '__main__':
    unittest.main()
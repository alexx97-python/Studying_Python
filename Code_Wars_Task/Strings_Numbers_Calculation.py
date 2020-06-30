"""
Here you have to do some mathematical operations on a "dirty string". This kata checks some basics,
 it's not too difficult.

So what to do?

Input: String which consists of two positive numbers (doubles) and exactly one operator like +,-,*,/,
always between these numbers. The string is dirty, which means that there are different characters inside too,
not only numbers and the operator. You have to combine all digits left and right, perhaps with "."
inside (doubles) and to calculate the result which has to be rounded to an integer and converted to a string at the end.

Easy example:
Input: "gdfgdf234dg54gf*23oP42"
Output: "54929268" (because 23454*2342=54929268)
First there are some static tests, later on random tests too...

"""
import unittest


def calculate_string(st):
    number1 = 0
    number2 = 0
    numbers = []
    operators = ['+', '-', '*', '/']
    for e in st:
        if e.isdigit() or e == '.':
            numbers.append(e)
        elif e in operators:
            operator = e
            if '.' in numbers:
                number1 = float(''.join(numbers))
            else:
                number1 = int(''.join(numbers))
            numbers = []
    if '.' in numbers:
        number2 = float(''.join(numbers))
    else:
        number2 = int(''.join(numbers))

    if operator == '+':
        return int(round(number1 + number2, 0))
    elif operator == '-':
        return int(round(number1 - number2, 0))
    elif operator == '*':
        return int(round(number1 * number2, 0))
    else:
        return int(round(number1 / number2, 0))


class TestCalculateString(unittest.TestCase):

    def test_result(self):
        self.assertEqual(calculate_string("gdfgdf234dg54gf*23oP42"), 54929268)
        self.assertEqual(calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000"), 47)
        self.assertEqual(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"), -210908)


if __name__ == '__main__':
    unittest.main()

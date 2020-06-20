import unittest
import sys


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_strings_a(self):
        self.assertEqual('a'*6, 'aaaaaa')

    def test_upper(self):
        self.assertEqual('good mood'.upper(), 'GOOD MOOD')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


# Using some unittest decorators
class MyTestCase(unittest.TestCase):

    # just skip this test
    @unittest.skip('demonstrating skipping')
    def test_nothing(self):
        self.fail("shouldn't happen")

    # skip test if condition is True
    @unittest.skipIf(sys.platform.startswith("win"), "Test is not supported in Windows platform")
    def test_format(self):
        pass

    # skip test if condition is False
    @unittest.skipUnless(sys.platform.startswith("notwin"), 'notwin is required')
    def test_windows_support(self):
        pass


if __name__ == '__main__':
    unittest.main()
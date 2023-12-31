from unittest import TestCase

from playground.版本号比较.example_01 import compare_version


class Test(TestCase):
    def test_compare_version(self):
        # self.fail()
        self.assertEqual(compare_version("1.0.0", "0.9.9"), True)
        self.assertEqual(compare_version("1.2.3", "1.1.1"), True)
        self.assertEqual(compare_version("1.1.1", "1.2.3"), False)
        self.assertEqual(compare_version("1.2.3", "1.2.3"), False)
        self.assertEqual(compare_version("2.0.0", "1.9.9"), True)
        self.assertEqual(compare_version("0.0.1", "0.1.1"), False)
        self.assertEqual(compare_version("0.1.1", "0.0.1"), True)


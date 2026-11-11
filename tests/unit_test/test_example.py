import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEquals("hello".upper(), "HELLO")
        self.assertEquals("helLo".upper(), "HELLO")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEquals(s.split(" "), ['hello', 'world'])


if __name__ == '__main__':
    unittest.main()
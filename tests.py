import unittest

class SimpleTestCase(unittest.TestCase):
    """demo travis ci"""

    def test(self):
        self.assertTrue("hello"=="hello")


if __name__ == '__main__':
    unittest.main()

import unittest
from main import KMPSearch

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = KMPSearch("ABABCABAB","ABABDABACDABABCABAB")
        self.assertEqual(res, 10)


if __name__ == '__main__':
    unittest.main()

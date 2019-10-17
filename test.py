import unittest
from main import KMPSearch
  
from lps import computeLPSArray

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
       
        self.assertEqual(KMPSearch("ABABCABAB","ABABDABACDABABCABAB"), 10)


if __name__ == '__main__':
    unittest.main()

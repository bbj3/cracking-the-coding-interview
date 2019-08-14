# 2.3 
def urlify1(string):
  return string.strip().replace(" ", "%20")


import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        str1 = "Mr John Smith      "
        self.assertEqual(urlify1(str1), "Mr%20John%20Smith")

if __name__ == '__main__':
    unittest.main()


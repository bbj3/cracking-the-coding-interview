def IsUnique(mystring):
    a = {}
    for string in mystring:
        if string in a.keys():
            print(mystring + " does not have unique letters ")
            a[string] = a[string]+1
            return False
        else:
            a[string] = 1
    print(mystring + " does indeed have unique letters ")
    return True



import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        rep_str = "ABCdC"
        uniq_str = "ABcd"
        self.assertEqual(IsUnique(rep_str), False)
        self.assertEqual(IsUnique(uniq_str), True)

if __name__ == '__main__':
    unittest.main()
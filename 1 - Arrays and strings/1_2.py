def IsPermutation(mystring1, mystring2):
    
    string1dict = {}
    for string in mystring1:
        if string in string1dict.keys():
            string1dict[string] = string1dict[string]+1
        else:
            string1dict[string] = 1
    
    string2dict = {}
    for string in mystring2:
        if string in string2dict.keys():
            string2dict[string] = string2dict[string]+1
        else:
            string2dict[string] = 1
    
    if (sorted(string2dict.keys())!=sorted(string1dict.keys())):
        print("not permutation")
        return False
    
    for (key,value) in string1dict.items():
        if string2dict[key] != value:
            print("not permutation")
            return False
    print("permuation")
    return True



import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        str1 = "ABBA"
        str2 = "ABBAB"
        str3 = "BABA"
        self.assertEqual(IsPermutation(str1, str2), False)
        self.assertEqual(IsPermutation(str1, str3), True)

if __name__ == '__main__':
    unittest.main()
# 1.9 
def is_rotation(str1, str2):                                                                                                                          
    return(len(str1) == len(str2) and is_one_substring_of_other(str1,str2*2))

def is_one_substring_of_other(str1, str2):
    return(str1 in str2)


import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
    	str1 = "waterbottle"
        str2 = "erbottlewat"
        str3 = "erbottlewata"
        is_rot = string_rotation(str1, str2)
        self.assertEqual(is_rot, True)
        is_rot_2 = string_rotation(str1, str3)
        self.assertEqual(is_rot_2, False)



if __name__ == '__main__':
    unittest.main()
def OneEditAway(str1, str2):
    len1=len(str1)
    len2=len(str2)
    diffcnt = 0
    
    len_diff = abs(len1 - len2)
    if len_diff > 1:
        return False
    if len(str1) > len(str2):
        longer, shorter = str1, str2
    else:
        longer, shorter = str2, str1
    ilong = 0
    ishorter = 0
    while ishorter < len(shorter) and (ilong < len(longer)):
        if longer[ilong]!=shorter[ishorter]:
            diffcnt+= 1
            if not(ilong>ishorter) and len(longer)>len(shorter):
                ilong+=1
            else:
                ilong+=1
                ishorter+=1 
        else:
            ilong+=1
            ishorter+=1
    if diffcnt>1:
        return False
    else:
        return True

import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        onedit = OneEditAway("bales", "pale")
        onedit2 = OneEditAway("bale", "pale")
        onedit3 = OneEditAway("pale", "ple")
        onedit4 = OneEditAway("pales", "pale") 
        onedit5 = OneEditAway("pale", "bale") 
        onedit6 = OneEditAway("pale", "bake")
        self.assertEqual(onedit, False)
        self.assertEqual(onedit2, True)
        self.assertEqual(onedit3, True)
        self.assertEqual(onedit4, True)
        self.assertEqual(onedit5, True)
        self.assertEqual(onedit6, False)


if __name__ == '__main__':
    unittest.main()


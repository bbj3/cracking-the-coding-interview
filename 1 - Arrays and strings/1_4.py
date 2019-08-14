def palindromepermutaion(palinstring):
    letterdict = {}
    for letter in palinstring:
        if letter==" ":
            continue
        if letter in letterdict:
            letterdict[letter]=letterdict[letter]+1
        else:
            letterdict[letter]=1
    oddcnt=0
    for (key,value) in letterdict.items():
        if value%2!=0:
            oddcnt+=1
            if oddcnt>1:
                return True
    return True



import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        str1 = "ABBA"
        str2 = "ABAB"
        str3 = "ABBAc"
        str4 = "ABBAcd"
        self.assertEqual(palindromepermutaion(str1), True)
        self.assertEqual(palindromepermutaion(str2), True)
        self.assertEqual(palindromepermutaion(str3), True)
        self.assertEqual(palindromepermutaion(str4), True)



if __name__ == '__main__':
    unittest.main()
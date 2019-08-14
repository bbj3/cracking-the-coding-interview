# 1.6

def stringcompress(fullstring):
    compressedstring = ""
    i=0
    maxcnt=1
    while i<len(fullstring):
        tmp_cnt=1
        letter = fullstring[i]
        j = i+1
        while (j<len(fullstring) and letter==fullstring[j]):
            j=j+1
            tmp_cnt+=1
        compressedstring = compressedstring + letter +str(tmp_cnt)
        i = i+tmp_cnt
        if tmp_cnt>maxcnt:
            maxcnt=tmp_cnt
    if maxcnt>1:
        return(compressedstring)
    else:
        return(fullstring)


import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        str1 = "ABBA"
        str2 = "aabcccccaaa"
        self.assertEqual(stringcompress(str1), "A1B2A1")
        self.assertEqual(stringcompress(str2), "a2b1c5a3")



if __name__ == '__main__':
    unittest.main()
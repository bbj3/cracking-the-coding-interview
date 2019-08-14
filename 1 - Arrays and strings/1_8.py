def zero_matrix(mat):
    row_dict = {}
    col_dict = {}
    for row in range(0,len(mat)):
        for col in range(0,len(mat[row])):
            if mat[row][col]==0:
                row_dict[row]=True
                col_dict[col]=True
   
    for row in row_dict.keys():
        for col in range(0,len(mat[row])):
            mat[row][col]=0

    for col in col_dict.keys():
        for row in range(0, len(mat)):
            mat[row][col]=0
    return mat


import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
        mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
        self.assertEqual(zero_matrix(mat1), mat2)



if __name__ == '__main__':
    unittest.main()



import math
#1.7
def rotate_matrix_in_place(mat):
    N = len(mat) # we have an NxN matrix
    for circle in range(0,int(math.floor(N/2))):
        for y in range(circle, N-circle-1):
            # store element in right
            tmp = mat[circle][y] # swap top corners

            mat[circle][y] = mat[y][N-1-circle] # right to top

            mat[y][N-circle-1] = mat[N-circle-1][N-y-1]      #bottom to right

            mat[N-circle-1][N-y-1] = mat[N-y-1][circle]# left to bottom

            mat[N-1-y][circle] = tmp

    return(mat)


import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        mat3 = [[1,2,3],[4,5,6],[7,8,9]]
        mat4 = [[3,6,9],[2,5,8],[1,4,7]]
        self.assertEqual(rotate_matrix_in_place(mat3), mat4)



if __name__ == '__main__':
    unittest.main()


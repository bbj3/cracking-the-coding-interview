import unittest
# https://www.afternerd.com/blog/python-check-tree-balanced/
# https://stackoverflow.com/questions/34258139/time-complexity-of-checking-if-a-binary-tree-is-balanced
# https://jelices.blogspot.com/2014/05/leetcode-python-balanced-binary-tree.html
# This is O(n)
def is_balanced_helper(root):
    # a None tree is balanced
    #base case 1
    if root is None:
        return 0
    left_height = is_balanced_helper(root.left)
    # if the left subtree is not balanced, then:
    # this tree is also not balanced
    if left_height == -1:
        return -1
    # if the right subtree is not balanced, then:
    # this tree is also not balanced
    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1
    # if the difference in heights is greater than 1, then:
    # this tree is not balanced
    # base case 2
    if abs(left_height - right_height) > 1:
        return -1
    # this tree is balanced, return its height
    # base case 3
    height = max(left_height, right_height) + 1
    return height

def is_balanced(root):
    return is_balanced_helper(root) > -1


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
 
class Test(unittest.TestCase):
     
    def test_check_balanced(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        self.assertTrue(is_balanced(n1))
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n2.left = n4
        n4.left = n5
        self.assertFalse(is_balanced(n1))
         
         
if __name__ == '__main__':
    unittest.main()

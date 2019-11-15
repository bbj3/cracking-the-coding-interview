import unittest


def check_balanced(node):
    try:
        height = check_balanced_helper(node)
        balanced = True
    except ValueError:
        balanced = False
 
    return balanced

# recusion but breaks if one of the subtrees is unbalanced
def check_balanced_helper(node):
    if not node:
        return 0
 
    left_height = check_balanced_helper(node.left) + 1
    right_height = check_balanced_helper(node.right) + 1
    diff = abs(left_height - right_height)
    if diff > 1:
        raise ValueError("Tree is unbalanced")
 
    return max(left_height, right_height)



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
        self.assertTrue(check_balanced(n1))
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n2.left = n4
        n4.left = n5
        self.assertFalse(check_balanced(n1))
         
         
if __name__ == '__main__':
    unittest.main()
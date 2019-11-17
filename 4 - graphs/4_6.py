# http://www.yujinc.com/4-6-successor-cci/
# [4.6] Successor: Write an algorithm to find the "next"
# node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has 
# a link to its parent.
 
import unittest
 
def get_next_highest_node(node):
     
    if node.right:
        return get_lowest_node(node.right)
    else:
        return get_next_highest_parent(node)
 
def get_lowest_node(node):
    if node.left:
        return get_lowest_node(node.left)
    else:
        return node
 
def get_next_highest_parent(node):
    if not node.parent:
        return None
 
    if node.parent.value > node.value: 
        return node.parent
    else:
        return get_next_highest_parent(node.parent)
 
class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
 
class Test(unittest.TestCase):
 
    def setUp(self):
        self.n5 = TreeNode(5)
        self.n3 = TreeNode(3)
        self.n1 = TreeNode(1)
        self.n4 = TreeNode(4)
        self.n10 = TreeNode(10)
        self.n7 = TreeNode(7)
        self.n6 = TreeNode(6)
        self.n12 = TreeNode(12)

   #      5
  #      / \
   #    3    10
   #  / \   / \
  #  1   4  7  12
 #         /
 #         6
        self.n5.left = self.n3
        self.n3.parent = self.n5
        self.n5.right = self.n10
        self.n10.parent = self.n5
        self.n3.left = self.n1
        self.n1.parent = self.n3
        self.n3.right = self.n4
        self.n4.parent = self.n3
        self.n10.left = self.n7
        self.n7.parent = self.n10
        self.n10.right = self.n12
        self.n12.parent = self.n10
        self.n7.left = self.n6
        self.n6.parent = self.n7
 
    def test_get_next_node(self):        
        self.assertEqual(get_next_highest_node(self.n1), self.n3)
        self.assertEqual(get_next_highest_node(self.n4), self.n5)
        self.assertEqual(get_next_highest_node(self.n6), self.n7)
         
if __name__ == '__main__':
    unittest.main()
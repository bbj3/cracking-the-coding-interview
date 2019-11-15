class Node():
    def __init__(self, data):
        self.right = None
        self.left = None
        self.val = data
    
    def __str__(self):
        return str(self.val)

# A utility function to print the preorder  
# traversal of the BST 
def preOrder(node): 
    if not node: 
        return
    print node.val
    preOrder(node.left) 
    preOrder(node.right) 
        



def createminimalBST(array):
    return createminimalBSThelper(array, 0, len(array)-1)

def createminimalBSThelper(array, start, end):
    if (end < start):
        return
    mid = (start+end)/2
    mynode = Node(array[mid])
    mynode.left = createminimalBSThelper(array, start, mid-1)
    mynode.right = createminimalBSThelper(array, mid+1, end)
    return mynode



import unittest


#      4
#     / \
#    2   6
#   /\  / \
#  1  3 5  7
sorted_array = [1, 2, 3, 4, 5, 6, 7
bst = createminimalBST(sorted_array)
preorder_bst = preOrder(bst)
# should be 4,2,1,3,6,5,7





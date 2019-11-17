import numpy as np
import random

# I used mostly the code from the book.
# there is an alternative solution in the book which only uses one RNG call.
# to see how to delete node from BST see:
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
class TreeNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.size = 1

    def insert(self, node):
    	if node.value < self.value:
    		if not self.left:
    			self.size = self.size+1
    			self.left = node
    			self.left.size = 1
    		else:
    			self.size = self.size+1
    			self.left.insert(node)
        if node.value >= self.value:
    		if not self.right:
    			self.size = self.size+1
    			self.right = node
    			self.right.size = 1
    		else:
    			self.size = self.size+1
    			self.right.insert(node)
    	return

    def getrandomNode(self):
    	if (self.size==1):
    		return self
    	if not self.left:
    		leftsize=0
    	else:
    		leftsize=self.left.size
    	index = random.randint(1, self.size)
    	#print(self.value)
    	if index <= leftsize:
    		return self.left.getrandomNode()
    	if index == leftsize+1:
    		return self
    	else: 
    		return self.right.getrandomNode()

binary_tree = TreeNode(7)
n3 = TreeNode(3)
#n7 = TreeNode(1)
n5 = TreeNode(5)
n10 = TreeNode(10)
n8 = TreeNode(8)
n12 = TreeNode(12)
 

#      7  
#    /   \
#   3     10
#    \    / \
#     5   8  12
binary_tree.insert(n3)
binary_tree.insert(n5)
binary_tree.insert(n10)
binary_tree.insert(n8)
binary_tree.insert(n12)

print("--start")
print(n3.size)
print(n5.size)
print(n10.size)
print(n8.size)
print(n12.size)
print(binary_tree.size)


print("--")
print(binary_tree.size)
list_of_results = []
iterations = 1000000
for i in range(0,iterations):
	rnd_node = binary_tree.getrandomNode().value
	list_of_results.append(rnd_node)
mydict = {}
print("h")
for val in list_of_results:
	#print(mydict[val])
	if val in mydict.keys():
		mydict[val] = mydict[val]+1
	else:
		mydict[val]=1

for val in mydict.keys():
    mydict[val] = float(mydict[val])/iterations
print(mydict)
hist, bin_edges = np.histogram(list_of_results)
print(hist)
print(bin_edges)



# Python program to check binary tree is a subtree of  
# another tree 
# this is O(n)
# The reason the algorithm above works is because to uniquely identify a binary tree, an in-order and pre-order traversal is needed
# see: https://www.geeksforgeeks.org/if-you-are-given-two-traversal-sequences-can-you-construct-the-binary-tree/
# solution comes from here https://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/

# if we had numbers as values we would have to convert them to string by result2 = [str(x) for x in result]

# it's actually enough to just compare the preorder strings if the None(endings) are part of the string.
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

# A utility function to store inorder traversal of tree rooted 
# with root in an array arr[]. Note that i is passed as reference 
def storeInorder(root, arr):
    if (root == None):
        arr.append("-999") #we put in None here
        return
    storeInorder(root.left, arr)
    arr.append(root.data)
    storeInorder(root.right, arr)
    return

# A utility function to store inorder traversal of tree rooted 
# with root in an array arr[]. Note that i is passed as reference 
def storePreOrder(root, arr):
    if (root == None):
        arr.append("-999") #we put in None here
        return
    arr.append(root.data)
    storePreOrder(root.left, arr)
    storePreOrder(root.right, arr)
    return

# This function returns true if S is a subtree of T, otherwise false */
def isSubtree(T, S):

    #/* base cases */
    if (S == None):  
    	return True
    if (T == None):
        return False
  
    # Store Inorder traversals of T and S in inT[0..m-1] 
    # and inS[0..n-1] respectively 

    inT = list() 
    inS = list()
    storeInorder(T, inT)
    storeInorder(S, inS) 
    
    inT = '-'.join(inT)
    inS = '-'.join(inS)
    #inT[m] = '\0', inS[n] = '\0'; 
  
    # If inS[] is not a substring of preS[], return false 
    if not(inS in inT):
        return False
  
    # Store Preorder traversals of T and S in inT[0..m-1] 
    # and inS[0..n-1] respectively 
    preT = list() 
    preS = list()
    storePreOrder(T, preT) 
    storePreOrder(S, preS);
    preS ='-'.join(preS)
    preT = '-'.join(preT)
    #preT[m] = '\0', preS[n] = '\0'; 
  
     #If inS[] is not a substring of preS[], return false 
     #Else return true 
    if preS in preT:
    	return True
    else:
    	return False


T = Node('a'); 
T.left = Node('b'); 
T.right = Node('d'); 
T.left.left = Node('c');
T.left.right = Node('k'); 
T.right.right = Node('e'); 

                    #    a
                    #   / \
                    #   b  d
                    #  / \  \
 					# c  k  e

  
S = Node('a'); 
S.left = Node('b'); 
S.left.left = Node('c'); 
S.right = Node('d'); 

S2 = Node('a'); 
S2.left = Node('b'); 
S2.left.left = Node('d'); 

S3 = Node('b'); 
S3.left = Node('c'); 
S3.right = Node('k'); 


if (isSubtree(T, S)):
    print("Yes: S is a subtree of T")
else:
    print("No: S is NOT a subtree of T")
  
if (isSubtree(T, S2)):
    print("Yes: S2 is a subtree of T")
else:
    print("No: S2 is NOT a subtree of T")


if (isSubtree(T, S3)):
    print("Yes: S3 is a subtree of T")
else:
    print("No: S3 is NOT a subtree of T")


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

def countPathsWithSum(root, targetsum):
    if(not root):
        return 0

    pathsFromRoot = countPathsWithSumFromNode(root, targetsum, 0)
    
    pathsOnLeft = countPathsWithSum(root.left, targetsum)
    pathsOnRight = countPathsWithSum(root.right, targetsum)
    print("----")
    print("root.data")
    try:
        print(root.data)
    except AttributeError:
        pass
    print("pathsFromRoot")
    print(pathsFromRoot)
    print("root.right.data")
    try:
        print(root.right.data)
    except AttributeError:
        pass
    print("pathsOnRight")
    print(pathsOnRight)
    print("root.left.data")
    try:
        print(root.left.data)
    except AttributeError:
        pass
    print("pathsOnLeft")
    print(pathsOnLeft)
    
    return pathsFromRoot + pathsOnLeft+pathsOnRight


def countPathsWithSumFromNode(node, targetsum, tmpsum):
    if(not node):
        return 0

    tmpsum = node.data+tmpsum
    totalpaths=0
    if(tmpsum==targetsum):
        totalpaths=totalpaths+1

    totalpaths = totalpaths+countPathsWithSumFromNode(node.left, targetsum, tmpsum)
    totalpaths = totalpaths+countPathsWithSumFromNode(node.right, targetsum, tmpsum)
    return totalpaths


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3
n2.left = n4
n3.right = n5
n3.left=n6


a = countPathsWithSum(n1, 6)
print(a)


#                 1
#               /   \ 
#              2     3
#             /     / \
#            4     6   5
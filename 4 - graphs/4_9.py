import pprint
import unittest
 
class Node(object):
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value
 
def weave(arr1, arr2, prefix, result):
    if (len(arr1)==0 or len(arr2)==0):
        print("now appending")
        print(prefix)
        print(arr1)
        print(arr2)
        result.append(prefix + arr1 + arr2)
        return result

    h1 = arr1.pop(0)
    prefix += [h1]
    weave(arr1, arr2, prefix, result)
    prefix.pop()
    arr1.insert(0, h1)
 
    h2 = arr2.pop(0)
    prefix += [h2]
    weave(arr1, arr2, prefix, result)
    prefix.pop()
    arr2.insert(0, h2)
    return result
 
def bst_seq(node):
    if not node:
        return []
     
    if not node.left and not node.right:
        return [[node.value]]
 
    bst_result = []
    left_lists = bst_seq(node.left)
    right_lists = bst_seq(node.right)
 
    if left_lists and right_lists:
        for left_seq in left_lists:
            for right_seq in right_lists:
                suffix = weave(left_seq, right_seq, [], [])
                bst_result += [[node.value] + seq for seq in suffix]
    else:
        remaining = left_lists or right_lists
        bst_result += [[node.value] + a_seq for a_seq in remaining]
 
    return bst_result

root = Node(value=4)
n2 = Node(value=2)
n6 = Node(value=6)
n5 = Node(value=5)
n7 = Node(value=7)
#         4
#        / \
#       2   6
#          / \
#         5   7
 
root.left = n2
root.right = n6
n6.left = n5
n6.right = n7
a = bst_seq(root)

print(a)
 
b = weave([1,2], [3,4], [], [])
print(b)

import unittest


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
 
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def printAll(self):
        mynode = self
        while mynode:
            print(mynode)
            mynode = mynode.next

 
def create_lists_per_level(node, depth, levels=[]):
    if not node:
        return
 
    if depth == 0:
        levels.append(Node(node.value))
    else:
        if depth >= len(levels):
            levels.append(Node(node.value))
        else:
            level = levels[depth]
            while level:
                previous = level
                level = level.next
 
            previous.next = Node(node.value)
 
    create_lists_per_level(node.left, depth+1, levels)
    create_lists_per_level(node.right, depth+1, levels)
    return levels


if __name__ == "__main__" :
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)

    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5
    node_3.left = node_6
    node_3.right = node_7

    #                1
    #               /   \
    #             2     3
    #            / \   / \
    #           4  5   6  7

    myll = create_lists_per_level(node_1,0)
    for n in myll:
        print("--")
        n.printAll()


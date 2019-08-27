import copy
import unittest

# simple node class
class Node:
    def __init__(self, dataval=None, mynext=None):
        self.dataval = dataval
        self.next = mynext
    def __str__(self):
        return str(self.dataval)


# simple linked list class
class SLinkedList:
    def __init__(self):
        self.headval = None

    def __str__(self):
        tmpnode = self.headval
        val_list = []
        while tmpnode is not None:
            val_list.append(tmpnode.dataval)
            tmpnode = tmpnode.next
        str_val = '->'.join(str(e) for e in val_list)
        return(str_val)


def intersection(myLL1, myLL2):
    nodes = {}
    node = myLL1.headval
    while node:
        nodes[node] = True
        node = node.next
    node = myLL2.headval
    while node:
        if node in nodes:
            return node
        node = node.next
    return None


class TestStringMethods(unittest.TestCase):

    def test_removemiddle(self):

        node1 = Node(70)
        node2 = Node(90)
        node3 = Node(50)
        node4 = Node(40)
        node1.next = node2
        node2.next = node3
        node3.next = node4 # 70-90-50-40

        
        nodea = Node(70)
        nodeb = Node(80)
        nodec = Node(10)

        nodea.next = nodeb # 70-80-90-10
        nodeb.next = node2
        node2.next = nodec


        llist1 = SLinkedList()
        llist1.headval = nodea
        llist2 = SLinkedList()
        llist2.headval = node1
        # first test with intersecting nodes
        self.assertEqual(intersection(llist1, llist2), node2)

        nodea.next = nodeb
        nodeb.next = nodec
        llist3 = SLinkedList()
        llist1.headval = nodea
        self.assertEqual(intersection(llist3, llist2), None)




if __name__ == '__main__':
    unittest.main()


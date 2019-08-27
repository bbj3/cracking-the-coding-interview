import copy
# simple node class
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None

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


    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.next

    #1.1 - using hashtables
    def remove_duplicates_hash(self):
        values ={}
        node = self.headval
        values[node.dataval]=True
        while(node.next):
            if (node.next.dataval in values)  and values[node.next.dataval]==True:
                node.next = node.next.next
            else:
                values[node.next.dataval]=True
                node = node.next

    #1.1 - O(N^2)
    def remove_duplicates(self):
        values ={}
        node = self.headval
        node_ahead = self.headval
        while(node):
            node_behind = node
            node_ahead = node.next
            while(node_ahead):
                if node_ahead and node_ahead.dataval == node.dataval:
                    node_behind.next = node_ahead.next
                    if (node_ahead.next):
                        node_ahead.next = node_ahead.next.next
                node_behind = node_ahead
                node_ahead = node_ahead.next
            node = node.next

import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
        llist = SLinkedList()
        llist.headval = Node("Mon")
        e2 = Node("Tue")
        e3 = Node("Thu")
        e4 = Node("Thu")
        llist.headval.next = e2
        e2.next = e3
        e3.next = e4
        llist.listprint()
        llist2 =copy.deepcopy(llist)

        llist.remove_duplicates_hash()
        llist2.remove_duplicates()

        self.assertEqual(str(llist), "Mon->Tue->Thu")
        self.assertEqual(str(llist2), "Mon->Tue->Thu")

if __name__ == '__main__':
    unittest.main()

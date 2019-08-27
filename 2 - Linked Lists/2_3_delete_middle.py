import copy
# simple node class
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None
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

# 2.3
# because we only have access to the one node we want to delete we have to change that node
def delete_middle_node(mynode):
    nextnode = mynode.next
    mynode.dataval = nextnode.dataval
    mynode.next = nextnode.next
    return()



import unittest

class TestStringMethods(unittest.TestCase):

    def test_removemiddle(self):
        llist = SLinkedList()
        llist.headval = Node("Mon")
        e2 = Node("Tue")
        e3 = Node("wed")
        e4 = Node("thu")
        e5 = Node("fri")
        e6 = Node("sat")
        e7 = Node("sun")

        llist.headval.next = e2
        e2.next = e3
        e3.next = e4
        e4.next = e5
        e5.next = e6
        e6.next = e7
        delete_middle_node(e4)
        self.assertEqual(str(llist), "Mon->Tue->wed->fri->sat->sun")


if __name__ == '__main__':
    unittest.main()

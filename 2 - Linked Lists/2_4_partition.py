import copy
import unittest

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



def partitionlinkedlist(mylinkedlist, k):
    llistsmaller = SLinkedList()
    llistbigger = SLinkedList()

    tmpnode = mylinkedlist.headval
    smalltmpnode = llistsmaller.headval
    bigtmpnode = llistbigger.headval
    while(tmpnode):

        if tmpnode.dataval>=k:
            if bigtmpnode==None: # first node to linked list
                bigtmpnode = Node()
                bigtmpnode.dataval = tmpnode.dataval
                bigtmpnode.next = None
                llistbigger.headval = bigtmpnode
            elif (bigtmpnode):
                newnode = Node(dataval=tmpnode.dataval)
                bigtmpnode.next = newnode
                bigtmpnode = bigtmpnode.next
        else:
            if smalltmpnode==None:
                smalltmpnode = Node()
                smalltmpnode.dataval = tmpnode.dataval
                smalltmpnode.next = None
                llistsmaller.headval = smalltmpnode
            elif (smalltmpnode):
                newnode = Node(dataval=tmpnode.dataval)
                smalltmpnode.next = newnode
                smalltmpnode = smalltmpnode.next
        tmpnode = tmpnode.next
    smalltmpnode.next = llistbigger.headval # glue the two list together

    return llistsmaller


class TestStringMethods(unittest.TestCase):

    def test_removemiddle(self):
        llist = SLinkedList()
        llist.headval = Node(3)
        e2 = Node(5)
        e3 = Node(8)
        e4 = Node(5)
        e5 = Node(10)
        e6 = Node(2)
        e7 = Node(1)

        llist.headval.next = e2
        e2.next = e3
        e3.next = e4
        e4.next = e5
        e5.next = e6
        e6.next = e7

        a= partitionlinkedlist(llist, 5)
        self.assertEqual(str(a), "3->2->1->5->8->5->10")

if __name__ == '__main__':
    unittest.main()



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


def sumlists(node1, node2):
    
    carry = 0
    mynode = Node()
    sumlist = SLinkedList()
    while(node1 or node2 or carry!=0):
        mysum = 0
        if node1:
            mysum = mysum+node1.dataval
            node1 = node1.next
        if node2:
            mysum=mysum+node2.dataval
            node2 = node2.next
        if carry:
            mysum=mysum+carry

        rest = mysum%10     # if mysum is 12 then this is 2
        carry= mysum/10     # if mysum is 12 then this is 1

        if not mynode.dataval:
            mynode = Node(rest)
            sumlist.headval = mynode
        else:
            tmpnode = Node(rest)
            mynode.next = tmpnode
            mynode = mynode.next
    return(sumlist)


class TestStringMethods(unittest.TestCase):

    def test_removemiddle(self):
        n1 = Node(7)
        n2 = Node(1)
        n1.next=n2
        n3 = Node(6)
        n2.next = n3

        u1 = Node(5)
        u2 = Node(9)
        u1.next=u2
        u3 = Node(2)
        u2.next = u3

        llist1 = SLinkedList()
        llist1.headval = n1
        llist2 = SLinkedList()
        llist2.headval = u1

        a = sumlists(n1, u1)
        self.assertEqual(str(a), "2->1->9")

if __name__ == '__main__':
    unittest.main()


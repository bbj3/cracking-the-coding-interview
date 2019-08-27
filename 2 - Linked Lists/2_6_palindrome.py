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

def palindrome(myLL):
    tmpnode = myLL.headval
    mystack = []
    while tmpnode:
        mystack.append(tmpnode)
        tmpnode =tmpnode.next
    tmpnode = myLL.headval

    while tmpnode:
        backwards = mystack.pop()
        if tmpnode.dataval!=backwards.dataval:
            return False
        tmpnode = tmpnode.next
    return True



class TestStringMethods(unittest.TestCase):

    def test_removemiddle(self):
        llist = SLinkedList()
        llist.headval = Node("A")
        e2 = Node("B")
        e3 = Node("B")
        e4 = Node("A")
        llist.headval.next = e2
        e2.next = e3
        e3.next = e4

        llist2 = SLinkedList()
        llist2.headval = Node("A")
        e2 = Node("B")
        e3 = Node("L")
        e4 = Node("A")
        llist2.headval.next = e2
        e2.next = e3
        e3.next = e4

        nodes = {}
        nodes[e2] = True
        a = palindrome(llist)

        b = palindrome(llist2)
        self.assertEqual(a, True)
        self.assertEqual(b, False)



if __name__ == '__main__':
    unittest.main()



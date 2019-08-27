import copy
# simple node class
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None
    def __str__(self):
        str(self.dataval)

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


# 2.2 -  kth to last
def kth_to_last(linkedlist, k):
    head =linkedlist.headval
    front_node = head
    for i in range(0, k):
        front_node = front_node.next
    
    node_behind = head
    while(front_node.next):
        front_node = front_node.next
        node_behind = node_behind.next

    kth_to_last_val = node_behind.dataval
    return(kth_to_last_val)



import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_unique(self):
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

        k_last_element = kth_to_last(llist, 2)
        self.assertEqual(str(k_last_element), "fri")

if __name__ == '__main__':
    unittest.main()

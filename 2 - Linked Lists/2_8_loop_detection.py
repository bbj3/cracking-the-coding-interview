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


# 2.8 
def detect_cycle(head):
    nodes = {}
    node = head
    while node:
        if node in nodes:
            return node
        nodes[node] = True
        node = node.next
    return None



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

		a = detect_cycle(llist.headval)
		self.assertEqual(a, None)
		e6.next = e4
		a = detect_cycle(llist.headval)
		self.assertEqual(a, e4)

if __name__ == '__main__':
    unittest.main()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return(str(self.data))

class MinStack:
    
    def __init__(self):
        self.top=None
        self.min_top = None

    def __str__(self):
        mynode  = self.top
        if mynode==None:
            return("None")
        mynodestr = str(mynode.data)
        while mynode.next:
            mynodestr = str(mynode.next.data)+"<-"+mynodestr
            mynode = mynode.next
        return(mynodestr)


    def push(self,data):
        self.push2MinStack(data)
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode
        return


    def push2MinStack(self,data):
        if self.min_top==None:
            self.min_top = Node(data)
        elif data<self.min_top.data:
            new_min_node = Node(data)
            new_min_node.next = self.min_top
            self.min_top = new_min_node
        else:
            new_min_node = Node(self.min_top.data)
            new_min_node.next = self.min_top
            self.min_top = new_min_node
        return
    

    def pop(self):
        temp = self.popstack(self.top, "list")
        self.popstack(self.min_top, "minlist")
        return temp


    def min(self):
        if self.isitempty(self.min_top):
            return None
        else:
            return self.min_top.data 


    def isitempty(self, topofStack):
        if (topofStack is None):
            return True 
        else:
            return False


    def popstack(self, topofStack, list_descr):
        empty = self.isitempty(topofStack)
        if (empty):
            return None
        temp=topofStack
        if list_descr == "list":
            self.top=topofStack.next
        else:
            self.min_top=topofStack.next
        popped=temp
        return popped

    def peek(self):
        return self.top.data


import unittest

class TestStringMethods(unittest.TestCase):

    def test_min_stack(self):

        mystack = MinStack()
        mystack.push(100)
        self.assertEqual(mystack.min(), 100)
        mystack.push(-100)
        self.assertEqual(mystack.min(), -100)
        mystack.push(100)
        self.assertEqual(mystack.min(), -100)
        mystack.push(-1000)
        self.assertEqual(mystack.min(), -1000)
        mystack.pop()
        self.assertEqual(mystack.min(), -100)
        mystack.pop()
        self.assertEqual(mystack.min(), -100)
        mystack.pop()
        self.assertEqual(mystack.min(), 100)
        mystack.pop()
        self.assertEqual(mystack.min(), None)
        


if __name__ == '__main__':
    unittest.main()



